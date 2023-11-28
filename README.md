# Extra Bone Lister for Blender
When executed within Blender, this script will list the bones for the Armature that are not mentioned by name in the Vertex Groups of the meshes and do not have any children.

## Usage
 When executed within Blender, this script will list the bones for the Armature that are not mentioned by name in the Vertex Groups of the meshes and do not have any children.

## Install
Copy & paste this script into the Python Console within Blender and run.

## Usage
- Use the list printed in the Python Console as a reference to know which bones to select and delete in the Outliner view.
- Multiple passes may be needed to delete all bones as this script only prints the names of bones without any children.
- So... run script, use printed bone names as reference to select and delete them in the Outliner. Then repeat these same steps until no bones are printed.
- If no bones are printed, then every bone in the Armature is in a Vertex Group.

## Considerations
- For this to work correctly, the Vertex Groups must be named the same as the bone they reference.
