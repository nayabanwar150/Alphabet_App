from tkinter import*
import pygame
from gtts import gTTS
import os

pygame.init()
root = Tk()
root.title("Alphabet App")
root.geometry('1352x652')
root.configure(background='white')

srt1 = StringVar()
srt1.set("Welcome to Alphabet App")
ABC = Frame(root, bg="white")
ABC.grid()

cont = Canvas(ABC, width = 160, height = 120, bg = "white")
cont.grid(row=3, column=3)
image1 = PhotoImage(file = "icon2.png")
image = cont.create_image(80, 70 , image = image1)

#==================================== functions ============================
imageA = PhotoImage(file = "icon1.png")
def Alphabet_A():
    srt1.set("A for Apple")
    image = cont.create_image(80, 70 , image = imageA)
    tts = gTTS(text= "A is for Apple", lang='en')
    tts.save("Alphabet_A.mp3")
    os.system("start Alphabet_A.mp3")

imageB = PhotoImage(file = "icons.png")
def Alphabet_B():
    srt1.set("B for Ball")
    image = cont.create_image(80, 70 , image = imageB)
    tts = gTTS(text= " B for Ball", lang='en')
    tts.save("Alphabet_B.mp3")
    os.system("start Alphabet_B.mp3")

imageC = PhotoImage(file = "icons.png")
def Alphabet_C():
    srt1.set("C for Cat")
    image = cont.create_image(80, 70 , image = imageC)
    tts = gTTS(text= "C for Cat", lang='en')
    tts.save("Alphabet_C.mp3")
    os.system("start Alphabet_C.mp3")

imageD = PhotoImage(file = "icons.png")
def Alphabet_D():
    srt1.set("D for Doll")
    image = cont.create_image(80, 70 , image = imageD)
    tts = gTTS(text= "D for Doll", lang='en')
    tts.save("Alphabet_D.mp3")
    os.system("start Alphabet_D.mp3")

imageE = PhotoImage(file = "icons.png")
def Alphabet_E():
    srt1.set("E for Elephant")
    image = cont.create_image(80, 70 , image = imageE)
    tts = gTTS(text= "E for Elephant", lang='en')
    tts.save("Alphabet_E.mp3")
    os.system("start Alphabet_E.mp3")

imageF = PhotoImage(file = "icons.png")
def Alphabet_F():
    srt1.set("F for Fox")
    image = cont.create_image(80, 70 , image = imageF)
    tts = gTTS(text= "F for Fox", lang='en')
    tts.save("Alphabet_F.mp3")
    os.system("start Alphabet_F.mp3")

imageG = PhotoImage(file = "icons.png")
def Alphabet_G():
    srt1.set("G for Goat")
    image = cont.create_image(80, 70 , image = imageG)
    tts = gTTS(text= "G for Goat", lang='en')
    tts.save("Alphabet_G.mp3")
    os.system("start Alphabet_G.mp3")


imageH = PhotoImage(file = "icons.png")
def Alphabet_H():
    srt1.set("H for Horse")
    image = cont.create_image(80, 70 , image = imageH)
    tts = gTTS(text= "H for Horse", lang='en')
    tts.save("Alphabet_H.mp3")
    os.system("start Alphabet_H.mp3")

imageI = PhotoImage(file = "icons.png")
def Alphabet_I():
    srt1.set("I for Inkpot")
    image = cont.create_image(80, 70 , image = imageI)
    tts = gTTS(text= "I for Inkpot", lang='en')
    tts.save("Alphabet_I.mp3")
    os.system("start Alphabet_I.mp3")

imageJ = PhotoImage(file = "icons.png")
def Alphabet_J():
    srt1.set("J for Joker")
    image = cont.create_image(80, 70 , image = imageJ)
    tts = gTTS(text= "J for Joker", lang='en')
    tts.save("Alphabet_J.mp3")
    os.system("start Alphabet_J.mp3")

imageK = PhotoImage(file = "icons.png")
def Alphabet_K():
    srt1.set("K for King")
    image = cont.create_image(80, 70 , image = imageK)
    tts = gTTS(text= "K for King", lang='en')
    tts.save("Alphabet_K.mp3")
    os.system("start Alphabet_K.mp3")

