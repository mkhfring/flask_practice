from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pytest

from flasker.models.database import db


@pytest.fixture(scope='session')
def engine():
    db.create_engine('sqlite:///:memory:', {})

    return True


@pytest.yield_fixture(scope='session')
def tables(engine):
    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    db.create_all()
    yield
    db.drop_all()


@pytest.yield_fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    # connection = engine.connect()
    # # begin the nested transaction
    # transaction = connection.begin()
    # # use the connection with the already started transaction
    # session = Session(bind=connection)

    yield db.session

    db.session.close()
    # roll back the broader transaction
    # transaction.rollback()
    # put back the connection to the connection pool
    # connection.close()

