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
    blueprint = input("Blueprint String: ")
    decoded = decode(blueprint)

    print(decoded)