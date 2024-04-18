from model.common.entity import Entity

class NotificationDTO(Entity):

    def __init__(self, message, has_notification):
        self.message = message
        self.has_notification = has_notification
        
    def to_dict(self):
        return {
            "message": self.message,
            "has_notification": self.has_notification

        }