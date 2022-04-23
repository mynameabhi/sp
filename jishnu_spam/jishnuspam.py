a='\033[31m'
lgreen = '\033[92m'

bold = '\033[01m'
print(a+bold+"""

░░░░░██╗██╗░██████╗██╗░░██╗███╗░░██╗██╗░░░██╗
░░░░░██║██║██╔════╝██║░░██║████╗░██║██║░░░██║
░░░░░██║██║╚█████╗░███████║██╔██╗██║██║░░░██║
██╗░░██║██║░╚═══██╗██╔══██║██║╚████║██║░░░██║
╚█████╔╝██║██████╔╝██║░░██║██║░╚███║╚██████╔╝
░╚════╝░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░""")
print("                                    ")


print(lgreen+bold+"                    this is created by jishnu")
print("                       ")
print("""tool will be update soon""")


print("  ")






####_____________________________________________________________________________-

import webbrowser
import time


import pyautogui





spm=int(input(a+bold+"enter spam range : "))


aa=str(input("enter the text : "))
aa2=str(input("enter the text : "))
tx=str(aa)
tx2=str(aa2)
# time.sleep(3)
####------------open website here----------------------------------------

a='\033[31m'
b = '\033[01m'

print(a+"press",b+"1","for",b+"instagram",)
print(a+"press",b+"2", "for", b+"facebook")
site=str(input("open website by writing : "))    




    #######_________________________________________----
if site is '1':
    webbrowser.open("https://www.instagram.com/direct/inbox/")
if site is '2':
    webbrowser.open("https://www.facebook.com/")

time.sleep(30)

for i in range(spm):

    pyautogui.write(tx)
    pyautogui.press("enter")
  
    pyautogui.write(tx2)
    pyautogui.press("enter")

print("great u have done")
    


   
  
