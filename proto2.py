from tkinter import*
import time
from datetime import datetime
import threading
from tkinter import ttk
import ytb_vid_strmr as yt

class app(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master=master
		self.master.geometry("420x550")
		self.interface()
		self.text_box=Entry(self,width=50)
		self.text_box.place(x=0,y=450)
		self.display=Text(self,state=DISABLED)
		self.display.place(x=0,y=0)
		

		

	def interface(self):
		self.pack(fill=BOTH, expand=1)
		a=Button(self,text="Enter",width=50,height=3)
		a.place(x=0,y=480)
		a.bind("<Return>",self.thread)
		a.bind("<Button-1>",self.thread)
	def enter(self):
		now = datetime.now()
		current_time = now.strftime("%H:%M")
		text=self.text_box.get()
		message=str(current_time)+":"+text
		self.text_box.delete(0,END)
		self.display.configure(state=NORMAL)
		self.display.insert(END,message+"\n"+"\n")
		self.display.configure(state=DISABLED)
		self.display.see("end")


		if(text[0]=="-"):
			if(text[1:5]=="play"):
				song_name=text[6:]
				yt.song_play(song_name)
				self.display.configure(state=NORMAL)
				self.display.insert(END,"Playing "+song_name+"\n"+"\n")
				self.display.configure(state=DISABLED)
				self.display.see("end")
				yt.ply()
			if(text[1:6]=="pause"):
				yt.ply()
				self.display.configure(state=NORMAL)
				self.display.insert(END,"Paused "+"\n"+"\n")
				self.display.configure(state=DISABLED)
				self.display.see("end")
			if(text[1:7]=="resume"):
				yt.ply()
				self.display.configure(state=NORMAL)
				self.display.insert(END,"Resumed "+"\n"+"\n")
				self.display.configure(state=DISABLED)
				self.display.see("end")
				
			if(text[1:5]=="stop"):
				yt.sttop()
				self.display.configure(state=NORMAL)
				self.display.insert(END,"Stopped"+"\n"+"\n")
				self.display.configure(state=DISABLED)
				self.display.see("end")
				

	def thread(self,event):
		t=threading.Thread(target=self.enter)
		t.start()
				
		
		



a=Tk()
b=app(a)
b.mainloop()