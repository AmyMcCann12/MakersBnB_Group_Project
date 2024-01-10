class Listing:
    def __init__(self, id, title, description, price, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.user_id = user_id

    def __repr__(self):
        return f"Listing({self.id}, '{self.title}', '{self.description}', {self.price}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__