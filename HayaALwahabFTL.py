"""
FTL SYRIA - PYTHON INDIVIDUAL PRACTICAL ASSIGNMENT
Submission Deadline: Friday, 25 September 2026
Author Solution File
"""

# ==============================================================================
# EXERCISE 1: Python Data Structures and Loops
# ==============================================================================
print("=" * 60)
print("EXERCISE 1: Python Data Structures and Loops")
print("=" * 60)

# Create climate information for 6 cities using a list of dictionaries
# Includes one city (Deir ez-Zor) with missing temperature value (None)
cities_data = [
    {"city": "Damascus", "temperature": 38.5, "humidity": 30, "rainfall": 2.0},
    {"city": "Aleppo", "temperature": 41.2, "humidity": 25, "rainfall": 0.5},
    {"city": "Homs", "temperature": 32.0, "humidity": 45, "rainfall": 12.0},
    {"city": "Latakia", "temperature": 28.5, "humidity": 75, "rainfall": 25.0},
    {"city": "Deir ez-Zor", "temperature": None, "humidity": 20, "rainfall": 0.0}, # Missing temperature
    {"city": "Palmyra", "temperature": 42.0, "humidity": 15, "rainfall": 1.0}
]

# 1, 2, 3 & 4. Loop, handle missing value using continue, classify temperature
valid_temperatures = []
city_classifications = {}

print("\n--- Displaying & Classifying City Climate Information ---")
for city in cities_data:
    name = city["city"]
    temp = city["temperature"]
    hum = city["humidity"]
    rain = city["rainfall"]
    
    # 2 & 3. Check for missing temperature and use 'continue' to skip
    if temp is None:
        print(f"Skipping {name}: Missing temperature data.")
        continue
    
    # Track valid temperatures
    valid_temperatures.append(temp)
    
    # 4. Temperature classification logic
    if temp >= 40:
        category = "Extreme Heat"
    elif temp >= 35:
        category = "High Heat"
    elif temp >= 30:
        category = "Moderate Heat"
    else:
        category = "Normal"
        
    city_classifications[name] = category
    print(f"City: {name:<12} | Temp: {temp}°C | Humidity: {hum}% | Rainfall: {rain}mm | Classification: {category}")

# 5. Calculations
num_valid = len(valid_temperatures)
avg_temp = round(sum(valid_temperatures) / num_valid, 2)
max_temp = max(valid_temperatures)
min_temp = min(valid_temperatures)

print("\n--- Temperature Summary Metrics ---")
print(f"Number of valid observations : {num_valid}")
print(f"Average temperature         : {avg_temp}°C")
print(f"Highest temperature         : {max_temp}°C")
print(f"Lowest temperature          : {min_temp}°C")

# 6. Final classification results stored in a dictionary
print("\n--- Final Stored Classifications ---")
print(city_classifications)


# ==============================================================================
# EXERCISE 2: Functions and Climate Risk
# ==============================================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Functions and Climate Risk")
print("=" * 60)

# Function to calculate risk
def calculate_risk(temperature, rainfall):
    if temperature >= 40:
        return "EXTREME"
    elif temperature >= 35 or rainfall < 5:
        return "HIGH"
    elif temperature >= 30 or rainfall < 15:
        return "MODERATE"
    else:
        return "LOW"

# Function to calculate climate stats and return a tuple: (average, minimum, maximum)
def calculate_climate_stats(cities_list):
    temps = [c["temperature"] for c in cities_list if c["temperature"] is not None]
    if not temps:
        return (0, 0, 0)
    avg_t = round(sum(temps) / len(temps), 2)
    min_t = min(temps)
    max_t = max(temps)
    return (avg_t, min_t, max_t)

# 1 & 2. Call calculate_risk for every valid city and display results
print("\n--- City Risk Assessment ---")
valid_cities = []

for city in cities_data:
    if city["temperature"] is None:continue
    
    risk = calculate_risk(city["temperature"], city["rainfall"])
    city_with_risk = city.copy()
    city_with_risk["risk"] = risk
    valid_cities.append(city_with_risk)
    
    print(f"City: {city['city']:<12} | Temperature: {city['temperature']}°C | Risk: {risk}")

