from tkinter import * #to import tkinter
import tkinter
from tkinter import ttk  #style the tkinter widgets just like CSS does in HTML
from tkinter.messagebox import showinfo #to import messagebox
from tkinter import Menu #to import menu
from PIL import Image, ImageTk #for image
import time #for time
import webbrowser #for opening website
import os #for accessing device file, interacting with the operating system
from tkinter import filedialog #for accessing file directory
import requests
from io import BytesIO

ws=Tk()

Grid.rowconfigure(ws,0,weight=1)
Grid.columnconfigure(ws,0,weight=1)
 
Grid.rowconfigure(ws,1,weight=1)

ws.state('zoomed')
ws.title('Face Attendance')
# Adding Background Image
ws.config(bg='black')



# Addinf new page
def newPage():
	new_win= Toplevel(ws)
	new_win.geometry('1100x100')
	new_win.title('Copy Path')
	new_win.config(bg='#050A30')
	Take=Entry(new_win,
			width=90,
			justify='center',
			font=('Arial', 15),
			fg='black',
			bg='white')
	Take.place(relx=0.05,rely=0.05)
	Take.insert(0,'Paste the path of the picture here')
	def Clear():
		Take.delete(0,END)
	btn3=Button(new_win,
			 text='Clear',
			 command=Clear,
			 font=('Arial', 12))
	btn3.place(x=100,y=48)
	def Submit():
		x=str(Take.get())
		y=''
		for i in x:
			y+=i
			if i=="\\":
				y+="\\"
		
		disp_tf.configure(state='normal')
		disp_tf.delete(0,END)
		disp_tf.insert(0,'Wait...scanning in progress')
		Take.configure(state='disabled')
		uploadPic(y)
		
		new_win.destroy()

	btn4=Button(new_win,
			 text='Submit',
			 command=Submit,
			 font=('Arial', 12))
	btn4.place(x=950,y=48)
	



#Adding Functions
FaceNumber=0





# Upload the picture from device
def uploadPic(FacePath):
	try:
		import cv2
		import dlib
		import cv2
		frame = cv2.imread(FacePath)

		# RGB to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		detector = dlib.get_frontal_face_detector()
		faces = detector(gray)

		# Iterator to count faces
		i = 0
		for face in faces:

			# Get the coordinates of faces
			x, y = face.left(), face.top()
			x1, y1 = face.right(), face.bottom()
			cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

			# Increment iterator for each face in faces
			i = i+1

			# Display the box and faces
			cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			print(face, i)

		# Display the resulting frame
		cv2.imshow('frame', frame)
		FaceNumber=i

		disp_tf.configure(state='normal')
		disp_tf.delete(0,END)
		disp_tf.insert(0,f'Number Of Faces: {FaceNumber}')
		disp_tf.configure(state='disabled')
	except:
		disp_tf.configure(state='normal')
		disp_tf.delete(0,END)
		disp_tf.insert(0,'Try Again With Valid Photo Path')
		disp_tf.configure(state='disabled')


	




# Taking Picture From Web Cam
def takePic():
    # Import required libraries
	import cv2
	import numpy as np
	import dlib

	disp_tf.configure(state='normal') #making the entry box enabled
	# Connects to your computer's default camera
	cap = cv2.VideoCapture(0)


	# Detect the coordinates
	detector = dlib.get_frontal_face_detector()


	# Capture frames continuously
	while True:

		# Capture frame-by-frame
		ret, frame = cap.read()
		frame = cv2.flip(frame, 1)

		# RGB to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = detector(gray)

		# Iterator to count faces
		i = 0
		for face in faces:

			# Get the coordinates of faces
			x, y = face.left(), face.top()
			x1, y1 = face.right(), face.bottom()
			cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

			# Increment iterator for each face in faces
			i = i+1

			# Display the box and faces
			cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			print(face, i)

		# Display the resulting frame
		cv2.imshow('frame', frame)
		FaceNumber=i
	
		disp_tf.delete(0,END)
		disp_tf.insert(0,f'Number Of Faces: {FaceNumber}')

		# This command let's us quit with the "q" button on a keyboard.
		if cv2.waitKey(1) & 0xFF == ord('q'):
			disp_tf.configure(state='disabled')
			break



	# Release the capture and destroy the windows
	cap.release()
	
	




# Adding Buttons

btn0=Button(ws, text="Click Image\n(Press 'q' to quit)",
           font=("Castellar",15,'bold'),
           borderwidth = 3,
           bg='#ffffcc',
           activebackground='yellow',
		   command=takePic
           )

btn0.place(x=200,y=150)

btn1=Button(ws, text="Click To Upload\n(Paste the path)",
           font=("Castellar",15,'bold'),
           borderwidth = 3,
           bg='#ffffcc',
           activebackground='yellow',
		   command=newPage
		   
           )

btn1.place(x=1240,y=150)



# Output field
disp_tf = Entry(
    ws,
    width=80,
    justify='center',
    font=('Arial', 20)
    )

disp_tf.insert(0, 'Result appears here')
disp_tf.configure(state='disabled')
disp_tf.place(x=200,y=400,height=200)

# Running the frame
ws.mainloop()
