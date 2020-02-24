from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import click
from flask.cli import with_appcontext


engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def close_db(e=None):
    Base.metadata.drop_all(engine)
    print("The database is closed")


@click.command('init_db')
@with_appcontext
def init_db_command():
    Base.metadata.create_all(engine)
    click.echo('Database is created')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


