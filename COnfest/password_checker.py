from password_validator import PasswordValidator


schema = PasswordValidator()
schema.min(8).max(100)
schema.has().uppercase()
schema.has().lowercase()
schema.has().digits()
schema.has().symbols()
schema.no().spaces()

def is_valid_password(password):
    a=schema.validate(password)
    if a is True:
        return "Valid Password"
    else:
        return "Invalid Password"