imageL = PhotoImage(file = "icons.png")
def Alphabet_L():
    srt1.set("L for Lock")
    image = cont.create_image(80, 70 , image = imageL)
    tts = gTTS(text= "L for Lock", lang='en')
    tts.save("Alphabet_L.mp3")
    os.system("start Alphabet_L.mp3")

imageM = PhotoImage(file = "icons.png")
def Alphabet_M():
    srt1.set("M for Mango")
    image = cont.create_image(80, 70 , image = imageM)
    tts = gTTS(text= "M for Mango", lang='en')
    tts.save("Alphabet_M.mp3")
    os.system("start Alphabet_M.mp3")

imageN = PhotoImage(file = "icons.png")
def Alphabet_N():
    srt1.set("N for Nayab")
    image = cont.create_image(80, 70 , image = imageN)
    tts = gTTS(text= "N for Nayab", lang='en')
    tts.save("Alphabet_N.mp3")
    os.system("start Alphabet_N.mp3")

imageO = PhotoImage(file = "icons.png")
def Alphabet_O():
    srt1.set("O for Orange")
    image = cont.create_image(80, 70 , image = imageO)
    tts = gTTS(text= "O for Orange", lang='en')
    tts.save("Alphabet_O.mp3")
    os.system("start Alphabet_O.mp3")

imageP = PhotoImage(file = "icons.png")
def Alphabet_P():
    srt1.set("P for Plan")
    image = cont.create_image(80, 70 , image = imageP)
    tts = gTTS(text= "P for Plan", lang='en')
    tts.save("Alphabet_P.mp3")
    os.system("start Alphabet_P.mp3")

imageQ = PhotoImage(file = "icons.png")
def Alphabet_Q():
    srt1.set("Q for Queen")
    image = cont.create_image(80, 70 , image = imageQ)
    tts = gTTS(text= "Q for Queen", lang='en')
    tts.save("Alphabet_Q.mp3")
    os.system("start Alphabet_Q.mp3")

imageR = PhotoImage(file = "icons.png")
def Alphabet_R():
    srt1.set("R for Rat")
    image = cont.create_image(80, 70 , image = imageR)
    tts = gTTS(text= "R for Rat", lang='en')
    tts.save("Alphabet_R.mp3")
    os.system("start Alphabet_R.mp3")

imageS = PhotoImage(file = "icons.png")
def Alphabet_S():
    srt1.set("S for Small")
    image = cont.create_image(80, 70 , image = imageS)
    tts = gTTS(text= "S for Small", lang='en')
    tts.save("Alphabet_S.mp3")
    os.system("start Alphabet_S.mp3")

imageT = PhotoImage(file = "icons.png")
def Alphabet_T():
    srt1.set("T for Tree")
    image = cont.create_image(80, 70 , image = imageT)
    tts = gTTS(text= "T for Tree", lang='en')
    tts.save("Alphabet_T.mp3")
    os.system("start Alphabet_T.mp3")

imageU = PhotoImage(file = "icons.png")
def Alphabet_U():
    srt1.set("U for Umberalla")
    image = cont.create_image(80, 70 , image = imageU)
    tts = gTTS(text= "U for Umberalla", lang='en')
    tts.save("Alphabet_U.mp3")
    os.system("start Alphabet_U.mp3")

imageV = PhotoImage(file = "icons.png")
def Alphabet_V():
    srt1.set("V for Van")
    image = cont.create_image(80, 70 , image = imageV)
    tts = gTTS(text= "V for Van", lang='en')
    tts.save("Alphabet_V.mp3")
    os.system("start Alphabet_V.mp3")

imageW = PhotoImage(file = "icons.png")
def Alphabet_W():
    srt1.set("W for Water")
    image = cont.create_image(80, 70 , image = imageW)
    tts = gTTS(text= "W for Water", lang='en')
    tts.save("Alphabet_W.mp3")
    os.system("start Alphabet_W.mp3")

imageX = PhotoImage(file = "icons.png")
def Alphabet_X():
    srt1.set("X for X Max")
    image = cont.create_image(80, 70 , image = imageX)
    tts = gTTS(text= "X for XMax", lang='en')
    tts.save("Alphabet_X.mp3")
    os.system("start Alphabet_X.mp3")

