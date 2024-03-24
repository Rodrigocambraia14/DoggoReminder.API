from model.common.entity import Entity

class UserDTO(Entity):

    def __init__(self, new_id, name, email, password):
        self.id = new_id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }