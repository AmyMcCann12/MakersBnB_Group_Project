from lib.request import *

def test_request_constructs():
    request = Request(0, '2024-02-01', '2024-02-08', 1, 4, True)
    assert request.id == 0
    assert request.date_from == '2024-02-01'
    assert request.date_to == '2024-02-08'
    assert request.user_id == 1
    assert request.listing_id == 4
    assert request.confirmed == True

def test_format():
    request = Request(0, '2024-02-01', '2024-02-08', 1, 4, True)
    assert str(request) == "Request(0, '2024-02-01', '2024-02-08', 1, 4, True)"