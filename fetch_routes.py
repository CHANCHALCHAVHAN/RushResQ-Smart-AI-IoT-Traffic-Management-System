import requests
import time
import json
from tabulate import tabulate   # pip install tabulate
from collections import defaultdict

# 🔴 Replace with your actual API endpoint
API_URL = "https://sheetdb.io/api/v1/h6hsy831jb8wp"

# Priority order: lower number = higher priority
PRIORITY_ORDER = {
    "ambulance": 1,
    "fire": 2,
    "firetruck": 2,
    "police": 3
}

def fetch_routes_once():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
   # Ensure it's a list of records
        routes = data.get("routes") if isinstance(data, dict) else data
        if not isinstance(routes, list):
            print("❌ ERROR: Expected a list of routes, got:", type(routes))
            return

        # Extract and normalize
        extracted = []
        for r in routes:
            route_no = r.get("Route Number", "UNKNOWN")
            vehicle = r.get("Vehicle Type", "other").lower()
            vehicle_id = r.get("Vehicle ID", "N/A")
            caller = r.get("Caller Name", "N/A")
            timestamp = r.get("Timestamp", "N/A")

            extracted.append({
                "Route": route_no,
                "Vehicle": vehicle,
                "Vehicle ID": vehicle_id,
                "Caller": caller,
                "Timestamp": timestamp
            })

        # ✅ Group by Route (lane)
        lanes = defaultdict(list)
        for item in extracted:
            lanes[item["Route"]].append(item)

        # ✅ Decide priority within each lane
        lane_decisions = {}
        for route_no, vehicles in lanes.items():
            vehicles_sorted = sorted(vehicles, key=lambda v: PRIORITY_ORDER.get(v["Vehicle"], 99))
            lane_decisions[route_no] = vehicles_sorted[0]  # top vehicle in this lane


        # Print all data
        print("\n✅ Live Data (All Vehicles):\n")
        table = [[r["Route"], r["Vehicle"], r["Vehicle ID"], r["Caller"], r["Timestamp"]] for r in extracted]
        print(tabulate(table, headers=["Route", "Vehicle", "Vehicle ID", "Caller", "Timestamp"], tablefmt="grid"))

        # Print lane-level priority
        print("\n🚦 Lane Decisions (Highest Priority in each lane):\n")
        decision_table = []
        for route_no, top in lane_decisions.items():
            decision_table.append([route_no, top["Vehicle"], top["Caller"], top["Timestamp"]])
        print(tabulate(decision_table, headers=["Route", "Top Vehicle", "Caller", "Timestamp"], tablefmt="grid"))

        # ✅ FINAL DECISION: Which route gets overall priority
        sorted_routes = sorted(lane_decisions.values(), key=lambda v: PRIORITY_ORDER.get(v["Vehicle"], 99))
        if sorted_routes:
            final = sorted_routes[0]
            print(f"\n🚨 FINAL DECISION: Selected Route = {final['Route']} | Vehicle = {final['Vehicle'].upper()} | Caller = {final['Caller']}")
        else:
            print("⚠️ No routes available for decision.")

    except Exception as e:
        print("⚠️ Error fetching data:", e)


