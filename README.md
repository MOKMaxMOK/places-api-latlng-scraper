# places-api-latlng-scraper

# Google Places Batch Geocoder 🌍

A simple and efficient Python script designed to batch query the [Google Places API (New)](https://developers.google.com/maps/documentation/places/web-service/op-overview). It takes a list of location names/addresses and automatically fetches their precise **Latitude**, **Longitude**, and **Formatted Address**, saving the results into a clean JSON file.

### ✨ Features
- **Highly Accurate:** Combines "Location Name + Address" for precise querying.
- **Batch Processing:** Processes multiple locations automatically with built-in delay to respect API rate limits.
- **Clean Output:** Exports structured data to a JSON file, ready for integration into frontend maps (e.g., Vue.js, MapLibre, Leaflet).
- **Error Handling:** Gracefully handles "Not Found" locations or API errors without crashing the script.
- **Almost free for small projects:** You can search 11,000 locations for free each month.

## 🔑 How to get a Google Maps API Key

To use this script, you need a valid Google Cloud API key with the **Places API (New)** enabled.

### Step 1: Create a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the project drop-down menu at the top left and select **New Project**.
3. Enter a project name and click **Create**.

### Step 2: Enable Billing
*Note: Google Maps APIs require an active billing account, but Google provides a **$200 recurring monthly credit**, which is more than enough for small projects and batch processing.*
1. Go to the **Billing** section in the left-hand navigation menu.
2. Link an existing billing account or create a new one by adding a payment method.

### Step 3: Enable the Places API
1. In the left menu, navigate to **APIs & Services** > **Library**.
2. Search for **Places API (New)**. *(Ensure it is the "New" version, as this script uses the `v1/places:searchText` endpoint).*
3. Click on the API and press **Enable**.

### Step 4: Generate the API Key
1. Go to **APIs & Services** > **Credentials**.
2. Click **+ CREATE CREDENTIALS** at the top and select **API key**.
3. A pop-up will appear with your new API key. Copy this key.

### Step 5: Secure Your Key (Crucial!)
To prevent unauthorized usage and unexpected charges, you should restrict your key:
1. Click on your newly created API key to edit its settings.
2. Scroll down to **API restrictions** and select **Restrict key**.
3. Check the box for **Places API (New)** from the dropdown list.
4. Click **Save**.

Finally, paste the copied key into the `API_KEY` variable inside the Python script!
<img width="1194" height="472" alt="image" src="https://github.com/user-attachments/assets/eefdca3b-b9f5-4770-a99e-48899924a378" />




effect:
<img width="1714" height="1062" alt="image" src="https://github.com/user-attachments/assets/f2dc5018-d0f6-41ae-995b-94931bc73f5a" />

automatically create and save to location_lat_long.json
<img width="1250" height="928" alt="image" src="https://github.com/user-attachments/assets/f27abc10-1a52-4737-a189-e323000d252b" />


