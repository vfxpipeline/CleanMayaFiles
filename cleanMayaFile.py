"""
Clean Maya File
How to delete old unwanted Missing Maya Plug ins?
"""
import maya.cmds as cmds

# delete unknown nodes
cmds.delete(cmds.ls(type="unknown"))

# delete unknown plugins
plugins_list = cmds.unknownPlugin(q=True, l=True)
if plugins_list:
    for plugin in plugins_list:
        print(plugin)
        cmds.unknownPlugin(plugin, r=True)
