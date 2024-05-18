# URLInPython Version 1.5

import os
import time
import webbrowser

def main():
    os.system('clear')
    print("URLInPython Version 1.5")
    print("©Edward Samuel 2024. All rights reserved.")
    print("---------------------------------------------------------------------------")
    print("What do you want to do?")
    print("1. Use URLInPython")
    print("2. Exit")
    print("---------------------------------------------------------------------------")
    select = int(input("Select VALID Option: "))
    if (select == 1):
        url()
    elif (select == 2):
        os.system('clear')
        print("Exiting...")
        time.sleep(2)
        os.system('clear')
    else:
        print("Option not valid. Please try again.")
        main()

def url():
    os.system('clear')
    print("URLInPython Version 1.5")
    print("©Edward Samuel 2024. All rights reserved.")
    print("---------------------------------------------------------------------------")
    link = input("Enter the URL (Make sure to include <<https://>> or <<http://>>): ")
    time.sleep(2)
    os.system('clear')
    print("Redirecting to " + link)
    time.sleep(3)
    webbrowser.open(link)
    time.sleep(1)
    os.system('clear')
    main()


main()
