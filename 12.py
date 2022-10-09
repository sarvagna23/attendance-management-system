class AddSubjects(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1=tk.Label(self,text="Add subject's name seperated by commas(,)",font=("Times",16))
		txt1=tk.Text(self,font=("Times",16),width=48,height=3)
		
	
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
      



# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
