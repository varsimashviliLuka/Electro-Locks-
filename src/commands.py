from flask.cli import with_appcontext
import click
import csv
from os import path

from src.extensions import db
from src.models import User, Role
from src import Config


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db():
    new_role_a = Role(name="admin", is_admin=True)
    new_role_a.create()
    new_role_u = Role(name="user", is_admin=False)
    new_role_u.create()
    admin = User(
        name="Luka",
        last_name="Varsimashvili",
        email = "varsimashvili.official@gmail.com",
        phone_number = "592159199",
        username = "01124096118",
        password = "LUKAluka123",
        role_id = new_role_a.id
    )
    admin.create()
    click.echo("Frist Tables Created")

@click.command("insert_db")
@with_appcontext
def insert_db():
    # ყველა სადგურის სტატუსს ცვლის True-თი
    # stations = Stations.query.all()
    # for i in stations:
    #     i.status = True
    #     i.save()
    pass