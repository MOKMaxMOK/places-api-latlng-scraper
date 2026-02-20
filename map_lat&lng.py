import requests
import json
import time
import os

# ================= CONFIGURATION =================
# ⚠️ WARNING: Do not commit your actual API key to GitHub!
# Replace the string below with your actual Google Maps API Key.
# Replace the string below with your actual Google Maps API Key.
# Replace the string below with your actual Google Maps API Key.
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
# Replace the string below with your actual Google Maps API Key.
# Replace the string below with your actual Google Maps API Key.
# Replace the string below with your actual Google Maps API Key.



# Default output file name
OUTPUT_FILE = "locations_lat_long.json"

# List of locations to query
# Format: {"name": "Display Name", "query": "Search query (Name + Address recommended for accuracy)"}
spots_data = [
    # Example:
    # {"name": "Central-Mid-Levels Escalator", "query": "Central-Mid-Levels Escalator Jubilee Street Central"},
]


# ==================================================

def search_place(spot):
    """
    Queries the Google Places API to fetch latitude, longitude, and formatted address.
    """
    url = "https://places.googleapis.com/v1/places:searchText"

    # Using the "query" field which combines name and address for better accuracy
    payload = {
        "textQuery": spot["query"]
    }

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
            lat = place["location"]["latitude"]
            lng = place["location"]["longitude"]

            return {
                "name": spot["name"],  # The original name you want to display
                "search_query": spot["query"],
                "google_address": place.get("formattedAddress"),  # The actual address returned by Google Maps
                "lat": lat,
                "lng": lng,
                "place_id": place["id"],
                "error": None
            }
        else:
            return {"name": spot["name"], "lat": 0, "lng": 0, "error": "Not Found"}

    except Exception as e:
        return {"name": spot["name"], "lat": 0, "lng": 0, "error": str(e)}


def main():
    # Prevent execution if the API key is not set
    if API_KEY == "YOUR_GOOGLE_MAPS_API_KEY" or not API_KEY:
        print("❌ ERROR: Please set your Google Maps API Key in the API_KEY variable!")
        return

    # Prevent execution if the data list is empty
    if not spots_data:
        print("⚠️ WARNING: The 'spots_data' list is empty. Please add locations to search.")
        return

    results = []
    print(f"🚀 Starting to query {len(spots_data)} locations...")
    print("-" * 50)

    for i, spot in enumerate(spots_data):
        print(f"[{i + 1}/{len(spots_data)}] 🔍 Querying: {spot['name']} ...", end=" ", flush=True)
        result = search_place(spot)

        if result.get("lat") != 0 and result.get("error") is None:
            print("✅ Success")
        else:
            print(f"❌ Failed (Reason: {result.get('error')})")

        # Remove the error key before saving to JSON to keep the output clean
        if "error" in result:
            del result["error"]

        results.append(result)

        # Short delay to prevent hitting API rate limits
        time.sleep(0.1)

    # Save results to a JSON file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("-" * 50)
    print(f"🎉 Done! Results have been saved to: {os.path.abspath(OUTPUT_FILE)}")


if __name__ == "__main__":
    main()
