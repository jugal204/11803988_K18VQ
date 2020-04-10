from tkinter import *
from pygame import mixer

master = Tk()
master.title("Music")

headerPhoto=PhotoImage(file="head.png")
hphoto=Label(master, image = headerPhoto,pady=2)
hphoto.pack()
mixer.init()  #initializing the mixer

def playMusic1():
    mixer.music.load("Aankhon Mein Aansoo.mp3")
    mixer.music.play()

def stopMusic1():
    mixer.music.stop()
    
def playMusic2():
    mixer.music.load("Ek Haseena Thi Ek Deewana Tha.mp3")
    mixer.music.play()
    
def stopMusic2():
    mixer.music.stop()

def playMusic3():
    mixer.music.load("Hanste Hanste.mp3")
    mixer.music.play()

def stopMusic3():
    mixer.music.stop()
    
def playMusic4():
    mixer.music.load("Hue Bechain.mp3")
    mixer.music.play()

def stopMusic4():
    mixer.music.stop()
    
def playMusic5():
    mixer.music.load("Humsafar.mp3")
    mixer.music.play()

def stopMusic5():
    mixer.music.stop()
    
def playMusic6():
    mixer.music.load("Lagdi Na Akh.mp3")
    mixer.music.play()

def stopMusic6():
    mixer.music.stop()
    
def playMusic7():
    mixer.music.load("Lavi Naa.mp3")
    mixer.music.play()

def stopMusic7():
    mixer.music.stop()
    
def playMusic8():
    mixer.music.load("Man Mera.mp3")
    mixer.music.play()

def stopMusic8():
    mixer.music.stop()
    
def playMusic9():
    mixer.music.load("Saanson Ko.mp3")
    mixer.music.play()

def stopMusic9():
    mixer.music.stop()
    
def playMusic10():
    mixer.music.load("Time Table.mp3")
    mixer.music.play()

def stopMusic10():
    mixer.music.stop()
    
def playMusic11():
    mixer.music.load("Tu Itni Khoobsurat Hai.mp3")
    mixer.music.play()

def stopMusic11():
    mixer.music.stop()

def playMusic12():
    mixer.music.load("Yaar Beli.mp3")
    mixer.music.play()

def stopMusic12():
    mixer.music.stop()
    
