using BepInEx;
using BepInEx.Logging;
using BepInEx.Unity.IL2CPP;
using UnityEngine;
using UnityEngine.SceneManagement;
using Newtonsoft.Json;

namespace data_dumper
{

	public class DataDumper_Component : MonoBehaviour 
	{
		void Update()
		{
			Scene uiScene = SceneManager.GetSceneByName("UserInterface");
			if (uiScene.loadingState == Scene.LoadingState.Loaded)
			{
				string Path = Application.persistentDataPath + "/item_data.json";


				string myData = "";
				myData += @"{
				""WeaponData"": {
				";

				Entities.Items.WeaponData[] objs = Resources.FindObjectsOfTypeAll<Entities.Items.WeaponData>();

				foreach (var go in objs)
				{
					myData += "	\"" + go.name + "\":";
					myData += JsonUtility.ToJson(go);
					myData += ",\n";
				}
				myData += "	\"Null\":{}";

				myData += "\n},\n";


				myData += @"
				""Ammo"": {
				";

				Entities.Items.Ammo[] ammoObjs = Resources.FindObjectsOfTypeAll<Entities.Items.Ammo>();

				foreach (var go in ammoObjs)
				{
					myData += "	\"" + go.name + "\":";
					myData += JsonUtility.ToJson(go);
					myData += ",\n";
				}
				myData += "	\"Null\":{}";

				myData += "\n},\n";


				myData += @"
				""TagsWeapon"": {
				";


				int tag = 0;
				foreach (var go in Enum.GetValues(typeof(Entities.Shared.TagsWeapon)).Cast<Entities.Shared.TagsWeapon>())
				{
					myData += "	\"" + tag + "\":\"" + go + "\"";
					myData += ",\n";
					tag++;
				}
				myData += "	\"-1\":\"Null\"";
				myData += "\n},\n";



				myData += @"
				""FiringType"": {
				";


				int fir = 0;
				foreach (var go in Enum.GetValues(typeof(Entities.Items.WeaponData.FiringType)).Cast<Entities.Items.WeaponData.FiringType>())
				{
					myData += "	\"" + fir + "\":\"" + go + "\"";
					myData += ",\n";
					fir++;
				}
				myData += "	\"-1\":\"Null\"";
				myData += "\n},\n";



				myData += @"
				""Attributes"": {
				";


				int att = 0;
				foreach (var go in Enum.GetValues(typeof(Entities.Player.PlayerAttributes.Attributes)).Cast<Entities.Player.PlayerAttributes.Attributes>())
				{
					myData += "	\"" + att + "\":\"" + go + "\"";
					myData += ",\n";
					att++;
				}
				myData += "	\"-1\":\"Null\"";
				myData += "\n},\n";



				myData += @"
				""Consumable"": {
				";

				Entities.Items.Consumable[] objsb = Resources.FindObjectsOfTypeAll<Entities.Items.Consumable>();

				foreach (var go in objsb)
				{
					myData += "	\"" + go.name + "\":";
					myData += JsonUtility.ToJson(go);
					myData += ",\n";
				}
				myData += "	\"Null\":{}";
				myData += "\n},\n";



				myData += @"
				""EntityData"": {
				";


				Entities.Shared.EntityData[] objsa = Resources.FindObjectsOfTypeAll<Entities.Shared.EntityData>();

				foreach (var go in objsa)
				{
					myData += "	\"" + go.name + "\":";
					myData += JsonUtility.ToJson(go);
					myData += ",\n";
				}
				myData += "	\"Null\":{}";
				myData += "\n},\n";



				myData += @"
				""Fate"": {
				";

				Entities.Player.Fate[] objsd = Resources.FindObjectsOfTypeAll<Entities.Player.Fate>();

				foreach (var go in objsd)
				{
					myData += "	\"" + go.name + "\":";
					myData += JsonUtility.ToJson(go);
					myData += ",\n";
				}
				myData += "	\"Null\":{}";
				myData += "\n},\n";



				myData += @"
				""InstanceIDs"": {
				";

				foreach (var go in objsa)
				{
					myData += "	\"" + go.GetInstanceID() + "\":\"" + go.name + "\"";
					myData += ",\n";
				}

				foreach (var go in objsd)
				{
					myData += "	\"" + go.GetInstanceID() + "\":\"" + go.name + "\"";
					myData += ",\n";
				}
				myData += "	\"0\":\"Null\"";

				myData += "\n}";

				myData += "\n}";

				var des = JsonConvert.DeserializeObject(myData);
				File.WriteAllText(Path, JsonConvert.SerializeObject(des, Formatting.Indented));

				Application.Quit();
			}
		}
	}

	[BepInPlugin("data_dumper", "Data Dumper", "0.0.1")]
	public class DataDumper : BasePlugin
	{
		internal static new ManualLogSource Log;

		public override void Load()
		{
			Log = base.Log;

			AddComponent<DataDumper_Component>();

			Log.LogInfo($"Plugin data_dumper loaded successfully.");
		}
	}
}