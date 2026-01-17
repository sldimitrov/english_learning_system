from LearningSystem.learning_system_project.constants.options import positive_options, negative_options
from LearningSystem.learning_system_project.database_files.db_testing import login_user, register_user

def reg_or_log_user():
    # TODO: Use some constants for the answers would make sense, as we use them much
    while True:
        answer = input("\nDo you have an existing account? (y/n): ").lower()
        if answer in positive_options:
            if login_user():
                return True
            else:
                break

        elif answer in negative_options:
            # TODO: Add a function for the input and just pass the label
            choice = input("Would you like to create a new account? (y/n): ").lower()

            if choice in positive_options:
                if register_user():
                    print(f'-You were successfully registered!\n')
                    if login_user():
                        return True

                    else:
                        break

            elif choice in negative_options:
                print("\nProgram ends here...")
                raise SystemExit

        # This logic is hard to read
        else:
            if answer:
                print("Unknown answer: " + answer)
            else:
                print("Please input a valid answer")
            continue

    return False
