import pyshorteners as p
from tkinter import *
import clipboard

window  = Tk()
window.geometry("400x200")
window.resizable(False, False)
window.title("URL Shortener")

url_input = Entry(window, font=("Arial", "16"))
url_input.grid(row=1,column=2, pady=8)
str_url = StringVar(window)

shortened_text = Label(window,textvariable=str_url, bg="#2ecc71", fg="#fff", font=("Arial","16"))
shortened_text.grid(row=3, column=2, pady=6)
def shorten():
    try:
        url = url_input.get()
        s = p.Shortener(api_key='YOUR API KEY') #get your api key from https://dev.bitly.com
        short_link = s.bitly.short(url)
        str_url.set(short_link)
    except:
        str_url.set("An Error Occured, Try Again")


btn = Button(window, text="Shorten", padx=8, pady=4, bg="#2ecc71", fg="#fff", font=("Arial","16"), activebackground="#16a085", command=shorten)
btn.grid(row=2, column=2, pady=6)

def copy():
    clipboard.copy(str_url.get())

copy_btn = Button(window, text="COPY", bg="#2ecc71", fg="#fff", font=("Arial","16"), command=copy)
copy_btn.grid(row=4, column=2, pady=6)

EnterLink = Label(window,text="Enter your URL", font=("Arial","16"))
EnterLink.grid(row=1, column=3, pady=6)

print("URL Shortener has started")

window.mainloop()
