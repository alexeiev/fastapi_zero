from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(
            username='alex',
            email='alex@email.com',
            password='password',
        )

        session.add(user)
        session.commit()

    result = session.scalar(select(User).where(User.email == 'alex@email.com'))

    assert asdict(result) == {
        'id': 1,
        'username': 'alex',
        'password': 'password',
        'email': 'alex@email.com',
        'created_at': time,
        'updated_at': time,
    }
