from gtts import gTTS
import os


language='en'

print("welcome to robo speaker")
print("Proud creation of Anshumaan")
while(True):
     x = input("what do you  want to pronounce ")
     my_text = f"text is this  {x}"
     if(x=="END"):
        break

myobj=gTTS(text= my_text, lang=language, slow = False)
myobj.save("speech.mp3")
os.system("mpg321 speech.mp3")



