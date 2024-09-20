import pyttsx3
if __name__ == '__main__':
   
    speech = pyttsx3.init()
    while(True):
        x = input("Enter your command: ")
        if x == 'q':
            break
        speech.say(x)
        speech.runAndWait()