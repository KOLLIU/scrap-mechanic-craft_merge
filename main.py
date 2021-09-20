from json_utils import read_json, write_json


def merge_crafts(destination: str = "",
                 path: str = "",
                 file: str = ""):
    if destination == "":
        destination = "F:/steam/steamapps/common/Scrap Mechanic/Survival/CraftingRecipes/"
    if path == "":
        path = "F:/steam/steamapps/common/Scrap Mechanic/Merge_crafts/"
    if file == "":
        file = "craftbot.json"

    old = read_json(destination + file)
    new = read_json(path + file)

    print(len(old), len(new))

    keys = [item["itemId"] for item in old]
    for i, item in enumerate(new):
        if item["itemId"] not in keys:
            old.append(item)

    print(len(old), len(new))

    write_json(file_name=destination + file[:-5:] + "2" + file[-5::], obj=old)


if __name__ == '__main__':
    merge_crafts(file="hideout.json")
