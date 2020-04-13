from tkinter import *
from gpiozero import LED

class relayGUI(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buttons()
        self.pin = int(input("Please enter pin number -> "))
        self.relay = LED(self.pin)

    def buttons(self):
        self.on = Button(self, text = "Turn ON", command = self.relay.on)
        self.on.pack(side = LEFT)
        self.off = Button(self, text = "Turn OFF", command =  self.relay.off)
        self.off.pack(side = LEFT)

        self.quit = Button(self, text= "QUIT", fg="red", command = self.master.destroy)
        self.quit.pack(side = BOTTOM)

root = Tk()
relay = relayGUI(root)
root.mainloop()
