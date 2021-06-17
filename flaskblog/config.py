
import os


class Config:
    SECRET_KEY = '363d0f6a98dc512a6480a7de1c9cec29'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = 'joshpillai10@gmail.com'
    MAIL_PASSWORD = '09880312231'