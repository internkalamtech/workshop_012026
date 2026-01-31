# instead of having many if and elif statement we can use functions to solve the issue open/closed principle
class Email:
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMS:
    def send(self, message):
        print(f"Sending SMS: {message}")
        
class WhatsApp: 
    def send(self, message):
        print(f"Sending WhatsApp: {message}")

class NotificationService:
    def notify(self, provider, message):
        provider.send(message)
        self.log(message)
        self.save(message)

    def log(self, message):
        print(f"Logging: {message}")

    def save(self, message):
        print(f"Saving to DB: {message}")

