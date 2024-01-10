from lib.request_repository import *
from lib.request import *
import datetime


def test_getting_the_requests(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    requests = repo.get_all_requests()
    assert requests == [
        Request(1, datetime.date(2024,4,3), datetime.date(2024,4,10), 1, 3, True),
        Request(2, datetime.date(2024,3,20), datetime.date(2024,3,27), 1, 3, True)
    ]

def test_grab_singular_request(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    requests = repo.get_single_requests(2)
    assert requests ==  Request(2, datetime.date(2024,3,20), datetime.date(2024,3,27), 1, 3, True)

def test_create_request(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    repo.create_request(Request(None, '2024-05-01', '2024-05-08', 1, 4, True))
    requests = repo.get_all_requests()
    assert len(requests) == 3

def test_delete_request(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    repo.delete(1)
    requests = repo.get_all_requests()
    assert len(requests) == 1

def test_update_the_request_dates(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    repo.update_dates(2, '2024-06-01', '2024-06-08')
    requests = repo.get_single_requests(2)
    assert requests == Request(2, datetime.date(2024,6,1), datetime.date(2024,6,8), 1, 3, True)
    