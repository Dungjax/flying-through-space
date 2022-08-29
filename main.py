from pygame import init,event,FINGERDOWN,FINGERMOTION,FINGERUP
init()
from setting import *
from object import Object
from camera import camera_group
from random import randint
from math import dist

class Game:
	def __init__(self):
		#touch
		self.fingerx=0
		self.fingery=0
		
		self.fingerx_d=0
		self.fingery_d=0
		
		self.slidex=0
		self.slidex_up=0
		self.slidey=0
		self.slidey_up=0
		#aeteroid setup
		self.aeteroid_respawn_range=max(Width,Height)
		self.aeteroid_collision_range=200
	def collision(self):
		for aeteroid in aeteroid_group:
			for bullet in bullet_group:
				if dist((aeteroid.pos.x,aeteroid.pos.y),(bullet.pos.x,bullet.pos.y))<self.aeteroid_collision_range and aeteroid.pos.z-bullet.pos.z<0.2:
					aeteroid.kill()
					bullet.kill()
					break
	
	def draw(self):
		camera_group.z_draw()
		
	def update(self):
		
		aeteroid=Object(aeteroid_imgs[randint(0,len(aeteroid_imgs)-1)],randint(50,400),randint(-self.aeteroid_respawn_range,self.aeteroid_respawn_range),randint(-self.aeteroid_respawn_range,self.aeteroid_respawn_range),10,-randint(1,2)/10)
		camera_group.add(aeteroid)
		
		aeteroid_group.add(aeteroid)
		
		camera_group.update()
		
		self.collision()
	
	def loop(self):
		while 1:
			clock.tick(60)
			for ev in event.get():
				if ev.type==FINGERDOWN:
					if ev.x*Width<H_Width:
						self.fingerx_d=ev.x*Width
						self.fingery_d=ev.y*Height
					else:
						bullet=Object(bullets_img,randint(50,100),0,0,0.5,0.2)
						camera_group.add(bullet)
						bullet_group.add(bullet)
					
				if ev.type==FINGERDOWN or ev.type==FINGERMOTION:
					if ev.x*Width<H_Width:
						self.fingerx=ev.x*Width
						self.fingery=ev.y*Height
						self.slidex=self.fingerx-self.fingerx_d
						self.slidey=self.fingery-self.fingery_d
					
				if ev.type==FINGERUP:
					if ev.x*Width<H_Width:
						self.fingerx=0
						self.fingery=0
						self.slidex_up+=self.slidex
						self.slidey_up-=self.slidey
						self.slidex=0
						self.slidey=0
			
			camera_group.pos.x=self.slidex_up+self.slidex
			camera_group.pos.y=self.slidey_up-self.slidey
					
			screen.blit(bg,(0,0))
			
			self.draw()
			self.update()
			display.update()
			
game=Game()
if __name__=="__main__":
	game.loop()