from lib.user import User

def test_user_constructs():
    user = User(1, 'email@gmail.com')
    assert user.id == 1
    assert user.email == 'email@gmail.com'

def test_format():
    user = User(1, 'email@gmail.com')
    assert str(user) == "user(1, 'email@email.com')"