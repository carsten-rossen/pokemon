#!/usr/bin/python3

# Script Name: Web Application Fingerprinting Part 2 of 3
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 5/25/21 
# Purpose: Return the cookie from a site that supports cookies.


# import libraries
import requests
import webbrowser

# targetsite = input("Enter target site:")
targetsite = "http://www.whatarecookies.com/cookietest.asp" 
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

response2 = requests.get(targetsite, cookie)
html_file = open("response.html", "w")
html_file.write(str(response2.content))
html_file.close()

webbrowser.open_new_tab("./response.html")


# End
