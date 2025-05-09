from tkinter import *
import pyttsx3       
engine = pyttsx3.init()
def play_text():
    text = text_entry.get()  
    engine.say(text)
    engine.runAndWait()
def set_action():
    text_entry.delete(0, END)
root =Tk()
root.title("Text to Speech") 
root.geometry("400x200")
label1 = Label(root, text="Text to Speech", font="Tahoma 20 bold")
label1.pack(pady=20)
label2 = Label(root, text="Enter your text:", anchor="nw", font="Tahoma 12 bold")
label2.pack(fill="x", padx=20)
text_entry = Entry(root, width=35, font="Tahoma 12 bold")
text_entry.pack(pady=10)
button1 = Button(root, text="Play", width=10, height=2, command=play_text, bg="green", fg="white", font="Helvetica 12 bold")
button1.pack(side="left", padx=10, pady=10)
button2 = Button(root, text="Exit", width=10, height=2, command=root.destroy, bg="red", fg="white", font="Helvetica 12 bold")
button2.pack(side="left", padx=10, pady=10)
button3 = Button(root, text="Set", width=10, height=2, command=set_action, bg="blue", fg="white", font="Helvetica 12 bold")
button3.pack(side="left", padx=10, pady=10)
root.mainloop()
