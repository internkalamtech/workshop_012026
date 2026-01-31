from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotificationService(NotificationService):
    def send(self, message):
        print(f"Sending email notification with message: {message}")

class SMSNotificationService(NotificationService):
    def send(self, message):
        print(f"Sending SMS notification with message: {message}")

class WhatsappNotificationService(NotificationService):
    def send(self, message):
        print(f"Sending WhatsApp notification with message: {message}") 

class Logger:
    def log(self, message):
        print(f"Log entry: {message}")

class Database:
    def save(self, message):
        print(f"Saving message to database: {message}")

class Notificationservice:
    def __init__(self, notification_service: NotificationService, logger: Logger, database: Database):
        self.notification_service = notification_service
        self.logger = logger
        self.database = database

def Send(self, message):
        self.notification_service.send(message)
        self.logger.log(message)
        self.database.save(message)
                        
