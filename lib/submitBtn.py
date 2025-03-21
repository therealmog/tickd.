# Amogh NG
# Submit button inheriting from CTkButton

from customtkinter import *
from PIL import Image


class SubmitButton(CTkButton):
    def __init__(self,parent,command,colour,buttonSize:tuple=(20,20),radius=20,icon="tick"):

        if icon == "tick":
            imgPath = "logo//tick.png"
        else:
            imgPath = "icons//add.png"
        self.img = CTkImage(Image.open(imgPath).resize(buttonSize),size=buttonSize)
        super().__init__(master=parent,width=1,image=self.img,fg_color=colour,command=command,text="",corner_radius=radius)


    