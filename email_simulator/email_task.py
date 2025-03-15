# ********************************** 10-029_OOP – Classes *************************************

# ********************************** AUTO GRATED TASK *****************************************
# In this task, we’re going to be creating an email simulator using OOP.
# Create an email class and initialise a constructor that takes in three arguments
# (email_address, subject_line, email_content)
# Implement an instance method called mark_as_read() that sets the has_been_read 
# instance variable to "True". 
# Initialise an empty variable called inbox of type list to store and access the email objects.
# Implement a populate_inbox() function that creates an email object with the email address, 
# subject line, and contents, and stores it in the inbox list.
# Implement a list_emails() function that prints each email’s subject_line and an index.
# Implement a read_email() function that displays a selected email, with the email_address, 
# subject_line, and email_content, and then sets its has_been_read instance variable to True.
# Implement a view_unread_emails() function that displays all unread Email object subject lines
# Ask the user to choose an option (1. Read an email 2. View unread emails 3. Quit application)


# ===== Email Class ===========================================================================
class Email:
    """
    A class representing emails.

    Attributes:
        email_address (str): The email address of the sender.
        subject_line (str): The subject line of the email.
        email_content (str): The contents of the email.
        has_been_read (bool): Mark if the email has been read or not

    Methods:
        __init__(email_address, subject_line, email_content):
            Initializes an email instance.

        mark_as_read():
            Sets the has_been_read instance variable to "True".
    """

    # Constructor method with instance variables email_address, subject_line, email_content
    def __init__(self, email_address, subject_line, email_content):
        """initialise the instance variables.
        """
        self.email_address = email_address      
        self.subject_line = subject_line        
        self.email_content = email_content      
        self.has_been_read = False              # initialised to "False"


    # An instance method that sets the has_been_read instance variable to "True".
    def mark_as_read(self):
        """An instance method that sets the has_been_read instance variable to "True"
        """
        self.has_been_read = True


#  Initialize an empty variable of type list to store and access the email objects.
inbox = []


# ===== A function that creates an email object ===============================================
def populate_inbox():
    """Create an email object with the email address, subject line, and contents, and stores it
    """

    # Create 3 sample emails and add them to the inbox list.
    sample_email = [
        Email("fonkoutchinmouo@yahoo.fr", "Welcome to HyperionDev!", 
              "We're absolutely thrilled to announce that you've been accepted into our fully funded  Skills Bootcamp"),
        Email("eddy_murply9@yahoo.com", "Great work on the bootcamp!", 
              "You're doing great! Well done on being in line with your expected progression."),
        Email("eddylarson6@gmail.com", "Your excellent marks!", 
              "Fantastic holiday program! Your code is commendable, and demonstrates a strong understanding of functions.")
    ]
    inbox.extend(sample_email)
    

# ===== A function that prints each email's subject line ======================================
def list_emails():
    """Function that prints each email's subject_line and a corresponding number in the inbox.
    """

    print("\nIndex \tsubject lines")
    [print(f"{index} \t {email.subject_line}") for index, email in enumerate(inbox)]


# ===== A function that displays a selected email =============================================
def read_email():
    """ Function that displays the email_address, subject_line, and email_content 
        attributes for the selected email.
    """

    # check the ValueError
    try:
        # Choose the email index to be read
        index = int(input("Enter the email index to be read: "))

        # Check if email exists
        if 0 <= index < len(inbox):
            email = inbox[index]

            print(f"\nEmail from {email.email_address}\nsubject_line: {email.subject_line}")
            print(f"email_content: {email.email_content}")
            print(f"\nEmail from {email.email_address} marked as read.")

            email.mark_as_read()   # Mark "True", the email has been read
        else:
            print("\nSorry! This email index don't exist in the inbox")

    except ValueError:
        print("\nSorry! Invalid input. Please try again!")
    
    
# ===== A function that displays all unread Email object subject lines ========================
def view_unread_emails():
    """A function that displays all unread Email object subject lines. The list of 
        displayed emails should update as emails are read
    """

    print("\nAll unread Email: \nIndex \tsubject lines")
    
    [print(f"{index} \t{email.subject_line}") for index, email in enumerate(inbox) 
     if not email.has_been_read] 


# ===== Main function to the application ======================================================
def main():
    """Main function to the Email Simulator.
    """

    print("\nWelcome to the application called Email Simulator!")

    # Called a function that creates an email object
    populate_inbox()
    
    while True:
        # Display the menu options for each iteration of the loop.
        print("\nWould you like to: \n1. Read an email \n2. View unread emails \n3. Quit application")
        
        # check the ValueError
        try:
            # Ask the user to choose an option
            user_choice = int(input("Enter selection: "))

            if user_choice == 1:
                # Call the function that prints each index and email's subject line
                list_emails()
                
                # Call yhe function that displays a selected email
                read_email()

            elif user_choice == 2:
                # Call the function that displays all unread Email object subject lines
                view_unread_emails()

            elif user_choice == 3:
                # Quit application
                print("\nExiting the application. See you soon!\n")
                break

            else:
                print("\nOops - incorrect input. Please try again!")

        except ValueError:
            print("\nSorry! Invalid input. You have not entered an integer. Please try again!")


# ===== Execution ============================================================================
if __name__ == "__main__":
    main()

# ******************************** END OF CODE ***********************************************