# 3. Call summary stats function
avg_stat, min_stat, max_stat = calculate_climate_stats(cities_data)
print(f"\nClimate Stats Tuple (Average, Minimum, Maximum): {(avg_stat, min_stat, max_stat)}")

# 4. Display only cities classified as HIGH or EXTREME
print("\n--- High Risk & Extreme Risk Cities ---")
high_or_extreme = [c for c in valid_cities if c["risk"] in ["HIGH", "EXTREME"]]
for c in high_or_extreme:
    print(f"City: {c['city']:<12} | Risk: {c['risk']} | Temp: {c['temperature']}°C | Rainfall: {c['rainfall']}mm")

# 5. Sort cities from highest to lowest temperature using sorted() and lambda
sorted_cities = sorted(valid_cities, key=lambda c: c["temperature"], reverse=True)

print("\n--- Valid Cities Sorted by Temperature (Highest to Lowest) ---")
for c in sorted_cities:
    print(f"City: {c['city']:<12} | Temperature: {c['temperature']}°C")


# ==============================================================================
# EXERCISE 3 & BONUS: OOP Climate Monitoring System
# ==============================================================================
print("\n" + "=" * 60)
print("EXERCISE 3 & BONUS: OOP Climate Monitoring System")
print("=" * 60)

class ClimateStation:
    def __init__(self, city, temperature, humidity, rainfall):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall = rainfall

    def display_summary(self):
        print(f"Station: {self.city:<12} | Temp: {self.temperature}°C | Humidity: {self.humidity}% | Rainfall: {self.rainfall}mm")

    def calculate_risk(self):
        if self.temperature is None:
            return "UNKNOWN"
        if self.temperature >= 40:
            return "EXTREME"
        elif self.temperature >= 35 or self.rainfall < 5:
            return "HIGH"
        elif self.temperature >= 30 or self.rainfall < 15:
            return "MODERATE"
        else:
            return "LOW"

    def update_temperature(self, new_temperature):
        old_temp = self.temperature
        self.temperature = new_temperature
        print(f"[{self.city}] Temperature updated from {old_temp}°C to {new_temperature}°C")


class SmartClimateStation(ClimateStation):
    def __init__(self, city, temperature, humidity, rainfall, sensor_status="Active"):
        # Inherit attributes from parent class
        super().__init__(city, temperature, humidity, rainfall)
        self.sensor_status = sensor_status

    def check_sensor(self):
        print(f"[{self.city}] Sensor Status: {self.sensor_status}")
        return self.sensor_status

    # Bonus Method: recommendation()
    def recommendation(self):
        risk = self.calculate_risk()
        recommendations = {
            "LOW": "Normal monitoring",
            "MODERATE": "Continue monitoring",
            "HIGH": "Increased monitoring recommended",
            "EXTREME": "Immediate attention required",
            "UNKNOWN": "Sensor check required"
        }
        return recommendations.get(risk, "No specific recommendation")


# Creating at least 5 ClimateStation / SmartClimateStation objects
stations = [
    SmartClimateStation("Damascus", 38.5, 30, 2.0, "Active"),
    SmartClimateStation("Aleppo", 41.2, 25, 0.5, "Active"),
    SmartClimateStation("Homs", 32.0, 45, 12.0, "Maintenance Needed"),
    SmartClimateStation("Latakia", 28.5, 75, 25.0, "Active"),
    SmartClimateStation("Palmyra", 42.0, 15, 1.0, "Active")
]

print("\n--- Initial Stations Summary & Risk Analysis ---")
for station in stations:
    station.display_summary()
    station.check_sensor()
    risk = station.calculate_risk()
    rec = station.recommendation()
    print(f" -> Calculated Risk: {risk} | Recommendation: {rec}")
    print("-" * 50)
    # Demonstrating update_temperature method
print("\n--- Updating Temperature Example ---")
stations[3].update_temperature(31.5) # Updating Latakia temperature
stations[3].display_summary()
print(f" -> New Calculated Risk: {stations[3].calculate_risk()}")
print(f" -> New Recommendation: {stations[3].recommendation()}")