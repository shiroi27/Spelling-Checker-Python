import tkinter
from tkinter import *
from textblob import TextBlob

# GUI Set Up
root= Tk()
root.title(" SPELLING CHECKER ")
root.geometry("800x500+200+200")
root.config(bg = "#FCC096")

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right= str(a.correct())

    spell.config(text=right)

# Fake header
header = Frame(root , width = 800 , height = 60 , bg = "#BDADFF" )
header.place(x=0 , y = 0)

# Header Title
title = Label ( root , text = " <<  SPELLING CHECKER  >> " , font=("Times New Roman" , 38 , "bold") ,
bg = "#BDADFF" , fg = "#000000")
title.place(x=140 , y = 5)

# Decorative line
line = Frame ( root , width = 800 , height = 6 , bg = "#F26262" )
line.place(x= 0 , y = 60)

# Subheading
subtitle = Label ( root , text = "ENTER TEXT" , font=("georgia" , 30 , "bold") ,
bg = "#FCC096" , fg = "#000000")
subtitle.place(x=309 , y = 90)

# Entry Box
enter_text = Entry(root,justify="center" , width = 40 , font = ("Times New Roman" , 25 , "bold") ,
bg = "#F9F9F9" , fg= "#000000" , borderwidth= 3)
enter_text.place(x= 140 , y = 150)

# Check_button
button = Button ( root , text = " CHECK " , font = ("Georgia" , 28 , "bold"), fg = "#000000" , command = check_spelling)
button.place(x= 335 , y = 220)

# Corrected
correct = Label ( root , text = " CORRECTED TEXT " , font= ("Georgia" , 30 ,"bold"),
bg = "#FCC096" , fg = "#000000")
correct.place(x= 260 , y = 300)

# Frame to simulate border color
spell_frame = Frame(root, bg="#FF5E5E", bd=0, highlightthickness=0)
spell_frame.place(x=140, y=345, width=530, height=50)

# Right Spelling Label inside frame
spell = Label(spell_frame, font=("Times New Roman", 25, "bold"), bg="#FFFFFF", fg="#000000",
width=38, height=2, borderwidth=0)
spell.pack(padx=3, pady=3)

root.mainloop()