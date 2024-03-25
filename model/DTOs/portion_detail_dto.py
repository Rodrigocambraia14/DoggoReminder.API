from model.common.entity import Entity

class PortionDetailDTO(Entity):

     def __init__(self, new_id, name, grams, feed_time, food_routine_id):
        self.id = new_id
        self.name = name
        self.grams = grams
        self.feed_time = feed_time
        self.food_routine_id = food_routine_id

     def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "grams": self.grams,
            "feed_time": self.feed_time,
            "food_routine_id": self.food_routine_id
        }