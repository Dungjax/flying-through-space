from setting import *
from camera import camera_group

class Object(sprite.Sprite):
	def __init__(self,imgs,size,x,y,z,fly_speed):
		super().__init__()
		self.pos=Vector3(x+camera_group.pos.x,y-camera_group.pos.y,z+camera_group.pos.z)
		self.size=size
		self.imgs=imgs
		self.imgs_index=0
		self.image=transform.scale(self.imgs[self.imgs_index],(int(self.size/z),int(self.size/z)))
		self.rect=self.image.get_rect()
		self.rect.center=H_Width+x/z,H_Height+y/z
		self.fly_speed=fly_speed
		self.index_speed=abs(fly_speed)*2
	
	def animate(self):
		self.imgs_index+=self.index_speed
		if self.imgs_index>=len(self.imgs):
			self.imgs_index=0
	
	def update(self):
		self.animate()
		
		self.pos.z+=self.fly_speed
		x_proj=self.pos.x-camera_group.pos.x
		y_proj=self.pos.y+camera_group.pos.y
		z_proj=self.pos.z-camera_group.pos.z
		size_proj=int(self.size/(z_proj+0.1))
		max_size=800
		if self.pos.z>0 and 0<size_proj<max_size:
			self.image=transform.scale(self.imgs[int(self.imgs_index)],(size_proj,size_proj))
			self.image.set_alpha(255/z_proj+1)
			self.rect=self.image.get_rect()
			self.rect.center=H_Width+x_proj/z_proj,H_Height+y_proj/z_proj
		else :
			self.kill()
		