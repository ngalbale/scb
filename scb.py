#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pyttsx3
import os
import datetime
import webbrowser

hour = datetime.datetime.now().hour
print("Welcome!")
if hour < 12:
    pyttsx3.speak("Good morning Sir! Welcome!")
elif hour >= 12 and hour < 17:
    pyttsx3.speak("Good afternoon Sir! Welcome!")
elif hour >=17 and hour < 22:
    pyttsx3.speak("Good evening Sir! Welcome!")
else:
    pyttsx3.speak("Welcome Sir!" )

while True:
    print("Please enter your query:", end='')
    pyttsx3.speak("Please enter your query")
    p = input()
    if (("run" in p) or ("open" in p)):
        if ("chrome" in p):
            os.system("chrome")
        elif ("notepad" in p):
            os.system("notepad")
        elif("google" in p):
            webbrowser.open(r"https://www.google.com/")
        else:
            print("Query Not Supported!")
            pyttsx3.speak("Sorry! I can't support this query at the moment")
        
    elif ("exit" in p) or ("quit" in p):
        print("Bye! Have a great day ahead.")
        pyttsx3.speak("Bye! Have a great day ahead.")
        break
    else:
        print("Query Not Supported!")
        pyttsx3.speak("Sorry! I can't support this query at the moment")


# In[ ]:




