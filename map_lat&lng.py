import requests
import json
import time
import os

# ================= CONFIGURATION =================

# ⚠️ ============================================ ⚠️
# ⚠️  Replace the key below with your own API Key  ⚠️
# ⚠️ ============================================ ⚠️
API_KEY = "your key"
# ⚠️ ============================================ ⚠️
# ⚠️  Replace the key above with your own API Key  ⚠️
# ⚠️ ============================================ ⚠️

OUTPUT_FILE = "locations_lat_long.json"

# Optional: Set a default city/region to improve search accuracy.
# If your locations are from multiple cities, leave this empty ("") and
# include the city name directly in each spot's "name" or "address" field.
TARGET_CITY = " "  # e.g. "Hong Kong", "Tokyo", "London" or leave empty ""

# ▼▼▼ ADD YOUR LOCATIONS HERE ▼▼▼
spots_data = [
    # Format 1 — Name only (script will append TARGET_CITY automatically)
    {"name": " "},

    # Format 2 — Name + Address (recommended when address is available, more precise)
    {"name": " ", "address": " "},
]
# ▲▲▲ DONE. Run the script after filling in the list. ▲▲▲
# ==================================================

def build_query(spot):
    """
    Builds the search query string from name, optional address, and optional TARGET_CITY.
    """
    parts = [spot.get("name", "")]
    if spot.get("address"):
        parts.append(spot["address"])
    if TARGET_CITY:
        parts.append(TARGET_CITY)
    return " ".join(parts)


def search_place(spot):
    """
    Queries the Google Places API to fetch latitude, longitude, and formatted address.
    """
    url = "https://places.googleapis.com/v1/places:searchText"

    search_query = build_query(spot)
    payload = {"textQuery": search_query}
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.id,places.displayName,places.location,places.formattedAddress"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if "places" in data and len(data["places"]) > 0:
            place = data["places"][0]
            return {
                "name": spot.get("name"),
                "search_query": search_query,
                "google_address": place.get("formattedAddress"),
                "lat": place["location"]["latitude"],
                "lng": place["location"]["longitude"],
                "place_id": place["id"],
                "error": None
            }
        else:
            return {"name": spot.get("name"), "lat": 0, "lng": 0, "error": "Not Found"}

    except Exception as e:
        return {"name": spot.get("name"), "lat": 0, "lng": 0, "error": str(e)}


def main():
    if API_KEY == "YOUR_GOOGLE_MAPS_API_KEY" or not API_KEY:
        print("❌ ERROR: Please set your Google Maps API Key in the API_KEY variable!")
        return

    if not spots_data:
        print("⚠️  WARNING: The 'spots_data' list is empty. Please add locations to search.")
        return

    if not TARGET_CITY:
        print("💡 TIP: TARGET_CITY is not set.")
        print("   To avoid matching wrong locations, include city name in each entry.")
        print('   e.g. {"name": "Eiffel Tower", "address": "Paris"}')
        print("-" * 50)

    results = []
    city_label = f" in {TARGET_CITY}" if TARGET_CITY else ""
    print(f"🚀 Starting to query {len(spots_data)} location(s){city_label}...")
    print("-" * 50)

    for i, spot in enumerate(spots_data):
        print(f"[{i + 1}/{len(spots_data)}] 🔍 Querying: {spot['name']} ...", end=" ", flush=True)
        result = search_place(spot)

        if result.get("lat") != 0 and result.get("error") is None:
            print("✅ Success")
        else:
            print(f"❌ Failed (Reason: {result.get('error')})")

        if "error" in result:
            del result["error"]

        results.append(result)
        time.sleep(0.1)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("-" * 50)
    print(f"🎉 Done! Results have been saved to: {os.path.abspath(OUTPUT_FILE)}")


if __name__ == "__main__":
    main()
