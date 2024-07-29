

import pyttsx3

text = pyttsx3.init()







if __name__ == '__main__':  #starting of the program
    print("welcome to robo speaker")
    print("Pround creation of Anshumaan")
    while(True):
        x = input("what do you    want to pronounce ")
        if(x=="END"):
            break
        text.say(x)
        text.runAndWait()



