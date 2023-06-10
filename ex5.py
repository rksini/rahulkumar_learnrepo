import json


ex5 = {
    "id": "0005",
    "type": "donut",
    "name": "Old Fashioned",
    "ppu": 0.55,
    "batters": {
        "batter": [
            {"id": "1001", "type": "Regular"},
            {"id": "1002", "type": "Chocolate"},
        ]
    },
    "topping": [
        {"id": "5001", "type": "None"},
        {"id": "5002", "type": "Glazed"},
        {"id": "5003", "type": "Chocolate"},
        {"id": "5004", "type": "Maple"}
    ]
}

with open("ex5.json", "w") as file:
    json.dump(ex5, file)


with open("ex5.json", "r") as file:
    ex5 = json.load(file)


new_batter = {"id": "1005", "type": "Coffee"}
ex5["batters"]["batter"].append(new_batter)

with open("ex5.json", "w") as file:
    json.dump(ex5, file)
