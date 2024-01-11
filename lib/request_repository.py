from lib.request import *
from datetime import datetime, timedelta


class RequestRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all_requests(self):
        rows = self.connection.execute('SELECT * FROM requests')
        return [Request(request['id'], request['date_from'], request['date_to'], request['user_id'], request['listing_id'], request['confirmed']) for request in rows]
    
    def get_single_requests(self, id):
        rows = self.connection.execute('SELECT * FROM requests WHERE id = %s', [id])
        return Request(rows[0]['id'], rows[0]['date_from'], rows[0]['date_to'], rows[0]['user_id'], rows[0]['listing_id'], rows[0]['confirmed'])
    
    def create_request(self, request):
        rows = self.connection.execute('INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES (%s, %s, %s, %s, %s) RETURNING id', [request.date_from, request.date_to, request.user_id, request.listing_id, request.confirmed])
        request.id = rows[0]['id']
        return request

    def delete(self, id):
        self.connection.execute('DELETE FROM requests WHERE id = %s', [id])
    
    def update_dates(self, id, date_from, date_to):
        self.connection.execute('UPDATE requests SET date_from = %s, date_to = %s WHERE id = %s', [date_from, date_to, id])

    def check_dates(self, date_from, date_to, listing_id):
        rows = self.connection.execute('SELECT * FROM requests WHERE listing_id = %s', [listing_id])
        if rows != []:
            is_available = True
            for row in rows: 
                reserved_start_date = row['date_from']
                reserved_end_date = row['date_to']
                print(date_from)
                current_date_check = datetime.strptime(date_from, '%Y-%m-%d').date()
                print(type(reserved_end_date))
                print(type(current_date_check))
                while is_available == True and current_date_check <= datetime.strptime(date_to, '%Y-%m-%d').date():
                    if reserved_start_date <= current_date_check < reserved_end_date:
                        is_available = False
                    current_date_check += timedelta(days=1)
            return is_available
        else:
            return True
