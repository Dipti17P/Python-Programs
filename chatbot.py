from tkinter import *
import pyttsx3
engine = pyttsx3.init()
root=Tk()
root.title("Coaching Info Chatbot")

def send():
    send="You -> "+e.get()
    txt.insert(END,"\n"+send)
    user=e.get().lower()
    e.delete(0,END)
    if(user=="hello"):
        txt.insert(END,"\n"+"Khandesh IIT -> Hi")
        engine.say("hi")
        engine.runAndWait()
    elif(user=="hi" or user=="hii" or user=="hiii"):
        txt.insert(END, "\n" + "Khandesh IIT -> Hello")
        engine.say("hello")
        engine.runAndWait()
    elif (user == "how are you" or user == "hru" or user == "h r u"):
        txt.insert(END, "\n" + "Khandesh IIT -> fine! and you")
        engine.say("fine! and you")
        engine.runAndWait()
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Khandesh IIT -> Great! how can I help you."+"\n1:- C Language \n2:-C++ Language \n3:-Data Structures \n4:-Java \n5:-PHP \n6:-Python \n7:-Android \n8:-Project Development \n9:-Exit")
        engine.say("Great! how can I help you.")
        engine.runAndWait()
    elif (user == "1" or user == "C Language" or user == "1:- C Language"):
        txt.insert(END, "\n" + "Khandesh IIT -> C-Language \n Course Fees 3000 Rs \n Duration 2 months")
        engine.say("Great! C Language Select. Course Fees 3000 Rs. Duration 2 months")
        engine.runAndWait()
    elif (user == "2" or user == "C++ Language" or user == "2:-C++ Language"):
        txt.insert(END, "\n" + "Khandesh IIT -> C++ Language \n Course Fees 2000 Rs \n Duration 3 months")
        engine.say("Great! C++ Language Select. Course Fees 2000 Rs. Duration 3 months")
        engine.runAndWait()
    elif (user == "3" or user == "Data Structures" or user == "3:-Data Structures"):
        txt.insert(END, "\n" + "Khandesh IIT -> Data Structures \n Course Fees 5000 Rs \n Duration 5 months")
        engine.say("Great! Data Structures Select. Course Fees 5000 Rs. Duration 5 months")
        engine.runAndWait()
    elif (user == "4" or user == "Java" or user == "4:-Java"):
        txt.insert(END, "\n" + "Khandesh IIT -> Java-Language \n Course Fees 3000 Rs \n Duration 3 months")
        engine.say("Great! Java Language Select. Course Fees 3000 Rs. Duration 3 months")
        engine.runAndWait()
    elif (user == "5" or user == "PHP" or user == "5:-PHP"):
        txt.insert(END, "\n" + "Khandesh IIT -> PHP-Language \n Course Fees 5000 Rs \n Duration 6 months")
        engine.say("Great! PHP Language Select. Course Fees 5000 Rs. Duration 6 months")
        engine.runAndWait()
    elif (user == "6" or user == "Python" or user == "6:-Python"):
        txt.insert(END, "\n" + "Khandesh IIT -> Python-Language \n Course Fees 7500 Rs \n Duration 6 months")
        engine.say("Great! Python Language Select. Course Fees 7500 Rs. Duration 6 months")
        engine.runAndWait()
    elif (user == "7" or user == "Android" or user == "7:-Android"):
        txt.insert(END, "\n" + "Khandesh IIT -> Android \n Course Fees 5000 Rs \n Duration 7-8 months")
        engine.say("Great! Android Select. Course Fees 5000 Rs. Duration 7-8 months")
        engine.runAndWait()
    elif (user == "8" or user == "Project Development" or user == "8:-Project Development"):
        txt.insert(END, "\n" + "Khandesh IIT -> Project Development \n Course Fees 5000 Rs \n Duration 6-7 months")
        engine.say("Great! Project Development Select. Course Fees 5000 Rs. Duration 6-7 months")
        engine.runAndWait()
    elif (user == "bye" or user == "9" or user == "9:-Exit"):
        txt.insert(END, "\n" + "Khandesh IIT -> Great! bye")
        engine.say("Great! byee")
        engine.runAndWait()
    else:
        txt.insert(END, "\n" + "Khandesh IIT -> Sorry! I can't understand your question.")
        engine.say("Sorry! I can't understand your question.")
        engine.runAndWait()
        e.delete(0, END)

txt=Text(root,font=("Arial",10,"bold"),fg="black",bg="white")
txt.insert(END,"Press Hii or Hello to get started")
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=40,bd=2,font=("Arial",10,"bold"),fg="red",bg="white")
e.grid(row=1,column=0)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
root.mainloop()
