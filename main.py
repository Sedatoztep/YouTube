#Created by Sedat Öztep

--------

from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("python.ogreniyorum")

Label(root,text = 'Youtube Video İndirme', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Buraya Linki Yapıştırınız:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'İNDİR', font = 'arial 15 bold' ,bg = 'pale violet red',
       padx = 2, command = Downloader).place(x=225 ,y = 150)

root.mainloop()




