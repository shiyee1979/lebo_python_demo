import socket
import sys
import time

from zss_debug_pb2 import Debug_Msgs, Debug_Msg, Debug_Arc

class Debugger(object):
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.debug_address = ('localhost', 20001)

	def draw_circle(self, x, y):
		package = Debug_Msgs()
		msg = package.msgs.add()
		msg.type = Debug_Msg.ARC
		msg.color = Debug_Msg.WHITE
		arc = msg.arc
		radius = 300
		arc.rectangle.point1.x = x - radius
		arc.rectangle.point1.y = y - radius
		arc.rectangle.point2.x = x + radius
		arc.rectangle.point2.y = y + radius
		arc.start = 0
		arc.end = 360
		arc.FILL = True
		self.sock.sendto(package.SerializeToString(), self.debug_address)
	
	def draw_line(self, x_start=0,  y_start=0, x_end=0, y_end=0):
		package = Debug_Msgs()
		msg = package.msgs.add()
		msg.type = Debug_Msg.LINE
		msg.color = Debug_Msg.RED
		line = msg.line
		p_start = line.start
		p_end = line.end
		p_start.x = x_start
		p_start.y = y_start
		p_end.x = x_end
		p_end.y = y_end
		line.FORWARD = True
		line.BACK = False
		self.sock.sendto(package.SerializeToString(), self.debug_address)


	def robot_msg(self, x=0, y=0, orientate=0):
		package = Debug_Msgs()
		msg = package.msgs.add()
		msg.type = Debug_Msg.ROBOT
		msg.color = Debug_Msg.RED
		robot = msg.robot
		point = robot.pos
		point.x = x
		point.y = y
		robot.dir = orientate
		self.sock.sendto(package.SerializeToString(), self.debug_address)
		
if __name__ == '__main__':
	debugger = Debugger()
	while True:
		debugger.draw_circle(x=100, y=200)
		time.sleep(0.02)
