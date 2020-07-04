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
		# debugger.draw_circle(vision.my_yellow_robot.x, vision.my_yellow_robot.y)
		# time.sleep(0.02)
	
		print(vision.my_ball.x)