from abc import ABC, abstractmethod

class NotificationHandler(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailHandler(NotificationHandler):
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMSHandler(NotificationHandler):
    def send(self, message):
        print(f"Sending SMS: {message}")

class WhatsAppHandler(NotificationHandler):
    def send(self, message):
        print(f"Sending WhatsApp: {message}")

class Logger:
    def log(self, message):
        print("Logging:", message)

class Database:
    def save(self, message):
        print("Saving to DB:", message)

class NotificationService:
    def __init__(self, handler, logger, database):
        self.handler = handler
        self.logger = logger
        self.database = database
    
    def send(self, message):
        self.handler.send(message)
        self.logger.log(message)
        self.database.save(message)

# Usage
email_handler = EmailHandler()
logger = Logger()
db = Database()

service = NotificationService(email_handler, logger, db)
service.send("Hello World")