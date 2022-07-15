def encrypt():
  message = input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt")
  ascii_message = [ord(char)-3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = 1
while flag < 2:
  choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \n 3.Exit!")
  if choice == '1':
     encrypt()
  elif choice == '2':
     decrypt() 
  elif choice=="3":
        print("You Are exit")
        break
  else:
        print("not valid")