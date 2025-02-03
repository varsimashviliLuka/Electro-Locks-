from flask.cli import with_appcontext
import click
import csv
from os import path

from src.extensions import db
from src.models import Stations
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
    pass
    # stations_csv_file_path = path.join(Config.BASE_DIR, "stations_2024-12-05.csv")
    # weather_data_csv_file_path = path.join(Config.BASE_DIR, "weather_data_2024-12-05.csv")

    # click.echo("Adding Stations")
    # with open(stations_csv_file_path, mode='r') as file:
    #     csv_reader = csv.DictReader(file)
    #     # Iterate through each row in the CSV file
    #     for row in csv_reader:
    #         # Create a new Station instance for each row
    #         new_station = Stations(
    #             station_name=row['station_name'],
    #             url=row['url'],
    #             api=row['api'],
    #             latitude=row['latitude'],
    #             longitude=row['longitude']
    #         )
    #         new_station.create()


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