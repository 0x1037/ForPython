dictionary = {}

turn = False
while turn == False:
    # ask to enter the name 
    student = input("Enter your name: ")
    # ask to enter the grade
    grade = input("Enter your grade: ")

    dictionary[student] = grade
    print(dictionary)

    # ask if you want to add more students
    another = input("You want to add another student? (y or n)")
    if another == "y":
        pass
    else:
        turn = True