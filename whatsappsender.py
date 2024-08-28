# a=int(input())
# b=int(input())
# c=int(input())
# mulitple=a*b*c
# add=a+b+c
# divide=mulitple/add
# print(divide)

import pywhatkit
# pywhatkit.sendwhatmsg("+91 9942371331", "+91 8870470862", "Hai this is test msg", 8,58, wait_time=10)

# List of phone numbers
phone_numbers = ["+91 9942371331", "+91 8870470862", "+91 9361289991"]

# The message you want to send
message = "Hai, this is a test message."

# Time to send the message (24-hour format)
hour = 9
minute = 2
wait_time = 5  # Optional: Time to wait before sending the message

# Loop through each phone number and send the message
for number in phone_numbers:
    pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time)
    minute += 1  # Increase the minute to avoid sending all at the exact same time
