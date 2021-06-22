# complete tool with cmd line interface for more advanced users

# author : falkensmaze (c0m3t-k2)

# project code name : coyote

import twint
from datetime import datetime
import os
import sys

print()
print(r"""████████╗██╗    ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
╚══██╔══╝██║    ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
   ██║   ██║ █╗ ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
   ██║   ██║███╗██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
   ██║   ╚███╔███╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   

@c0m3t-k2 / falkensmaze                                                          

""")
print("twosint - v. 2.0.0")
print()
username = input("twosint~# Before we start the investigation, please enter your target's username -> ")
print("twosint~# Please enter 'help' if you are stuck!")

def usernameSearch():
    today = datetime.now().strftime('%Y-%m-%d')

    c = twint.Config()
    c.To = username
    c.Since = today
    c.Followers = True
    c.Hide_output = True
    c.Store_object = True

    twint.run.Search(c)

    tweets = twint.output.tweets_list

    followers = []

    for tweet in tweets:
            followers.append(('{}'.format(tweet.username)))

    print(followers)

    for user in followers:
            c = twint.Config
            c.Username = user
            c.Limit = 18
    twint.run.Search(c)


def keyHunter():
    limit = input("twosint~# Enter a limit of tweets :")
    keyword = input("twosint~# Enter keyword : ")
    print("twosint~# Searching ...")
    c = twint.Config()
    c.Limit = limit
    c.Search = keyword
    twint.run.Search(c)

def mailHunter():
    print()
    print("twosint~# Gathering possible emails ...")
    print()
    
    c = twint.Config()
    c.Username = username
    c.Email = True
    twint.run.Search(c)

def numHunter():
    print()
    print("twosint~# Gathering possible phone numbers ...")
    print()

    c = twint.Config()
    c.Username = username
    c.Phone = True
    twint.run.Search(c)

def followHunter():
    print()
    limit = input("twosint~# Please enter a limit of followers : ")

    c = twint.Config()
    c.Username = username
    c.Followers == True
    c.Limit = limit
    c.User_full == True

    twint.run.Search(c)

def whoHunter():
    print()
    limit = input("twosint~# Please enter a limit of users : ")
    c = twint.Config()
    c.Username = username
    c.Limit = limit

    twint.run.Following(c)

def soloInvestigation():
    print()
    c = twint.Config()
    c.Username = username
    
    twint.run.Lookup(c)

# project code name : coyote

def infoUsernameSearch():
    print(r"""
    usernameSearch - module number 0:
    This module allows you to gather the usernames of your
    target's followers. Just enter a limit to not crash the 
    program , and you are good to go!""")

def infoKeyHunter():
    print(r"""
    keyHunter - module number 1 :
    This module allows you to search for a specific word
    in your target's tweets. Enter the word and if everything
    goes as planned, you should gather your tweets.""")

def infoMailHunter():
    print(r"""
    mailHunter - module number 2 :
    This module allows you to gather possible emails from your
    target's tweets. The way it works is that it searches for
    specific keywords such as "email" or "mail" .""")

def infoNumHunter():
    print(r"""
    numHunter - module number 3 :
    This module allows you to gather possible phone numbers
    from your target's tweets. The way it works is that it
    searches for specific keywords such as "phone number" or
    "cellphone".""")

def infoFollowHunter():
    print(r"""
    followHunter - module number 4 :
    This module allows you to gather a lot of information on
    your target's followers. It uses a technique that firstly
    scrapes the target's followers usernames and then it investigates
    their profiles.""")

def infoWhoHunter():
    print(r"""
    whoHunter - module number 5 :
    This module allows you to gather the usernames of the 
    people that your target is following. Unlike followHunter,
    this module only scrapes the usernames and it does not
    investigate them!""")

def infoSoloInvestigation():
    print(r"""
    soloInvestigation - module number 6 :
    This module allow you to investigate your
    target by all means. It scrapes their bio, current tweets,
    followers , following etc. """)

def introduction():
    choice = input("twosint~# ")
    if choice == 'help':
        print(r"""
                    twosint - version 2.0.2 Alpha Release
            
            version                     - displays current version
            clear                       - clears the screen
            exit                        - exit
            modulebomb                  - shows all modules
            username                    - shows current set username
            run [module name / module number]  - runs the chosen module
            info [module name / module number] - get more information on a specified module
        """)
        introduction()
    if choice == 'version':
        print("twosint~# twosint - version 2.0.2 Alpha Release")
    if choice == 'clear':
        os.system("clear")
    if choice == 'exit':
        print("twosint~# Exitting ...")
        quit()
    if choice == 'modulebomb':
        print()
        print(r"""
        
        0 - usernameSearch              [get usernames of your target's followers]
        1 - keyHunter                   [get tweets that only have your chosen keyword in them]
        2 - mailHunter                  [search for potential emails]
        3 - numHunter                   [search for potential phone numbers]
        4 - followHunter                [get a lot of information on target's followers]
        5 - whoHunter                   [who is your target following]
        6 - soloInvestigation           [get current stats and more on your tareget]
        
        """)
        print()
        introduction()
    if choice == 'username':
        print("twosint~#", username)
        introduction()
    if choice == 'run usernameSearch' or choice == 'run 0':
        print()
        usernameSearch()
    if choice == 'run 1' or choice == 'run keyHunter':
        print()
        keyHunter()
    if choice == 'run 2' or choice == 'run mailHunter':
        print()
        mailHunter()
    if choice == 'run 3' or choice == 'run numHunter':
        print()
        numHunter()
    if choice == 'run 4' or choice == 'run followHunter':
        print()
        followHunter()
    if choice == '5' or choice == 'run whoHunter':
        print()
        whoHunter()
    if choice == 'run 6' or choice == 'run soloInvestigation':
        print()
        print("twosint~# Running the soloInvestigation module ... ")
        soloInvestigation()
    if choice == 'info 0' or choice == 'info usernameSearch':
    	print()
    	infoUsernameSearch()
    	print()
    if choice == 'info 1' or choice == 'info keyHunter':
    	print()
    	infoKeyHunter()
    	print()
    if choice == 'info 2' or choice == 'info mailHunter':
    	print()
    	infoMailHunter()
    	print()
    if choice == 'info 3' or choice == 'info numHunter':
    	print()
    	infoNumHunter()
    	print()
    if choice == 'info 4' or choice == 'info followHunter':
    	print()
    	infoFollowHunter()
    	print()
    if choice == 'info 5' or choice == 'info whoHunter':
    	print()
    	infoWhoHunter()
    	print()
    if choice == 'info 6' or choice == 'info soloInvestigation':
    	print()
    	infoSoloInvestigation()
    	print()
    else:
        introduction()

introduction()

# project code name : coyote
