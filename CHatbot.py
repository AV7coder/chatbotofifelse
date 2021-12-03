# Friend 6
from datetime import date


from datetime import datetime

import os
import sys
import time
import webbrowser
import googlesearch
import wikipedia
userquery = input("Hello, What can I do for you? :")
while True:
    if "time" in userquery:
        now = datetime.now()
        print("The time is {}.".format(now))
        userquery = input("Hello, What can I do for you? :")

    elif "safe from coronavirus" in userquery:
        print("Wash hands regularly , Wear mask , Maintain social distancing and download Arogya Setu App.")
        userquery = input("Hello, What can I do for you? :")

    elif "who are you" in userquery:
        print("I am an AI called Friend designed by Aaditya Vyas of Class 6th-E.")
        userquery = input("Hello, What can I do for you? :")  

    elif "tell a joke" in userquery:
        print("While half time in a football match, the captain said to a player pass the ball to me. The player replied I don't get it, Captain yelled EXACTLY! ")
        userquery = input("Hello, What can I do for you? :")  

    elif "convert kilometer into miles" in userquery:
        kilometers = float(input("Enter value in kilometers: "))
        conv_fac = 0.621371
        miles = kilometers * conv_fac
        print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles)) 
        userquery = input("Hello, What can I do for you? :")

    elif "convert miles into kilometer" in userquery:
        miles = float(input("Enter value in miles: "))
        conv_fac = 0.621371
        kilometers = miles / conv_fac
        print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
        userquery = input("Hello, What can I do for you? :") 

    elif "calculator" in userquery:
        num1 = float(input("ENTER FIRST NUMBER:")) # for input 
        num2 = float(input("ENTER SECOND NUMBER: "))
        operator = input("ENTER OPERATOR: ")
        sum = num1 + num2 #         M
        difference = num1 - num2 #  A   
        quotient = num1 / num2 #    I
        product = num1 * num2 #  
        if operator == ("+"):
            print(sum)
            userquery = input("Hello, What can I do for you? :") 
        elif "*" in operator:
            print(product)  
            userquery = input("Hello, What can I do for you? :") 
        elif "-" in operator:
            print(difference)
            userquery = input("Hello, What can I do for you? :")  
        elif "/" in operator:
            print(quotient)
            userquery = input("Hello, What can I do for you? :") 
        else:
            print("Type a valid operator")
            userquery = input("Hello, What can I do for you? :") 

    elif "open scratch" in userquery:
        print("Ok") 
        webbrowser.open('https://www.scratch.mit.edu', new=2)
        userquery = input("Hello, What can I do for you? :")  

    elif "open ips website" in userquery:
        print("Sure") 
        webbrowser.open('www.iwsportal.com', new=2)
        userquery = input("Hello, What can I do for you? :")   
        
    elif "open first in math" in userquery:
        print("Sure") 
        webbrowser.open('https://https://www.firstinmath.in/home', new=2)
        userquery = input("Hello, What can I do for you? :")       

    elif "open gmail" in userquery:
        print("Sure")
        webbrowser.open('https://www.gmail.com', new=2)
        userquery = input("Hello, What can I do for you? :") 

    elif "open google" in userquery:
        print("Opening...")
        webbrowser.open('https://www.google.co.in', new=2)
        userquery = input("Hello, What can I do for you? :")

    elif "open youtube" in userquery:
        print("Opening youtube...")
        webbrowser.open("www.youtube.com", new=2)
        userquery = input("Hello, What can I do for you? :")

    elif "you are good" in userquery:
        print("Thank you") 
        userquery = input("Hello, What can I do for you? :")

    elif "you are bad" in userquery:
        print("I am sorry.") 
        userquery = input("Hello, What can I do for you? :")   


    elif "bye" in userquery:
        print(":D Bye")    
        break  

    elif "hi" in userquery:
        userquery = input("Hello, What can I do for you? :")       

    elif "open a website" in userquery:
        while True:
            web = input("ENTER WEB URL: ")
            webbrowser.open(web, new=2)
            userquery = input("Hello, What can I do for you? :")

    elif "open teams" in userquery:
        print("Requirment already satisfied.")
        userquery = input("Hello, What can I do for you? :")    

    elif "wish birthday" in userquery:
        print("Happy Birthday!! :)") 
        userquery = input("Hello, What can I do for you? :") 
        
    elif "search wikipedia" in userquery:
        import wikipedia
        hh = input("What should I search? : ")  
        result = wikipedia.summary(hh, sentences = 2)  
        print(result) 
        userquery = input("Hello, What can I do for you? :")

    elif "open powerpoint" in userquery:
        import os
        powerpoint_path = "D:\\Microsoft + google\\PowerPoint"
        os.startfile(powerpoint_path)
        userquery = input("Hello, What can I do for you? :")

    elif "open word" in userquery:
        import os
        word_path = "D:\\Microsoft + google\\Word"
        os.startfile(word_path)
        userquery = input("Hello, What can I do for you? :")    

    elif "open code" in userquery:
        import os
        code_path = "D:\\Python Programming\\VISUAL CODE\\Visual Studio Code"
        os.startfile(code_path)
        userquery = input("Hello, What can I do for you? :")   

    elif "open a file" in userquery:
        import os
        location = input("ENTER FILE LOCATION : ")
        try:
            print("Opening File.....")
            os.startfile(location)
            
            userquery = input("Hello, What can I do for you? :")
        except:
            print("File not found kindly check the location.")   
            userquery = input("Hello, What can I do for you? :")             

    elif "search on youtube" in userquery:
        print("Sure.") 
        import webbrowser
        hhh = input("What should I search : ")  
        webbrowser.open("https://www.youtube.com/results?search_query={}".format(hhh))
        userquery = input("Hello, What can I do for you? :")


    elif "song" in userquery:
        print("Sure.") 
        import webbrowser 
        webbrowser.open("https://www.youtube.com/results?search_query= Songs")
        userquery = input("Hello, What can I do for you? :")
 

    else:
        try:
            import wikipedia
            
            result = wikipedia.summary(userquery, sentences = 2)  
            print(result) 
            userquery = input("Hello, What can I do for you? :")
        except:    
            from googlesearch import search 
            for j in search(userquery, tld="co.in", num=3, stop=3, pause=2): 
                print(j) 
            print("This what I found on internet.")
            userquery = input("Hello, What can I do for you? :")  
 
