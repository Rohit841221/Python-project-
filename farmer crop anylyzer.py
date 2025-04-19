#!/usr/bin/python3

# Data in list of dictionaries
farmers = [
    {"name": "Ramu", "state": "Punjab", "crop": "Wheat", "land": 5, "production": 50},
    {"name": "Sita", "state": "UP", "crop": "Rice", "land": 3, "production": 28},
    {"name": "Mohan", "state": "Maharashtra", "crop": "Sugarcane", "land": 10, "production": 200},
    {"name": "Geeta", "state": "Punjab", "crop": "Wheat", "land": 7, "production": 65},
    {"name": "Karan", "state": "Bihar", "crop": "Maize", "land": 4, "production": 30},
    {"name": "Radha", "state": "UP", "crop": "Rice", "land": 2, "production": 18},
    {"name": "Suraj", "state": "Maharashtra", "crop": "Sugarcane", "land": 12, "production": 250}
]

# Calculate yield and category
for f in farmers:
    yield_per_acre = f["production"] / f["land"]
    f["yield"] = round(yield_per_acre, 2)

    if yield_per_acre < 10:
        f["category"] = "Low"
    elif yield_per_acre < 20:
        f["category"] = "Medium"
    else:
        f["category"] = "High"

# Display all farmer data
print("=== Farmers Data ===")
for f in farmers:
    print(f)

# State-wise average yield
print("\n=== State-wise Average Yield ===")
state_yields = {}
state_counts = {}

for f in farmers:
    state = f["state"]
    state_yields[state] = state_yields.get(state, 0) + f["yield"]
    state_counts[state] = state_counts.get(state, 0) + 1

for state in state_yields:
    avg = round(state_yields[state] / state_counts[state], 2)
    print(f"{state}: {avg} Qtl/Acre")

# Top farmer by each crop
print("\n=== Top Farmers by Crop ===")
crop_topper = {}
for f in farmers:
    crop = f["crop"]
    if crop not in crop_topper or f["yield"] > crop_topper[crop]["yield"]:
        crop_topper[crop] = f

for crop in crop_topper:
    top = crop_topper[crop]
    print(f"{crop}: {top['name']} with {top['yield']} Qtl/Acre")