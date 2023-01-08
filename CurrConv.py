import os,time
title='''
░█████╗░██╗░░░██╗██████╗░██████╗░███████╗███╗░░██╗░█████╗░██╗░░░██╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░░██║██████╔╝██████╔╝█████╗░░██╔██╗██║██║░░╚═╝░╚████╔╝░
██║░░██╗██║░░░██║██╔══██╗██╔══██╗██╔══╝░░██║╚████║██║░░██╗░░╚██╔╝░░
╚█████╔╝╚██████╔╝██║░░██║██║░░██║███████╗██║░╚███║╚█████╔╝░░░██║░░░
░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
By Adithya Manjunath (github.com/Cr4zySh4rk/INRCurrencyConverter'''

def clrscr():
    os.system('clear')

print(title)
print("\nConverts Indian Currency i.e Indian National Rupee (INR) to other foreign currencies and vice versa.")
while(True):
    choice=input("\nProceed to convert? (Y/n) : ")
    if (choice=='Y'or choice=='y' or choice==''):
        clrscr()
        print("[1] Convert from INR to foreign currencies.")
        print("[2] Convert from foreign currencies to INR.")
        try:
            choice=int(input("\nEnter your choice : "))
        except:
            print("Invalid Option!")
        if (choice==1):
            clrscr()
            print("[1] Japanese Yen (JPY)")
            print("[2] US Dollar (USD)")
            print("[3] Russian Ruble (RUB)")
            print("[4] UAE Dirham (AED)")
            print("[5] Chinese Yuan (CNY)")
            try:
                foreign=int(input("Enter currency to convert to : "))
                amount=float(input("Enter amount to convert : "))
            except:
                print("Invalid input!")
            if (foreign==1):
                print("Converted amount is : {} JPY".format(1.61*amount))
            elif (foreign==2):
                print("Converted amount is : {} USD".format(0.012*amount))
            elif (foreign==3):
                print("Converted amount is : {} RUB".format(0.88*amount))
            elif (foreign==4):
                print("Converted amount is : {} AED".format(0.045*amount))
            elif (foreign==5):
                print("Converted amount is : {} CNY".format(0.083*amount))
            else:
                print("Invalid Input!")
        elif (choice==2):
            clrscr()
            print("[1] Japanese Yen (JPY)")
            print("[2] US Dollar (USD)")
            print("[3] Russian Ruble (RUB)")
            print("[4] UAE Dirham (AED)")
            print("[5] Chinese Yuan (CNY)")
            try:
                native=int(input("Enter currency to convert from : "))
                amount=float(input("Enter amount to convert : "))
            except:
                print("Invalid input!")
            if (native==1):
                print("Converted amount is : {} JPY".format(0.62*amount))
            elif (native==2):
                print("Converted amount is : {} USD".format(82.27*amount))
            elif (native==3):
                print("Converted amount is : {} RUB".format(1.13*amount))
            elif (native==4):
                print("Converted amount is : {} AED".format(22.40*amount))
            elif (native==5):
                print("Converted amount is : {} CNY".format(12.03*amount))
            else:
                print("Invalid Input!")
        else:
            clrscr()
            print("Invalid input!")
    elif (choice=='N'or choice=='n'):
        print('Exiting...')
        time.sleep(1.5)
        quit()