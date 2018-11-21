# Classes  

## Board

### Data Variables:
<br />
**data:** &nbsp;*holds all the data about the game*   
has duplicates for easy access namely   
`self.rows:`  
`self.cols`  
`self.speed`  
`self.multiplier`    
`self.img_loc`  
`self.rotation_speed`  

**derived from data**  
`self.total_box_width`  *area of grid*    
`self.total_box_height`   
`self.total_width` *area of full window*  
`self.total_height`

### Dynamic containers:
<br />
`self.animations` &nbsp; *holds all animations->* &nbsp; *set type*  
`self.remove_cycle` &nbsp; *holds all animations to be removed ->* &nbsp; *set type*  
`self.box_list` &nbsp; *holds all the boxes ->* &nbsp; *type list*  
`self.players` &nbsp; *holds all the players ->* &nbsp; *type list*  
`self.alive_players` &nbsp; *holds all the alive players ->* &nbsp; *type list*

### Control Variables:
<br />
`self.running` &nbsp; *whether any animation is running ->* &nbsp;  *type bool*  
`self.main_running` &nbsp; *whether the main game is running ->* &nbsp; *type bool*  
`self.check_end` &nbsp; *when user event has occured and chance has to cycle ->* &nbsp; *type bool*

`self.animation_owners` &nbsp; *holds owners under animation ->*&nbsp; *type list*  
*required because a owner might not be in any boxes and game should not declare it not alive*  

`self.state` &nbsp; *state of game --*   
*1 for playing game  <br />2 for in the end screen*

`self.count` &nbsp; *hold current total no of turns ->* &nbsp; *type bool*    
`self.end_setup` &nbsp; *if end_game has been setup ->* &nbsp; *type bool*  

### Others
<br />
`self.end_game` &nbsp; *holds all methods for end screen ->* &nbsp; *type class*  
`self.current` &nbsp; *the turn of which player ->* &nbsp; *type class*  