def button_search():
    if E1.get() == "Telugu":
         middleFrame.destroy()
         bottomFrame.destroy()
         middleFrame1=LabelFrame(master,text="Telugu songs",bd=5)
         middleFrame1.pack(side=LEFT,padx=50,pady=10)
         p1=PhotoImage(file="Aankhon mei.png")
         labelphoto1=Label(middleFrame1, image = p1)
         labelphoto1.image=p1
         labelphoto1.grid(row=0,column=0,padx=20)
         B1 = Button(middleFrame1, text ="play",command = playMusic1)
         B1.grid(row=1,column=0,sticky=W,padx=30)
         B2 = Button(middleFrame1, text ="stop",command = stopMusic1)
         B2.grid(row=1,column=0,sticky=E,padx=30)
         p2=PhotoImage(file="ek hasina.png")
         labelphoto2=Label(middleFrame1, image = p2)
         labelphoto2.image=p2
         labelphoto2.grid(row=0,column=1,padx=20)
         B3 = Button(middleFrame1, text ="play",command = playMusic2)
         B3.grid(row=1,column=1,sticky=W,padx=30)
         B4 = Button(middleFrame1, text ="stop",command = stopMusic2)
         B4.grid(row=1,column=1,sticky=E,padx=30)
         p3=PhotoImage(file="haste haste.png")
         labelphoto2=Label(middleFrame1, image = p3)
         labelphoto2.image=p3
         labelphoto2.grid(row=0,column=2,padx=20)
         B5 = Button(middleFrame1, text ="play",command = playMusic3)
         B5.grid(row=1,column=2,sticky=W,padx=30)
         B6 = Button(middleFrame1, text ="stop",command = stopMusic3)
         B6.grid(row=1,column=2,sticky=E,padx=30)
         p4=PhotoImage(file="hue bechain.png")
         labelphoto2=Label(middleFrame1, image = p4)
         labelphoto2.image=p4
         labelphoto2.grid(row=0,column=3,padx=20)
         B7 = Button(middleFrame1, text ="play",command = playMusic4)
         B7.grid(row=1,column=3,sticky=W,padx=30)
         B8 = Button(middleFrame1, text ="stop",command = stopMusic4)
         B8.grid(row=1,column=3,sticky=E,padx=30)
    elif E1.get() == "pop":
         middleFrame.destroy()
         bottomFrame.destroy()
         middleFrame1=LabelFrame(master,text="Pop Songs",bd=5)
         middleFrame1.pack(side=LEFT,padx=50,pady=10)
         p1=PhotoImage(file="humsafar.png")
         labelphoto1=Label(middleFrame1, image = p1)
         labelphoto1.image=p1
         labelphoto1.grid(row=0,column=0,padx=20)
         B1 = Button(middleFrame1, text ="play",command = playMusic5)
         B1.grid(row=1,column=0,sticky=W,padx=30)
         B2 = Button(middleFrame1, text ="stop",command = stopMusic5)
         B2.grid(row=1,column=0,sticky=E,padx=30)
         p2=PhotoImage(file="lagdi na aankh.png")
         labelphoto2=Label(middleFrame1, image = p2)
         labelphoto2.image=p2
         labelphoto2.grid(row=0,column=1,padx=20)
         B3 = Button(middleFrame1, text ="play",command = playMusic6)
         B3.grid(row=1,column=1,sticky=W,padx=30)
         B4 = Button(middleFrame1, text ="stop",command = stopMusic6)
         B4.grid(row=1,column=1,sticky=E,padx=30)
         p3=PhotoImage(file="laavi na.png")
         labelphoto2=Label(middleFrame1, image = p3)
         labelphoto2.image=p3
         labelphoto2.grid(row=0,column=2,padx=20)
         B5 = Button(middleFrame1, text ="play",command = playMusic7)
         B5.grid(row=1,column=2,sticky=W,padx=30)
         B6 = Button(middleFrame1, text ="stop",command = stopMusic7)
         B6.grid(row=1,column=2,sticky=E,padx=30)
         p4=PhotoImage(file="man mera.png")
         labelphoto2=Label(middleFrame1, image = p4)
         labelphoto2.image=p4
         labelphoto2.grid(row=0,column=3,padx=20)
         B7 = Button(middleFrame1, text ="play",command = playMusic8)
         B7.grid(row=1,column=3,sticky=W,padx=30)
         B8 = Button(middleFrame1, text ="stop",command = stopMusic8)
         B8.grid(row=1,column=3,sticky=E,padx=30)

    elif E1.get() == "Hindi":
         middleFrame.destroy()
         bottomFrame.destroy()
         middleFrame1=LabelFrame(master,text="Hindi songs",bd=5)
         middleFrame1.pack(side=LEFT,padx=50,pady=10)
         p1=PhotoImage(file="saanson ko.png")
         labelphoto1=Label(middleFrame1, image = p1)
         labelphoto1.image=p1
         labelphoto1.grid(row=0,column=0,padx=20)
         B1 = Button(middleFrame1, text ="play",command = playMusic9)
         B1.grid(row=1,column=0,sticky=W,padx=30)
         B2 = Button(middleFrame1, text ="stop",command = stopMusic9)
         B2.grid(row=1,column=0,sticky=E,padx=30)
         p2=PhotoImage(file="time table2.png")
         labelphoto2=Label(middleFrame1, image = p2)
         labelphoto2.image=p2
         labelphoto2.grid(row=0,column=1,padx=20)
         B3 = Button(middleFrame1, text ="play",command = playMusic10)
         B3.grid(row=1,column=1,sticky=W,padx=30)
         B4 = Button(middleFrame1, text ="stop",command = stopMusic10)
         B4.grid(row=1,column=1,sticky=E,padx=30)
         p3=PhotoImage(file="tu itni khoobsurat.png")
         labelphoto2=Label(middleFrame1, image = p3)
         labelphoto2.image=p3
         labelphoto2.grid(row=0,column=2,padx=20)
         B5 = Button(middleFrame1, text ="play",command = playMusic11)
         B5.grid(row=1,column=2,sticky=W,padx=30)
         B6 = Button(middleFrame1, text ="stop",command = stopMusic11)
         B6.grid(row=1,column=2,sticky=E,padx=30)
         p4=PhotoImage(file="yaar beli.png")
         labelphoto2=Label(middleFrame1, image = p4)
         labelphoto2.image=p4
         labelphoto2.grid(row=0,column=3,padx=20)
         B7 = Button(middleFrame1, text ="play",command = playMusic12)
         B7.grid(row=1,column=3,sticky=W,padx=30)
         B8 = Button(middleFrame1, text ="stop",command = stopMusic12)
         B8.grid(row=1,column=3,sticky=E,padx=30)
    else:
         print("No file found")

topFrame = LabelFrame(master,text="Search for a song",padx=200,pady=20)
topFrame.pack(padx=10,pady=10)
E1 = Entry(topFrame, bd =7,width=50)
E1.pack(side=LEFT,padx=200)
B=Button(topFrame,text="search",command = button_search)
B.pack(padx=30)

