from tkinter import *

class MovingDisk:
    
    def __init__(self,
                 height=300,
                 width=300,
                 bg_color='white',
                 diameter=30,
                 x_init=10,
                 y_init=10,
                 motion_step=10):
        """
        """
        self.gui=Tk(className='Moving Disk')
        self.gui.configure(bg=bg_color)
        self.step=motion_step
        self.diameter=diameter
        self.x=x_init
        self.y=y_init
        self.canvas=Canvas(self.gui,
                           bg="green",
                           height=height,
                           width=width)
        self.disk=self.canvas.create_oval(self.x,
                                          self.y,
                                          self.x+self.diameter,
                                          self.y+self.diameter,
                                          width=0,
                                          fill="red")
        self.canvas.pack(side=LEFT)
        
        Button(self.gui,text="Quit",command=self.gui.destroy).pack(side=BOTTOM)
        Button(self.gui,text="gauche",command=self._left).pack()
        Button(self.gui,text="droite",command=self._right).pack()
        Button(self.gui,text="haut",command=self._up).pack()
        Button(self.gui,text="bas",command=self._down).pack()
        self.gui.mainloop()
        
    def _move(self,dx,dy):
        """
        """
        self.x+=dx
        self.y+=dy
        self.canvas.coords(self.disk,
                           self.x,
                           self.y,
                           self.x+self.diameter,
                           self.y+self.diameter)
        
    def _left(self,):
        """
        """
        self._move(-self.step,0)
        
    def _right(self,):
        """
        """
        self._move(self.step,0)
        
    def _up(self,):
        """
        """
        self._move(0,-self.step)
        
    def _down(self,):
        """
        """
        self._move(0,self.step)
