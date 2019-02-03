print("Sign up now!")

x = input("Enter your email: ")
y = input("Enter your password: ")

print("Registration successful!")

print("Sign in")
tries = 0
while tries < 3:
    a = input("Enter email: ")
    b = input("Enter password: ")
    if x == a and y == b:
        print("Login succcessful!")
        break
    else:
        print("Email or password incorrect!")
    tries += 1
    if tries == 3:
        print("Exceeded login attempts!")

