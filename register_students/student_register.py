# ********************************** 10-039 IO OPERATIONS ************************************

# ********************************** AUTO GRATED TASK 1 **************************************
# Write a program that allows a user to register students for an exam venue. 
# First, ask the user how many students are registering.
# Create a for loop that runs for that number of students.
# Each time the loop runs the program should ask the user to enter the next student ID number.
# Write each of the ID numbers to a text file called reg_form.txt.
# Include a dotted line after each student ID because this document will be used as an 
# attendance register, which the students will sign when they arrive at the exam venue.


# ===== Function for registering the ID numbers for an exam venue ============================


def register_student_ID() -> None:
    """Register the student ID
    """

    # Check if the number is an integer
    try:
        # ===== User enter the number of students ============================================
        number_students = int(input("Enter the number of students registered: "))

        # ===== Open the file for writing ====================================================
        with open("reg_form.txt", "w+", encoding = "utf-8") as file:
            file.write("List of students ID" + "\n\n")

            for index in range(number_students):      # iterate through the number of students
                student_ID = input(f"Enter the next ID number for student {index + 1}: ")
                file.write(student_ID + "." * 50  + "\n\n")
        
        print(f"\n{number_students} ID numbers have been successfully registered.\n")

    except Exception as e:
        print("\nInvalid number! Please enter a integer number.")
        print(f"An error occured: {e}\n")


# ===== Execution ============================================================================
if __name__ == "__main__":
    register_student_ID()

# ************************************* END OF CODE ******************************************