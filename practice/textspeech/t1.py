import pyttsx3

Text_speech=pyttsx3.init()
k=input("what would you to speck : ")
answer="hello , my name is vaghela ajitkumar vishunubhai i am from government engineering collage rajkot"

Text_speech.say(k)
Text_speech.runAndWait()