imageY = PhotoImage(file = "icons.png")
def Alphabet_Y():
    srt1.set("Y for Yak")
    image = cont.create_image(80, 70 , image = imageY)
    tts = gTTS(text= "Y for Yak", lang='en')
    tts.save("Alphabet_Y.mp3")
    os.system("start Alphabet_Y.mp3")

imageZ = PhotoImage(file = "icons.png")
def Alphabet_Z():
    srt1.set("Z for Zebra")
    image = cont.create_image(80, 70 , image = imageZ)
    tts = gTTS(text= " Z for Zebra", lang='en')
    tts.save("Alphabet_Z.mp3")
    os.system("start Alphabet_Z.mp3")

imageCLEAR = PhotoImage(file = "icons.png")
def Clear():
    srt1.set("Welcome to Alphabet App")
    image = cont.create_image(80, 70 , image = imageCLEAR)  
    
#==================================== row0 =================================
txtDisplay = Entry(ABC, textvariable = srt1, font=('arial', 44,'bold'), bd =34, width = 39, justify = CENTER)
txtDisplay.grid(row=0, column=0, columnspan=7, pady=1)

#==================================== row1 =================================
btnA = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="A",
                bg="cornSilk", command=Alphabet_A).grid(row=1, column=0)
btnB = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="B",
                bg="cornSilk", command=Alphabet_B).grid(row=1, column=1)
btnC = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="C",
                bg="cornSilk", command=Alphabet_C).grid(row=1, column=2)
btnD = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="D",
                bg="cornSilk", command=Alphabet_D).grid(row=1, column=3)
btnE = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="E",
                bg="cornSilk", command=Alphabet_E).grid(row=1, column=4)
btnF = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="F",
                bg="cornSilk", command=Alphabet_F).grid(row=1, column=5)
btnG = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="G",
                bg="cornSilk", command=Alphabet_G).grid(row=1, column=6)

#==================================== row2 ==================================
btnH = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="H",
                bg="cornSilk", command=Alphabet_H).grid(row=2, column=0)
btnI = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="I",
                bg="cornSilk", command=Alphabet_I).grid(row=2, column=1)
btnJ = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="J",
                bg="cornSilk", command=Alphabet_J).grid(row=2, column=2)
btnK = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="K",
                bg="cornSilk", command=Alphabet_K).grid(row=2, column=3)
btnL = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="L",
                bg="cornSilk", command=Alphabet_L).grid(row=2, column=4)
btnM = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="M",
                bg="cornSilk", command=Alphabet_M).grid(row=2, column=5)
btnN = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="N",
                bg="cornSilk", command=Alphabet_N).grid(row=2, column=6)

#==================================== row3 ==================================
btnO = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="O",
                bg="cornSilk", command=Alphabet_O).grid(row=3, column=0)
btnP = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="P",
                bg="cornSilk", command=Alphabet_P).grid(row=3, column=1)
btnQ = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="Q",
                bg="cornSilk", command=Alphabet_Q).grid(row=3, column=2)
btnR = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="R",
                bg="cornSilk", command=Alphabet_R).grid(row=3, column=4)
btnS = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="S",
                bg="cornSilk", command=Alphabet_S).grid(row=3, column=5)
btnT = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="T",
                bg="cornSilk", command=Alphabet_T).grid(row=3, column=6)

#==================================== row4 ==================================
btnU = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="U",
                bg="cornSilk", command=Alphabet_U).grid(row=4, column=0)
btnV = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="V",
                bg="cornSilk", command=Alphabet_V).grid(row=4, column=1)
btnW = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="W",
                bg="cornSilk", command=Alphabet_W).grid(row=4, column=2)
btnX = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="X",
                bg="cornSilk", command=Alphabet_X).grid(row=4, column=3)
btnY = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="Y",
                bg="cornSilk", command=Alphabet_Y).grid(row=4, column=4)
btnZ = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="Z",
                bg="cornSilk", command=Alphabet_Z).grid(row=4, column=5)
btnCLEAR = Button(ABC, pady=1, bd=4,font=('arial',21,'bold'), width=10, height=3, text="CLEAR",
                bg="cornSilk", command=Clear).grid(row=4, column=6)

root.mainloop()
