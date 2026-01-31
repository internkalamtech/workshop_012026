# Sender interfaces (one responsibility each)

class NotificationSender:
    def send(self, message):
        pass


class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Sending EMAIL: {message}")


class SmsSender(NotificationSender):
    def send(self, message):
        print(f"Sending SMS: {message}")


class WhatsAppSender(NotificationSender):
    def send(self, message):
        print(f"Sending WhatsApp: {message}")


# Logger

class Logger:
    def log(self, message):
        print("Logging:", message)


# Database saver

class Database:
    def save(self, message):
        print("Saving to DB:", message)


# Notification service (simple and clean)

class NotificationService:
    def __init__(self, sender, logger, database):
        self.sender = sender
        self.logger = logger
        self.database = database

    def notify(self, message):
        self.sender.send(message)
        self.logger.log(message)
        self.database.save(message)


# Usage

logger = Logger()
database = Database()

email_service = NotificationService(EmailSender(), logger, database)
sms_service = NotificationService(SmsSender(), logger, database)
whatsapp_service = NotificationService(WhatsAppSender(), logger, database)

email_service.notify("Hello via Email")
sms_service.notify("Hello via SMS")
whatsapp_service.notify("Hello via WhatsApp")
