import tkinter as tk
from tkinter import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import subprocess

root = tk.Tk()
links = []
root.counter = 1

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
    firefox = webdriver.FirefoxOptions()
    firefox.add_argument('--disable-notifications')
    firefox.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox)
    driver.get(hello)
    xpath = '//*[@id="video-title"]'
    btn = driver.find_element_by_xpath(xpath)
    btn.click()
    print (driver.current_url)
    url = (driver.current_url)
    driver.close()
    subprocess.call(["mpv", url])
    links.append(hello)

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


root.mainloop()




