from tkinter import *
from gtts import gTTS
from threading import Thread
from playsound import playsound
from time import perf_counter



rootWindow = Tk()
rootWindow.resizable(0, 0)
rootWindow.title('Test To Speech')



def saveAssistant(message):
    speaker = str(perf_counter()) + ".mp3"
    instruction = gTTS(message, lang = 'en')
    instruction.save(speaker)
    playsound(speaker)

def speak(message):

    saveAssistant(message)
    
def speakThread():

    Thread(target = speak, args = (testBox.get("1.0",END),)).start()
    
#Frame that contains all the elements of the User Interface
mainFrame = Frame(rootWindow, height = 500, width = 500 , relief = SUNKEN , bg = '#ffffff')
mainFrame.pack()

testBox = Text(mainFrame, width = 45, height = 10, relief = FLAT,  font = ('calibri' , 12), bg = '#e4e4e4', padx = 5, pady = 5)
testBox.place(x = 70, y = 100)
speakButton = Button(mainFrame , width = 18,  font = ('Aerial' , 14, 'bold') , text = 'Speak' , command = speakThread, relief = FLAT , highlightthickness=4 , fg = "#ffffff", bg="#4d96f6" )
speakButton.place(x = 135 , y = 350)

rootWindow.mainloop()