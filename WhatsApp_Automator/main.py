import pywhatkit
number = input("Enter the number: ")
message = input("Enter the message: ")
time = input("Enter the time: ")
#specify time in the form of HH:MM
pywhatkit.sendwhatmsg(number, message, int(time.split(":")[0]), int(time.split(":")[1]))
#//will send a whatsapp message to the number upon running the code in the time specified
