from vision import Vision
from action import Action
from debug import Debugger
import time

if __name__ == '__main__':
	vision = Vision()
	action = Action()
	debugger = Debugger()

	my_command1 = {
	"id" : 0,
	"vx" : 300,
	"vy":  0,
	"vw" : 0
	}
	my_command2 = {
	"id" : 1,
	"vx" : 0,
	"vy":  0,
	"vw" : 1.25
	}


	while True:
		# Do something(path planning)
		# action.sendCommand(id = my_command1["id"],vx=my_command1["vx"], vy=my_command1['vy'], vw=my_command1["vw"])
		#debugger.draw_line(vision.robots_yellow[0].x, vision.robots_yellow[0].y, vision.my_ball.x, vision.my_ball.y)
		for val in vision.robots_blue.keys():
    			#print(vision.robots_blue[val].y)
			if val == 0:
				#action.sendCommand(id = my_command1["id"],vx=my_command1["vx"], vy=my_command1['vy'], vw=my_command1["vw"])
				#time.sleep(1)
				#print(vision.robots_yellow.keys())
				#debugger.robot_msg(vision.robots_blue[val].x, vision.robots_blue[val].y)
				debugger.draw_circle(vision.robots_blue[val].x, vision.robots_blue[val].y)
				#print(val)
				pass					
			if val == 1:
    				#action.sendCommand(id = my_command2["id"],vx=my_command1["vx"], vy=my_command2['vy'], vw=my_command2["vw"])
				debugger.draw_line(vision.robots_blue[val].x, vision.robots_blue[val].y, vision.my_ball.x, vision.my_ball.y)
				pass
		# time.sleep(0.02)
		#debugger.draw_line(120, 120, 0, 0)
	
	