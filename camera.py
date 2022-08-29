from setting import *

class Camera_group(sprite.Group):
	def __init__(self):
		super().__init__()
		self.pos=Vector3(0,0,0)

	def z_draw(self):
		for i in sorted(self.sprites(),key=lambda sprite:sprite.pos.z,reverse=1):
			screen.blit(i.image,i.rect)

camera_group=Camera_group()