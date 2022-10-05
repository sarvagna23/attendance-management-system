class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		
		
		label1=tk.Label(self,text="Attendance Management System Project in Python",font=("Times",26))
    
		bt1=tk.Button(self,text="Add new record",font=("Times",16),height=2,width=17,bg="blue" ,command=lambda:controller.show_frame(NewRecord))
		bt2=tk.Button(self,text="Manage attendance",font=("Times",16),height=2,width=17,bg="yellow",command=lambda:controller.show_frame(ManageAttendance))
		bt3=tk.Button(self,text="Delete record",font=("Times",16),height=2,width=17,bg="red",command=lambda:controller.show_frame(DeleteRecord))
		bt4=tk.Button(self,text="Edit record",font=("Times",16),height=2,width=17,bg="orange",command=lambda:controller.show_frame(EditRecord))
		label1.pack()
		bt1.pack()
		bt2.pack()
		bt3.pack()
		bt4.pack()
