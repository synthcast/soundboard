from playsound import playsound
import tkinter as tk
from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


root = tk.Tk()
links = []
root.counter = 0

root.title("Music Player")

e = Entry(root, width=30)
e.pack()

def Link():
    for widget in frame.winfo_children():
        widget.destroy()
    search = e.get()
    print(search)
    link = 'https://www.youtube.com/results?search_query='
    hello = (f"{link}{search}")
    print(hello)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(hello)
    xpath = '//*[@id="video-title"]'
    btn = driver.find_element_by_xpath(xpath)
    btn.click()
    links.append(hello)
    for app in links:
        label = tk.Button(frame, text=app, bg="gray", command=lambda:[Prev(), Save()])
        label.pack()


def Prev():
    search = e.get()
    link = 'https://www.youtube.com/results?search_query='
    hello = (f"{link}{search}")
    print(hello)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(hello)
    xpath = '//*[@id="video-title"]'
    btn = driver.find_element_by_xpath(xpath)
    btn.click()


def Save():
    search = e.get()
    link = 'https://www.youtube.com/results?search_query='
    hello = (f"{link}{search}\n")
    root.counter +=1
    f = open("save.txt", "a")
    f.write(hello)
    f.close()
    f.open("save.txt", 'r')
    f.readlines()







##linkButton
Link = tk.Button(root, text="Search", padx=10,
                             pady=5, fg="white", bg="#263D42", command=Link)
Link.pack()

##exitButton
exitButton = tk.Button(root, text="Exit", padx=10,
                             pady=5, fg="white", bg="#263D42", command=root.destroy).pack()

##canvas
canvas = tk.Canvas(root, height=200, width=300, bg="#263D42")
canvas.pack()

canvas.create_text(155,50,fill="darkblue",font="Times 20 italic bold",
                        text="Search For A Song")

##frame
frame = tk.Frame(root, height=30, width=300, bg="#263D42")
frame.pack()


##playsound('D:\csgosoundboard\deathgift_drop.mp3')

root.mainloop()


##with open('save.txt', 'a') as f:
        ##for app in links:
            ##f.write(app + '\n')


