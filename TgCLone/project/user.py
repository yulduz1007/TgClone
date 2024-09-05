from dataclasses import dataclass
from db.servise import DbService
from utils import random_code
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@dataclass
class User(DbService):
    id: int = None
    phone_number: str = None
    email: str = None
    first_name: str = None
    last_name: str = None
    username: str = None
    photo: str = None
    is_premium: bool = False
    bio: str = None

    def sequence_id(self):
        users: list[User] = self.objects()
        return int(users[-1].id) + 1 if users else 1

    def is_valid(self):
        users: list[User] = self.objects()
        for user in users:
            if user.phone_number == self.phone_number:
                raise Exception(f"{self.phone_number} , Already Exists phone number")
            elif user.username == self.username:
                raise Exception(f"{self.phone_number} , Already Exists username")

    def save(self):
        users: list[User] = self.objects()
        users.append(self)
        self.write(users)

    @staticmethod
    def sendemail_code(receiver_email):
        code = str(random_code())

        sender_email = "absaitovdev@gmail.com"
        password = "wuiswkcyupsufjum"

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email


        html = f"""
            Hi,
            How are you?
            code : {code}
        """
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        return code

    def is_login(self):
        users: list[User] = self.objects()
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.sendemail_code(user.email)
                user_code = input("code :")
                if code == user_code:
                    return user
                else:
                    raise Exception(f"{self.phone_number} , Invalid code")
        raise Exception("Not Found phone number")
