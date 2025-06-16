def password_strength_check(password):
    special_chars = {'!', '@', '#', '$', '%', '&', '*'}
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    characters = set(password)
    
    has_length = len(password) >= 8
    has_special = bool(special_chars.intersection(characters))
    has_digit = bool(nums.intersection(characters))
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)

    # Check each condition
    if has_length:
        print("✅ Has at least 8 characters")
    else:
        print("❌ Password must have at least 8 characters")

    if has_special:
        print("✅ Contains a special character")
    else:
        print("❌ Must include at least one special character (!, @, #, etc.)")

    if has_digit:
        print("✅ Contains a number")
    else:
        print("❌ Must include at least one number")

    if has_upper:
        print("✅ Contains an uppercase letter")
    else:
        print("❌ Must include at least one uppercase letter")

    if has_lower:
        print("✅ Contains a lowercase letter")
    else:
        print("❌ Must include at least one lowercase letter")

    # Overall strength
    score = sum([has_length, has_special, has_digit, has_upper, has_lower])
    if score == 5:
        print("\n🔒 Strong password!")
    elif score >= 3:
        print("\n⚠️ Moderate password. Consider making it stronger.")
    else:
        print("\n❌ Weak password. Please try again.")

# Example use
password = input("Input your password: ")
password_strength_check(password)
