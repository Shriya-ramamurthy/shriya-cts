class Email:
    def send(self):
        return "Email Notification Sent"

class SMS:
    def send(self):
        return "SMS Notification Sent"

class NotificationFactory:

    @staticmethod
    def get_notification(notification_type):
        if notification_type == "email":
            return Email()
        elif notification_type == "sms":
            return SMS()

notification = NotificationFactory.get_notification("email")
print(notification.send())

notification = NotificationFactory.get_notification("sms")
print(notification.send())