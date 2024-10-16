cw = int(input("Enter your score:"))
ex = int(input("Enter your score:"))



#asking user whether they attended class or not

cw_passmark = 17.5
ex_passmark = 17.5
attendance = Yes

#asking user to enter their cw_passmark

if cw >= cw_passmark:
    print("You are legible to do the exam.")

class_attendance = input("Enter attendance status:")

if class_attendance == attendance:
    print("You eligible to do the exam")
    
    if ex_passmark >= ex_passmark:
        print("You are ellegible to attending the next semister.")

    else:
        print("You not ellegible for the next semister.")
