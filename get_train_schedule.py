from blueprint_editing import decode

blueprint = input("Train Blueprint String: ")

json = decode(blueprint)

trainInfo = json["blueprint"]["schedules"][0]["schedule"]

print(trainInfo)