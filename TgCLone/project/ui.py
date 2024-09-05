from typing import Optional

from log_config import info
from project.user import User
from utils import choose_emoji

current_user: Optional[User] = None


class UI:
    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) Exit
                >>>"""
            match input(menu):
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as message:
            user_msg = str(message).split(",")
            info.info(message)
            print(user_msg)
            self.main()

    def register(self):
        user = {
            "id": User().sequence_id(),
            "phone_number": input("phone_number : "),
            "email": input("Email : "),
            "first_name": input("first_name : "),
            "last_name": input("last_name : "),
            "username": input("username : "),
            "photo": choose_emoji(),
            "bio": input("bio : "),
        }
        user = User(**user)
        user.is_valid()
        user.save()
        print("Success Register")
        self.main()

    def login(self):
        global current_user
        phone = input("Phone number : ")
        auth = User(phone_number=phone)
        current_user = auth.is_login()
        self.account()

    def account(self):

        print(f"Welcome to Telegram account {current_user.first_name} {current_user.last_name}")
