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
