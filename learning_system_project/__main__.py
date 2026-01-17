from LearningSystem.learning_system_project.app.auth_flow import reg_or_log_user
from LearningSystem.learning_system_project.app.navigation import access_learning
from LearningSystem.learning_system_project.messaging.printer import authentication_failure, greet_user

# TODO: There should be a dictionary containing all labels - future i18n
# TODO: Tests should be added - "System that does not contain tests is broken by design".

# Navigation
def main():
    """
    TODO: (4)
    Configuration:
        (1) re-write the whole program using Classes or in Django
    Authentication:
        (1) add more extensions for the email
    """
    greet_user()

    # Register and or login the user
    if reg_or_log_user():
        access_learning()
    else:
        authentication_failure()

if __name__ == '__main__':
    main()
