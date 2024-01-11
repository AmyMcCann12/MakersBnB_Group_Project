class Request:
    def __init__(self, id, date_from, date_to, user_id, listing_id, confirmed):
        self.id = id
        self.date_from = date_from
        self.date_to = date_to
        self.user_id = user_id
        self.listing_id = listing_id
        self.confirmed = confirmed

    def __repr__(self):
        return f"Request({self.id}, '{self.date_from}', '{self.date_to}', {self.user_id}, {self.listing_id}, {self.confirmed})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__