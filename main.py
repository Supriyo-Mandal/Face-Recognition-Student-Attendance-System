from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\img1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second Image
        img1=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\university.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=500,y=0,width=500,height=130)

        # Third Image
        img2=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\img3.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1000,y=0,width=550,height=130)

        # Background Image
        img3=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\background.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # Title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student Button
        img4=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Student Details.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img5=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Face Detector.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)

        # Attendence Button
        img6=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Attendance.gif")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_3=Button(bg_img,text="Attendence", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=800,y=300,width=220,height=40)

        # Help Desk Button
        img7=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Help Desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_4=Button(bg_img,text="Help Desk", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height=40)

        # Train Data Button
        img8=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Train Data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)

        b5_5=Button(bg_img,text="Train Data", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=200,y=580,width=220,height=40)

        # Photos Button
        img9=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Photos.webp")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)

        b6_6=Button(bg_img,text="Photos", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=500,y=580,width=220,height=40)

        # Developer Button
        img10=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b6.place(x=800,y=380,width=220,height=220)

        b6_6=Button(bg_img,text="Developer", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=800,y=580,width=220,height=40)

        # Exit Button
        img11=Image.open(r"C:\Users\SUDIPTO\Desktop\Face Recognition Student Attendance System\college_images\Exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=1100,y=380,width=220,height=220)

        b7_7=Button(bg_img,text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=1100,y=580,width=220,height=40)





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
