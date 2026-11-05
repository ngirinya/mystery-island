inventory = [
    {
        "name": "Rope",
        "description": "Used for crossing bridges",
        "quantity": 2
    },
    {
        "name": "Lantern",
        "description": "Used for exploring dark places",
        "quantity": 1
    },
    {
        "name" : "Key",
        "description": "Used for opening locked doors",
        "quantity": 3
    }
]
print(inventory[0]["name"])
print(inventory[1]["quantity"])
print(inventory[2]["description"])
print(inventory[2]["name"])

for item in inventory:
    print(f"{item['name']}:{item['quantity']}")

inventory[0]["quantity"] = 4 
inventory[1]["quantity"] = 3
inventory.append({
    "name": "Map",
    "description": "Shows island locations",
    "quantity": 1
})
print(inventory[0]["quantity"])
print(inventory[1]["quantity"])
print(inventory[3]["description"])
print(inventory[3]["quantity"])

for item in inventory:
    if item["name"] == "Key":
        print("Key Found")
        break
else:
    print("Key Not Found")        