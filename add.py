def student(email,grade):
    if email.endswith("@gmail.com"):
        if (grade) == ("A"):
            return "registation Successfully"
        else:
            return "registration Failed"
    else:
        print("Invalid email")
student('email','grade')
