def strengthCheck(password):
    import string
    capital_char = set(string.ascii_uppercase)
    special_char = set(string.punctuation)
    numbers = set(string.digits)
    minimum = 8
    count = 0
    requirements = {"capital":False, "special":False, "number":False, "length":False, }

    if len(password) >= minimum:
        requirements["length"] = True

    for char in password:
        if char in capital_char:
            requirements["capital"] = True
        elif char in special_char:
            requirements["special"] = True
        elif char in numbers:
            requirements["number"] = True
    
    for k in requirements:
        if requirements[k] == True:
            count += 1
    
    if count <= 2:
        print ("weak.")
    elif count == 3:
        print ("ok?")
    else:
        print("strong!")    
    