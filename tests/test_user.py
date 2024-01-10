from lib.user import User

def test_user_constructs():
    user = User(1, 'name', 'hello@gmail.com', 'Password')
    assert user.id == 1
    assert user.email == 'hello@gmail.com'

def test_format():
    user = User(1, 'name', 'hello@gmail.com', 'Password')
    assert str(user) == "User(1, 'name', 'hello@gmail.com', 'Password')"