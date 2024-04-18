from model.common.entity import Entity

#classe ainda não está sendo utilizada, pois não estou armazenando notificações disparadas no SQLite

class Notification(Entity):

    def __init__(self, message, has_notification):
        self.message = message
        self.has_notification = has_notification
        
