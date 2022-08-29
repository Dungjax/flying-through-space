from pygame import display,font,image,sprite,transform,Vector3,time,SCALED,FULLSCREEN
from os import walk
#screen setup
Width=display.Info().current_w
Height=display.Info().current_h
H_Width=Width/2
H_Height=Height/2
screen=display.set_mode((Width,Height),SCALED | FULLSCREEN)
#color
grey=(50,50,50)
red=(255,0,0)
#font & text
font=font.Font(None,30)
def cre_text(name,x,y):
	text=font.render(str(name),1,red)
	screen.blit(text,(x,y))
#image
bg=transform.scale(image.load("bg.png"),(Width,Height)).convert()
def import_sprite(folder):
	for _,__,img in walk(folder):
		return [image.load(folder+i).convert_alpha() for i in img]
aeteroid_imgs=[]
for i in range(3):
	aeteroid_imgs.append(import_sprite(f"aeteroid{i}/"))
bullets_img=import_sprite("bullets/")
#sprite group
aeteroid_group=sprite.Group()
bullet_group=sprite.Group()
#time
clock=time.Clock()