marks = float(input("Enter the student's exam score: "))

if marks >= 35:
    print("Status: Passed!")
    
    if marks > 90:
        print("Congratulations! You have qualified for a scholarship.")
    else:
        print("Keep up the good work (No scholarship awarded).")
        
else:
    print("Status: Failed. Try again next time!")
