import uuid


class Config(object):
    def __init__(self):
        self.SECRET_KEY = uuid.uuid4().hex

        # MONGODB configs
        self.MONGODB_DB = 'panorama'
        self.MONGODB_HOST = 'localhost'
        self.MONGODB_PORT = 27017

        # GMAIL SMTP configs
        self.DEFAULT_MAIL_SENDER = 'Admin < satyajeetnim@gmail.com >'
        self.MAIL_SERVER = 'smtp.gmail.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = 'XXXXXXXXXXX'
        self.MAIL_PASSWORD = 'XXXXXXXXXXX'

        # Flask-Security configs
        self.SECURITY_EMAIL_SENDER = 'Panorama < security@panorama.com >'
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
        self.SECURITY_REGISTERABLE = True
        self.SECURITY_RECOVERABLE = True
        #self.SECURITY_URL_PREFIX = '/auth'
        self.SECUIRTY_POST_LOGIN = '/'
        self.SECURITY_PASSWORD_HASH = 'sha512_crypt'
        self.SECURITY_PASSWORD_SALT = uuid.uuid4().hex
        self.SECURITY_CONFIRMABLE = True
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

panorama_config = Config()