middleFrame=LabelFrame(master,text="Top songs")
middleFrame.pack(padx=30,pady=10)
photo=PhotoImage(file="Aankhon mei.png")
labelphoto=Label(middleFrame, image = photo)
labelphoto.grid(row=0,column=0,padx=20)
B1 = Button(middleFrame, text ="play",command = playMusic1)
B1.grid(row=1,column=0,sticky=W,padx=30)
B2 = Button(middleFrame, text ="stop", command = stopMusic1)
B2.grid(row=1,column=0,sticky=E,padx=30)
photo1=PhotoImage(file="ek hasina.png")
labelphoto=Label(middleFrame, image = photo1)
labelphoto.grid(row=0,column=1,padx=20)
B3 = Button(middleFrame, text ="play",command = playMusic2)
B3.grid(row=1,column=1,sticky=W,padx=30)
B4 = Button(middleFrame, text ="stop", command = stopMusic2)
B4.grid(row=1,column=1,sticky=E,padx=30)
photo2=PhotoImage(file="haste haste.png")
labelphoto=Label(middleFrame, image = photo2)
labelphoto.grid(row=0,column=2,padx=20)
B5 = Button(middleFrame, text ="play",command = playMusic3)
B5.grid(row=1,column=2,sticky=W,padx=30)
B6 = Button(middleFrame, text ="stop", command = stopMusic3)
B6.grid(row=1,column=2,sticky=E,padx=30)
photo3=PhotoImage(file="hue bechain.png")
labelphoto=Label(middleFrame, image = photo3)
labelphoto.grid(row=0,column=3,padx=20)
B7 = Button(middleFrame, text ="play",command = playMusic4)
B7.grid(row=1,column=3,sticky=W,padx=30)
B8 = Button(middleFrame, text ="stop", command = stopMusic4)
B8.grid(row=1,column=3,sticky=E,padx=30)
photo4=PhotoImage(file="humsafar.png")
labelphoto=Label(middleFrame, image = photo4)
labelphoto.grid(row=0,column=4,padx=20)
B9 = Button(middleFrame, text ="play",command = playMusic5)
B9.grid(row=1,column=4,sticky=W,padx=30)
B10 = Button(middleFrame, text ="stop", command = stopMusic5)
B10.grid(row=1,column=4,sticky=E,padx=30)

bottomFrame=LabelFrame(master,text="Recommended songs")
bottomFrame.pack(padx=30,pady=10)
photo5=PhotoImage(file="lagdi na aankh.png")
labelphoto=Label(bottomFrame, image = photo)
labelphoto.grid(row=0,column=0,padx=20)
B11 = Button(bottomFrame, text ="play",command = playMusic6)
B11.grid(row=2,column=0,sticky=W,padx=30)
B12 = Button(bottomFrame, text ="stop", command = stopMusic6)
B12.grid(row=2,column=0,sticky=E,padx=30)
photo6=PhotoImage(file="laavi na.png")
labelphoto=Label(bottomFrame, image = photo1)
labelphoto.grid(row=0,column=1,padx=20)
B11 = Button(bottomFrame, text ="play",command = playMusic7)
B11.grid(row=2,column=0,sticky=W,padx=30)
B12 = Button(bottomFrame, text ="stop", command = stopMusic7)
B12.grid(row=2,column=0,sticky=E,padx=30)
photo7=PhotoImage(file="man mera.png")
labelphoto=Label(bottomFrame, image = photo2)
labelphoto.grid(row=0,column=2,padx=20)
B11 = Button(bottomFrame, text ="play",command = playMusic8)
B11.grid(row=2,column=0,sticky=W,padx=30)
B12 = Button(bottomFrame, text ="stop", command = stopMusic8)
B12.grid(row=2,column=0,sticky=E,padx=30)
photo8=PhotoImage(file="saanson ko.png")
labelphoto=Label(bottomFrame, image = photo3)
labelphoto.grid(row=0,column=3,padx=20)
B11 = Button(bottomFrame, text ="play",command = playMusic9)
B11.grid(row=2,column=0,sticky=W,padx=30)
B12 = Button(bottomFrame, text ="stop", command = stopMusic9)
B12.grid(row=2,column=0,sticky=E,padx=30)
photo9=PhotoImage(file="time table2.png")
labelphoto=Label(bottomFrame, image = photo4)
labelphoto.grid(row=0,column=4,padx=20)
B11 = Button(bottomFrame, text ="play",command = playMusic10)
B11.grid(row=2,column=0,sticky=W,padx=30)
B12 = Button(bottomFrame, text ="stop", command = stopMusic10)
B12.grid(row=2,column=0,sticky=E,padx=30)

mainloop()
