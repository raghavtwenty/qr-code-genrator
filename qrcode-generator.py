'''
Application Name: QR Code Generator
Author : Raghav, Kendriya Vidyalaya, Coimbatore. [2021]
Github ID : @raghavtwenty
Created On: July 20, 2021 | Last Modified On: July 20, 2021
Version Info: 1.0
'''


# Importing required libraries
import os
import qrcode 


# input from the user
strin = str(input("\nEnter the string which needs to be converted it into QR Code : "))

# call the qr module and pass the value
img = qrcode.make(strin)

# save the qr code image
img.save(f'{strin}.png','PNG')

# open and display it to the user
os.system(f'open {strin}.png')

# final show
print("\nQR CODE Generation complete.\n")
