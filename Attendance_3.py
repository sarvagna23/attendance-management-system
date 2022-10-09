class ManageAttendance(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		
		label1=tk.Label(self,text="Manage Attendance",font=("Times",24))
		label1.pack()
		bt2=tk.Button(self,text="Show status", bg="blue",font=("Times",16.5),height=2,width=17,command=lambda:self.showstatus(controller))
		bt3=tk.Button(self,text="Today's data",  bg="orange",font=("Times",16),height=2,width=17,command=lambda:controller.show_frame(TodayData))	
		bt1=tk.Button(self,text="Back to home",bg="red",font=("Times",16),height=2,width=17,command=lambda:controller.show_frame(StartPage))
		bt2.pack()
		bt3.pack()
		bt1.pack()
	def showstatus(self,controller):
		try:
			conn=sql.connect("Attend")
			cur=conn.cursor()
			cur.execute('SELECT * FROM attable')
			text=""
			for w in cur:
				if w[2]==0 and w[3]==0:
					per="0"
				else:
					per=w[2]/(w[2]+w[3])
					per=per*100
					per=str(int(per))
				text=text+"sub id "+str(w[0])+" "+w[1]+" "+per+"%\n"
			messagebox.showinfo("status", text)
		except:
			messagebox.showinfo("Alert!", "No Records Found")	
