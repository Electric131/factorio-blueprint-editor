from blueprint_editing import decode, encode
from json import load, loads

def colorFromString(config: dict, color: str):
    if trainColor == "":
        color = config["default_color"]
    else:
        color = trainColor.replace(" ", "").split(",")
    return color

def generate_train(config: dict, itemName: str, color: list):
    if itemName in config["fluid_types"]:
        itemType = "fluid"
        wagonType = "fluid"
    else:
        itemType = "item"
        wagonType = "cargo"

    itemSymbol = f"[{itemType}={itemName}]"
    wagonSymbol = f"[item={wagonType}-wagon]"
    formattedItem = " ".join(itemName.split("-")).title()

    schedule = str(config["schedule_format"])
    label = config["blueprint_label"]
    replace = {"<item_name>": itemName, "<item_symbol>": itemSymbol, "<wagon_type>": wagonType, "<item_type>": itemType, "<wagon_symbol>": wagonSymbol, "<item_titled>": formattedItem}
    for replaceA, replaceB in replace.items():
        schedule = schedule.replace(replaceA, replaceB)
        label = label.replace(replaceA, replaceB)

    schedule = loads(schedule.replace("'", '"'))

    entityCount = 0
    entities = []

    filterList = [{"index": i + 1, "name": itemName} for i in range(40)]

    for i in range(config["locomotive_count"]):
        entityCount += 1
        entityData = {'entity_number': entityCount, 'name': 'locomotive', 'position': {'x': 0, 'y': ((entityCount - 1) * 7)}, 'orientation': 0, 'color': {'r': color[0]/255, 'g': color[1]/255, 'b': color[2]/255, 'a': 0.5}, 'items': {config["fuel"]: config["fuel_amount"]}}
        entities.append(entityData)

    for i in range(config["wagon_count"]):
        entityCount += 1
        entityData = {'entity_number': entityCount, 'name': f'{wagonType}-wagon', 'position': {'x': 0, 'y': ((entityCount - 1) * 7)}, 'orientation': 0, "inventory": {"filters": filterList}}
        entities.append(entityData)

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
        ],
        "entities": entities,
        "schedules": [
            {
                "locomotives": [i + 1 for i in range(config["locomotive_count"])],
                "schedule": schedule
            }
        ],
        "item": "blueprint",
        "label": label,
        "version": config["game-version"]
    }

    blueprint = {"blueprint": blueprintData}

    encoded = encode(blueprint)

    with open("message.txt", "w") as f:
        f.write(encoded)
    
    return (f"'{itemName}' is type {itemType} and is stored in a {wagonType} wagon\n\n", encoded)

if __name__ == "__main__":
    itemName = input("Train Item: ")
    trainColor = input("Train Color(optional): ")

    with open("config.json") as f:
        config = load(f)

    generate_train(config, itemName, colorFromString(config, trainColor))
    print("Completed")