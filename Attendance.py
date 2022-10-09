class AttendanceManager(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk. __init__(self,*args,**kwargs)
		container=tk.Frame(self)
		
		
		container.grid_columnconfigure(0,weight=1)
		
		
		
		self.show_frame(StartPage)
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()
