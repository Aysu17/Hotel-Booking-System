from models.user import User
from services.emailService import send_welcome_email
from utils.validationUtils import validate_email, validate_password

class UserController:
    
    @staticmethod
    def register_user(name, email, password):
        if not validate_email(email):
            return "Invalid email format."
        
        if not validate_password(password):
            return "Password must be at least 8 characters long."
        
        existing_user = User.get_user_by_email(email)
        if existing_user:
            return "Email is already registered."
        
        user = User(name, email, password)
        user.save()  # Save user to database
        
        send_welcome_email(email)
        
        return f"Welcome {user.name}, registration successful!"
    
    @staticmethod
    def login_user(email, password):
        user = User.get_user_by_email(email)
        if user and user.check_password(password):
            return f"Welcome back, {user.name}!"
        return "Invalid credentials."

    @staticmethod
    def update_user_profile(user_id, new_name=None, new_email=None):
        user = User.get_user_by_id(user_id)
        if user:
            user.update_profile(new_name, new_email)
            return f"User profile updated for {user.name}."
        return "User not found."
    
    @staticmethod
    def delete_user(user_id):
        user = User.get_user_by_id(user_id)
        if user:
            user.delete()
            return "User account deleted."
        return "User not found."
