import socket
import sys
import time

from zss_cmd_pb2 import Robots_Command, Robot_Command

class Action(object):
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.command_address = ('localhost', 50001)

	def sendCommand(self, id=0, vx=0, vy=0, vw=0, kick=False, power=0, dribble_spin=False):
		commands = Robots_Command()
		command = commands.command.add()
		#command.robot_id = 0
		command.robot_id = id
		command.velocity_x = vx
		command.velocity_y = vy
		command.velocity_r = vw
		command.kick = False
		command.power = 0
		command.dribbler_spin = False
		#print(type(command))
		self.sock.sendto(commands.SerializeToString(), self.command_address)

if __name__ == '__main__':
	
	my_command1 = {
		"id" : 1,
		"vx" : 0,
		"vy":  0,
		"vw" : 7
	}

	my_command2 = {
		"id" : 1,
		"vx" : 0,
		"vy":  0,
		"vw" : 0

	}

	action_module = Action()

	while True:
		action_module.sendCommand(id  = my_command1['id'], vx = my_command1["vx"], vy=my_command1["vy"], vw=my_command1["vw"])
		time.sleep(0.89)
		action_module.sendCommand(id = my_command2['id'], vx=my_command2["vx"], vy = my_command2["vy"], vw=my_command2["vw"])
		time.sleep(1)
