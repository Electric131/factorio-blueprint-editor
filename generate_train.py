from blueprint_editing import decode, encode
from json import load

itemName = input("Train Item: ")
trainColor = input("Train Color(optional): ")

with open("config.json") as f:
    config = load(f)

if trainColor == "":
    color = config["default_color"]
else:
    color = trainColor.replace(" ", "").split(",")

if itemName in config["fluid_types"]:
    itemType = "fluid"
    wagonType = "fluid"
else:
    itemType = "item"
    wagonType = "cargo"

itemSymbol = f"[{itemType}={itemName}]"

print(f"Type Recognized: '{itemName}' is type {itemType} and is stored in a {wagonType} wagon")

schedule = str(config["schedule_format"])
replace = {"<item_name>": itemName, "<item_symbol>": itemSymbol, "<wagon_type>": wagonType}
for replaceA, replaceB in replace.items():
    schedule = schedule.replace(replaceA, replaceB)

entityCount = 0
entities = []

filterList = [{"index": i + 1, "name": itemName} for i in range(40)]

for i in range(config["locomotive_count"]):
    entityCount += 1
    entityData = {'entity_number': entityCount, 'name': 'locomotive', 'position': {'x': 0, 'y': ((entityCount - 1) * 6)}, 'orientation': 0, 'color': {'r': color[0]/255, 'g': color[1]/255, 'b': color[2]/255, 'a': 0.5}, 'items': {config["fuel"]: config["fuel_amount"]}}
    entities.append(entityData)

for i in range(config["wagon_count"]):
    entityCount += 1
    entityData = {'entity_number': entityCount, 'name': f'{wagonType}-wagon', 'position': {'x': 0, 'y': ((entityCount - 1) * 6)}, 'orientation': 0, "inventory": {"filters": filterList}}
    entities.append(entityData)

print(entities)

blueprintData = {
    "icons":[
        {
            "signal": {
                "type": "item",
                "name": "locomotive"
            },
            "index": 1
        },
        {
            "signal":
            {
                "type": itemType,
                "name": itemName
            },
            "index": 2
        }
    ]
}