treasures = [
    {
       "name": "Gold",
       "location": "cave",
       "value": 500 
    },
    {
        "name":"Diamond",
        "location": "Jungle",
        "value": 1000
    },
    {
        "name": "Silver",
        "location": "Beach",
        "value": 300
    },
    {
        "name": "Emerald",
        "location": "Lighthouse",
        "value": 800
    }
]
print(treasures[0]["name"])
print(treasures[1]["location"])
print(treasures[2]["value"])
print(treasures[3]["name"])
print(treasures[0]["value"])
print(treasures[3]["location"])

for item in treasures:
    print(f"{item['name']} is worth {item['value']}")

treasures[0]["value"] = 700
treasures[2]["location"] = "Cave"
treasures[3]["value"] = 1200

for item in treasures:
    if item["name"] == "Diamond":
        print("Diamond discovered!")
        break
else:
     print("Diamond not found!")

total = 0

for item in treasures:
    total += item["value"]
print(f"Total Treasure value:{total}")    

