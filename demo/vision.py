import sys
import socket
import threading

from vision_detection_pb2 import Vision_DetectionFrame, Vision_DetectionRobot, Vision_DetectionBall

class Vision(object):
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.vision_address = '127.0.0.1'
		self.vision_port = 23333
		self.sock.bind((self.vision_address, self.vision_port))
		self.sock.settimeout(1.0)
		self.vision_thread = threading.Thread(target=self.receive_vision)
		self.vision_thread.start()
		self.vision_frame = Vision_DetectionFrame()

		#self.my_robot = Robot()
		self.robots_blue = dict()
		self.robots_yellow = dict()
		self.ball = Vision_DetectionBall()
		self.my_ball = Ball()

	def receive_vision(self):
		while True:
			try:
				data, server = self.sock.recvfrom(4096)
				# print('received message from', server)
				self.vision_frame.ParseFromString(data)
				self.parse_vision()
			except socket.timeout:
				print('VISION TIMED OUT')
 
	def parse_vision(self):
		for robot_blue in self.vision_frame.robots_blue:
			# print('Robot Blue {} pos: {} {}'.format(robot_blue.robot_id, robot_blue.x, robot_blue.y))
				self.robots_blue[robot_blue.robot_id] = robot_blue


		for robot_yellow in self.vision_frame.robots_yellow:
			# print('Robot Yellow {} pos: {} {}'.format(robot_yellow.robot_id, robot_yellow.x, robot_yellow.y))
				self.robots_yellow[robot_yellow.robot_id] = robot_yellow
	

		self.ball = self.vision_frame.balls
		while(self.ball.valid):
			self.my_ball.x = self.ball.x
			self.my_ball.y = self.ball.y
			break
			






class Ball(object):
	def __init__(self,  x=0, y=0, vel_x=0, vel_y=0):
		self.x = x
		self.y = y
		self.vel_x = vel_x
		self.vel_y = vel_y
    		

    		


if __name__ == '__main__':
	vision_module = Vision()
	print(vision_module.robots_yellow.keys())
