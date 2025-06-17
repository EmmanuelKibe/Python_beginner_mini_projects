#Ask the user to input their phone number
phone_number = input("Input your phone number: ")
    
if len(phone_number) < 10:
    print("Phone number is too short")
elif len(phone_number) > 10:
    print("Phone number is too long")
elif not (phone_number.startswith('07') or phone_number.startswith('01')):
    print("Phone number should start with '07' or '01'")
else:
     print(f"Your phone number: {phone_number} is valid")