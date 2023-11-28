# Usage: 
# When executed within Blender, this script will list the bones for the Armature that are not mentioned by name in the Vertex Groups of the meshes and do not have any children.

# Install:
# Copy & paste this script into the Python Console within Blender and run.

# Usage:
# Use the list printed in the Python Console as a reference to know which bones to select and delete in the Outliner view.
# Multiple passes may be needed to delete all bones as this script only prints the names of bones without any children.
# So... run script, use printed bone names as reference to select and delete them in the Outliner. Then repeat these same steps until no bones are printed.
# If no bones are printed, then every bone in the Armature is in a Vertex Group.

# Considerations
# For this to work correctly, the Vertex Groups must be named the same as the bone they reference.

import bpy # Included for viewing/editing the script in an IDE only. DO NOT copy/paste this line into the Python Console in Blender.

bones = []
vertexGroups = []

for obj in bpy.data.objects:
    if obj.type == "ARMATURE":
        armature = obj.data
        for child in obj.children:
            if child.type == "MESH":
                for vertexGroup in child.vertex_groups:
                    if vertexGroup.name not in vertexGroups:
                        vertexGroups.append(vertexGroup.name)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        for bone in armature.edit_bones:
            if bone.name not in vertexGroups:
                if bone.name != "[Root]":
                    if len(bone.children) < 1:
                        print(bone.name)