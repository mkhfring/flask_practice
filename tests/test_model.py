from flasker.models import User, Post

def test_user(dbsession):
    post = Post(title='salam', body='bye')
    user = User(user_name='Mohamad', password='123456', posts=[post])
    dbsession.add(user)
    dbsession.flush()
