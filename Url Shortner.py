from tkinter import *
import pyshorteners
import clipboard

root=Tk()

url_input = StringVar()
Entry(textvariable=url_input,width=35).grid(row=0,column=1)

def sb():
    try:
        url = url_input.get()
        s = pyshorteners.Shortener()
        final_result = s.tinyurl.short(url)
        str_url.set(final_result)
    except:
        str_url.set("Please Paste the URL")

def copy():
    try:
        clipboard.copy(str_url.get())
        print("URL Copied succesfully!!")
    except:
        str_url.set("Something went wrong. Try Again!!")

root.geometry("450x350")
root.resizable(False,False)
root.title("URL Shortner")

Label(text="Paste URL:",font="Book_Antiqua 10 bold").grid(row=0,column=0,pady=20,padx=30)
Button(text="SUBMIT",command=sb,bg="green",font="verdana 10 bold",fg="white").grid(row=1,column=1)

str_url = StringVar()
Label(textvariable=str_url,width=35,bg="white").grid(row=2,column=1)

Label(text="Shortened URL:",font="Book_Antiqua 10 bold").grid(row=2,column=0,pady=20)
Button(text="PASTE URL",command=copy,bg="skyblue4",font="verdana 10 bold",fg="white").grid(row=3,column=1)

root.mainloop()
