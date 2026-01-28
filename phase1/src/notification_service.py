class NotificationService:

    def send(self, type, message):
        if type == "EMAIL":
            print(f"Sending EMAIL: {message}")
        elif type == "SMS":
            print(f"Sending SMS: {message}")
        elif type == "WHATSAPP":
            print(f"Sending WhatsApp: {message}")

        self.log(message)
        self.save(message)

    def log(self, message):
        print("Logging:", message)

    def save(self, message):
        print("Saving to DB:", message)
