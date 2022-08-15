This folder contains the necessary python files to run the frontend part of the project.

- /Assets/Scripts/RigBone.cs: a class that provides methods and variables to allow animation on rig model.
- /Assets/Scripts/RigControl.cs: Code to allow animation on our rig model. Uses dictionary from the RotationData
- /Assets/Scripts/SceneController.cs: Code to switch scenes
- /Assets/Scripts/UpdateREBAScore.cs: Small script to update text in textField for REBA score.
- /Assets/UtilityClasses/JointData.cs: Class that holds deserialized JSON data from backend in Python.
- /Assets/UtilityClasses/REBA.cs: Static class that is used to colour our rig model, based on jointData collected.
- /Assets/UtilityClasses/RotationData.cs: Rotational data captured from jointData serialized; static class that provides properties/variables to move the rigModel.
