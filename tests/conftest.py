import functools

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pytest
from sqlalchemy_media import StoreManager, FileSystemStore

from flasker.models.db import  Base


base_url = 'http://static1.example.orm'
TEMP_PATH = '/tmp/sqlalchemy-media'


@pytest.fixture(scope='session')
def engine():

    return create_engine('sqlite:///:memory:')


@pytest.yield_fixture(scope='session')
def tables(engine):
    StoreManager.register(
        'fs',
        functools.partial(FileSystemStore, TEMP_PATH, base_url),
        default=True
    )
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.yield_fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()

