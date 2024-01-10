from lib.request_repository import *
from lib.request import *
import datetime

#Test to check that get_all_requests method pulls all requests
def test_getting_the_requests(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    requests = repo.get_all_requests()
    assert requests == [
        Request(1, datetime.date(2024,4,3), datetime.date(2024,4,10), 1, 3, True),
        Request(2, datetime.date(2024,3,20), datetime.date(2024,3,27), 1, 3, True)
    ]

#Test to check that get_single_requests method pulls single request
def test_get_single_request(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    requests = repo.get_single_requests(2)
    assert requests ==  Request(2, datetime.date(2024,3,20), datetime.date(2024,3,27), 1, 3, True)

#Test to check create request method
def test_create_request(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    repo.create_request(Request(None, '2024-05-01', '2024-05-08', 1, 4, True))
    requests = repo.get_all_requests()
    assert len(requests) == 3

#Test to check delete request method
def test_delete_request(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    repo.delete(1)
    requests = repo.get_all_requests()
    assert len(requests) == 1

#Test to check update_dates method does update in database
def test_update_the_request_dates(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    repo.update_dates(2, '2024-06-01', '2024-06-08')
    requests = repo.get_single_requests(2)
    assert requests == Request(2, datetime.date(2024,6,1), datetime.date(2024,6,8), 1, 3, True)

#Test to check date availability when the listing is available
def test_date_is_available(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    is_available = repo.check_dates(datetime.date(2024,7,1), datetime.date(2024,7,8), 3)
    assert is_available == True

#Test to check date availability when the dates are already booked
def test_date_is_not_available(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    is_available = repo.check_dates(datetime.date(2024,3,21), datetime.date(2024,3,24), 3)
    assert is_available == False

#Test to check date availability when the dates are already booked but
#not on requested listing so property should be available
def test_date_available_for_listing_but_booked_other_listing(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    is_available = repo.check_dates(datetime.date(2024,3,21), datetime.date(2024,3,24), 1)
    assert is_available == True

#Test to check if when someone wants to check in on a departure date,
#it the listing is available to book
def test_date_is_available_overlapped_start_end(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    is_available = repo.check_dates(datetime.date(2024,4,10), datetime.date(2024,4,17), 3)
    assert is_available == True

#Test to check if a listing is available when no other requests have been made
#for that listing
def test_date_available_with_no_listing_requests(db_connection):
    db_connection.seed("seeds/requests.sql")
    repo = RequestRepository(db_connection)
    is_available = repo.check_dates(datetime.date(2024,4,10), datetime.date(2024,4,17), 2)
    assert is_available == True
