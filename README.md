# ANEURISM IV Data Dumper

This plugin is meant primarily for developers to dump data that is useful to the wiki, for wiki data automation

Once the UI scene is loaded, it will gather game object data and export it to `AppData\LocalLow\Vellocet\ANEURISM IV\item_data.json` then it force closes the game

The data exported, at the time of writing, includes:
- Weapon data (firerate, recoil, damage, damage type, ammo count, ammo types)
- Consumable data (effects, attributes, exceptions like sus meat by scum)
- Entity data (weight, contraband, inventoriable, soulbound)
- Instance IDs (used in some places like ammo or consumable fate exceptions)
- Fates (anamnecyte cost, karma req, loadout, health, speed)
- Enums
  - Attributes (for consumables)
  - TagsWeapon (damage type)
  - FiringType (single or full auto)
