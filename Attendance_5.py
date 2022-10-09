class EditRecord(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1=tk.Label(self,text="Edit Record",font=("Times",24))
		bt1=tk.Button(self,text="Back to home",bg="red",font=("Times",16),height=2,width=17,command=lambda:controller.show_frame(StartPage))
		label1.pack()
		lb2=tk.Label(self,text="Input Subject ID: ",font=("Times",15))
		txt1=tk.Entry(self)
		lb2.pack()
		txt1.pack()
		lb3=tk.Label(self,text="Number of times attended:",font=("Times",15))
		txt2=tk.Entry(self)
		lb4=tk.Label(self,text="Number of times bunked:",font=("Times",15))
		txt3=tk.Entry(self)
		lb3.pack()
		txt2.pack()
		lb4.pack()
		txt3.pack()
		bt3=tk.Button(self,text="Update",bg="green",font=("Times",16),height=2,width=17,command=lambda:self.update(txt1.get(),txt2.get(),txt3.get()))
		bt2=tk.Button(self,text="Show subjects ID",bg="yellow",font=("Times",16),height=2,width=17,command=lambda:self.showid(controller))
		bt2.pack()
		bt3.pack()
		bt1.pack()
	def update(self,i,p,b):
		i=int(i)
		
		if p=="" or p==" " or p=="\n":
			p=0
		else:
			p=int(p)
		if b=="" or b==" " or b=="\n":
			b=0
		else:
			b=int(b)
		try:
		
			conn=sql.connect("attend")
			cur=conn.cursor()
			cur.execute("SELECT * FROM attable WHERE subid=?",(i,))
			kk=cur.fetchone()
			np=p
			
			nb=b
				
			cur.execute("UPDATE attable SET attended = ? WHERE subid= ?",(np,i))
			cur.execute("UPDATE attable SET bunked = ? WHERE subid= ?",(nb,i))
			conn.commit()
			conn.close()
			messagebox.showinfo("Alert!", "Updated")
			
		except:
			messagebox.showinfo("Alert!", "There is no record")
	
	def showid(self,):
		try:
			conn=sql.connect("attend")
			cur=conn.cursor()
			cur.execute('SELECT * FROM attable')
			text=""
			for w in cur:
				text=text+"sub id "+str(w[0])+" "+w[1]+"\n"
			messagebox.showinfo("Subject ID: ", text)
			conn.commit()
			conn.close()
		except:
			messagebox.showinfo("Alert!", "There is no record")
