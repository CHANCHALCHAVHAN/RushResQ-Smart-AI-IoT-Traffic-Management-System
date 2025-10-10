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
