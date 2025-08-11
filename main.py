import os
import json
from bitflags import BitFlags
# from mwcleric import WikiggClient, AuthCredentials


def main():
    # credentials = AuthCredentials(user_file='me')
    # site = WikiggClient('aneurism', credentials=credentials)

    item_data_path = ""
    if os.name == "nt":
        item_data_path = os.path.expandvars(
            r"%APPDATA%/../LocalLow/Vellocet/ANEURISM IV/item_data.json"
        )
    elif os.name == "posix":
        item_data_path = os.path.expandvars(
            r"$HOME/.config/unity3d/Vellocet/ANEURISM IV/item_data.json"
        )

    if not os.path.isfile(item_data_path):
        print("Couldn't find item_data.json. Exiting.")
        return

    with open(item_data_path, "r") as file:
        json_monolith = json.load(file)
        WeaponData = json_monolith["WeaponData"]
        WeaponData.pop("Null", None)
        Ammo = json_monolith["Ammo"]
        Ammo.pop("Null", None)
        TagsWeapon = json_monolith["TagsWeapon"]
        TagsWeapon.pop("-1", None)
        FiringType = json_monolith["FiringType"]
        FiringType.pop("-1", None)
        WType = json_monolith["Type"]
        WType.pop("-1", None)
        Attributes = json_monolith["Attributes"]
        Attributes.pop("-1", None)
        Consumable = json_monolith["Consumable"]
        Consumable.pop("Null", None)
        EntityData = json_monolith["EntityData"]
        EntityData.pop("Null", None)
        Fate = json_monolith["Fate"]
        Fate.pop("Null", None)
        InstanceIDs = json_monolith["InstanceIDs"]
        del json_monolith

    NumTagsWeapon = {}  # Bitflag, Attributes and FiringType and WType are not bitflags
    for Tag in TagsWeapon:
        NumTagsWeapon[int(Tag) - 1] = TagsWeapon[Tag]

    class WeaponTagsFlags(BitFlags):
        options = NumTagsWeapon

    for Weapon in WeaponData:
        print("- " + Weapon)
        WeaponData[Weapon]["WeaponTags"] = WeaponTagsFlags(
            WeaponData[Weapon]["WeaponTags"]
        ).get_flags()
        WeaponData[Weapon]["FireType"] = FiringType[str(WeaponData[Weapon]["FireType"])]

        newAmmoEntities = []
        for ammoEntity in WeaponData[Weapon]["ammoEntities"]:
            newAmmoEntities.append(InstanceIDs[str(ammoEntity["instanceID"])])
        WeaponData[Weapon]["ammoEntities"] = newAmmoEntities
        del newAmmoEntities

        WeaponData[Weapon]["Type"] = WType[str(WeaponData[Weapon]["Type"])]
        WeaponData[Weapon].pop("StartFireSounds", None)
        WeaponData[Weapon].pop("StopFireSounds", None)
        WeaponData[Weapon].pop("LoopSounds", None)
        WeaponData[Weapon].pop("FireSounds", None)
        WeaponData[Weapon].pop("ReloadSounds", None)
        WeaponData[Weapon].pop("ReloadFinishSounds", None)
        WeaponData[Weapon].pop("EmptySounds", None)
        WeaponData[Weapon]["AlternateWeaponEntityData"] = InstanceIDs[
            str(WeaponData[Weapon]["AlternateWeaponEntityData"]["instanceID"])
        ]
        WeaponData[Weapon].pop("WeaponModel", None)
        WeaponData[Weapon].pop("weaponPositioning", None)
        WeaponData[Weapon].pop("bulletOverrideHoleGo", None)
        WeaponData[Weapon].pop("AnimationSet", None)
        WeaponData[Weapon].pop("bulletOverrideHoleGo", None)
        WeaponData[Weapon].pop("HasIdlePose", None)


# https://github.com/RheingoldRiver/amberisle-python

# f = open('data.csv', mode='r', newline='')
# # Load the CSV data
# reader = csv.DictReader(f)

# WIKITEXT = """{{{{Clothing infobox
# |uid={}
# |display={}
# |craft slots={}
# }}}}"""

# CRAFT_SLOT_TEXT = """{{{{CraftSlot|id={} |amount={} }}}}"""

# # Example of reusing the reader
# for row in reader:
#     craft_slots = []
#     for i in range(5):  # 0, 1, 2, 3, 4
#         j = str(i + 1)  # 1, 2, 3, 4, 5
#         idname = 'Craft Slot ' + j + ' ID'  # Craft Slot 1 ID
#         amountname = 'Craft Slot ' + j + ' Amount'  # Craft Slot 1 Amount
#         if row[idname] != '':
#             craft_slots.append(  # lua: craft_slots[#craft_slots+1] =
#                 CRAFT_SLOT_TEXT.format(row[idname], row[amountname])
#             )

#     text = WIKITEXT.format(
#         row['UID'],
#         row['-Friendly Name-'],
#         ''.join(craft_slots)
#     )
#     page_name = row['-Friendly Name-']
#     print('Saving page ' + page_name + '...')
#     site.save_title(page_name, text, summary='Automatic page creation from mwcleric :)')

# # cleanup
# f.close()


if __name__ == "__main__":
    main()
