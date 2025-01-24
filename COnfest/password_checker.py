# from password_validator import PasswordValidator
#
#
# schema = PasswordValidator()
# schema.min(8).max(100)
# schema.has().uppercase()
# schema.has().lowercase()
# schema.has().digits()
# schema.has().symbols()
# schema.no().spaces()
#
# def is_valid_password(password):
#     a=schema.validate(password)
#     if a is True:
#         return "Valid Password"
#     else:
#         return "Invalid Password"
#

from password_validator import PasswordValidator

# Define the password validation schema
schema = PasswordValidator()
schema.min(8).max(100)  # Password must be between 8 and 100 characters
schema.has().uppercase()  # Must have at least one uppercase letter
schema.has().lowercase()  # Must have at least one lowercase letter
schema.has().digits()  # Must have at least one digit
schema.has().symbols()  # Must have at least one symbol
schema.no().spaces()  # Must not have spaces

def is_valid_password(password):
    # Validate the password and get detailed errors if invalid
    if schema.validate(password):
        return "Valid Password"
    else:
        # Get the list of validation errors
        errors = schema.validate(password, details=True)
        error_messages = [str(error) for error in errors]
        return f"Invalid Password: {', '.join(error_messages)}"


password = "Password@123"
print(is_valid_password(password))


