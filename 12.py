class AddSubjects(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1=tk.Label(self,text="Add subject's name seperated by commas(,)",font=("Times",16))
		txt1=tk.Text(self,font=("Times",16),width=48,height=3)
		
		bt2=tk.Button(self,text="Add subjects!",bg="orange",font=("Times",16),height=2,width=17,command=lambda:self.addsub(txt1.get("1.0",tk.END),controller))
		bt1=tk.Button(self,text="Back to home",bg="red",font=("Times",16),height=2,width=17,command=lambda:controller.show_frame(StartPage))
		label1.pack()
		txt1.pack()
		bt2.pack()	
		bt1.pack()
	def addsub(self,a,controller):
		
		conn=sql.connect('attend')
		cur=conn.cursor()
		cur.execute('DROP TABLE IF EXISTS attable')
		
		a=a[0:len(a)-1]
		a=a.split(",")
		
		if len(a)==1 and a[0]=="" :
			messagebox.showinfo("Alert!", "Please enter the subjects")
		else:
			sid=1
			cur.execute('CREATE TABLE attable(subid INTEGER,subject TEXT,attended INTEGER,bunked INTEGER)')
			for sub in a:
				cur.execute('INSERT INTO attable (subid,subject,attended,bunked) VALUES(?,?,?,?)',(sid,sub,0,0))
				sid=sid+1
			conn.commit()
			conn.close()
			messagebox.showinfo("congratulations!", "subjects are added")
			controller.show_frame(StartPage)
      
