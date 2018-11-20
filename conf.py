data = {
    "rows":7,
    "cols":7,
    "multiplier":120,#size of each box
    "speed":6, #speed of box to box movement
    "icon_loc":"assets/atoms_c.ico",
    "img_loc":"assets/atoms.png",
    "title":"chainreaction2d",
    "fps":75,
    "rotation_speed":(7,9) #range of values for speed of rotation
}

#add how many players you want in this format
players = [# added random colors
           {"name":"red","color":(255,0,0)},
           {"name":"blue","color":(0,0,255)},
           {"name":"green","color":(0,255,0)},
           {"name":"yellow","color":(255,255,0)},
           #{"name":"orange","color":(255,165,0)},
           #{"name":"turquoise","color":(64,224,208)}
          ]
data["players"] =players
