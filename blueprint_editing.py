import zlib, base64, json

def decode(blueprintString: str):
    blueprintBase64 = base64.b64decode(blueprintString[1:].encode("utf-8"))

    blueprintJSON = str(zlib.decompress(blueprintBase64).decode("utf-8"))
    return json.loads(blueprintJSON)

def encode(blueprintJSON):
    blueprintCompress = zlib.compress(json.dumps(blueprintJSON).encode("utf-8"), 9)
    blueprintString = "0" + base64.b64encode(blueprintCompress).decode("utf-8")
    return blueprintString

if __name__ == '__main__':
    # blueprint = input("Blueprint String: ")
    # decoded = decode(blueprint)

    # print(decoded)

    # print(list(decoded["blueprint"].keys()))

    data = {'blueprint': {'icons': [{'signal': {'type': 'item', 'name': 'locomotive'}, 'index': 1}, {'signal': {'type': 'item', 'name': 'copper-ore'}, 'index': 2}], 'entities': [{'entity_number': 1, 'name': 'locomotive', 'position': {'x': 0, 'y': 0}, 'orientation': 0, 'color': {'r': 0.843137264251709, 'g': 0.2078431397676468, 'b': 0.07058823853731155, 'a': 0.5}, 'items': {'nuclear-fuel': 3}}, {'entity_number': 2, 'name': 'cargo-wagon', 'position': {'x': 0, 'y': 6}, 'orientation': 0, 'inventory': {'filters': [{'index': 1, 'name': 'copper-ore'}, {'index': 2, 'name': 'copper-ore'}, {'index': 3, 'name': 'copper-ore'}, {'index': 4, 'name': 'copper-ore'}, {'index': 5, 'name': 'copper-ore'}, {'index': 6, 'name': 'copper-ore'}, {'index': 7, 'name': 'copper-ore'}, {'index': 8, 'name': 'copper-ore'}, {'index': 9, 'name': 'copper-ore'}, {'index': 10, 'name': 'copper-ore'}, {'index': 11, 'name': 'copper-ore'}, {'index': 12, 'name': 'copper-ore'}, {'index': 13, 'name': 'copper-ore'}, {'index': 14, 'name': 'copper-ore'}, {'index': 15, 'name': 'copper-ore'}, {'index': 16, 'name': 'copper-ore'}, {'index': 17, 'name': 'copper-ore'}, {'index': 18, 'name': 'copper-ore'}, {'index': 19, 'name': 'copper-ore'}, {'index': 20, 'name': 'copper-ore'}, {'index': 21, 'name': 'copper-ore'}, {'index': 22, 'name': 'copper-ore'}, {'index': 23, 'name': 'copper-ore'}, {'index': 24, 'name': 'copper-ore'}, {'index': 25, 'name': 'copper-ore'}, {'index': 26, 'name': 'copper-ore'}, {'index': 27, 'name': 'copper-ore'}, {'index': 28, 'name': 'copper-ore'}, {'index': 29, 'name': 'copper-ore'}, {'index': 30, 'name': 'copper-ore'}, {'index': 31, 'name': 'copper-ore'}, {'index': 32, 'name': 'copper-ore'}, {'index': 33, 'name': 'copper-ore'}, {'index': 34, 'name': 'copper-ore'}, {'index': 35, 'name': 'copper-ore'}, {'index': 36, 'name': 'copper-ore'}, {'index': 37, 'name': 'copper-ore'}, {'index': 38, 'name': 'copper-ore'}, {'index': 39, 'name': 'copper-ore'}, {'index': 40, 'name': 'copper-ore'}]}}], 'schedules': [{'locomotives': [1], 'schedule': [{'station': '[entity=tile-ghost]', 'wait_conditions': [{'compare_type': 'or', 'type': 'inactivity', 'ticks': 60}]}, 
{'station': '[virtual-signal=signal-L][item=copper-ore]', 'wait_conditions': [{'compare_type': 'or', 'type': 'full'}, {'compare_type': 'or', 'type': 'item_count', 'condition': {'first_signal': {'type': 'item', 'name': 
'copper-ore'}, 'constant': 0, 'comparator': '>'}}, {'compare_type': 'and', 'type': 'time', 'ticks': 18000}]}, {'station': '[entity=tile-ghost]'}, {'station': '[virtual-signal=signal-U][item=copper-ore]', 'wait_conditions': [{'compare_type': 'or', 'type': 'empty'}]}]}], 'item': 'blueprint', 'label': '[item=locomotive][item=copper-ore][item=cargo-wagon] Copper Ore', 'version': 281479275151360}}

    print(encode(data))