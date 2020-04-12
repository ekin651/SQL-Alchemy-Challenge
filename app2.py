from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import create_engine, inspect
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData
from sqlalchemy.ext.automap import automap_base
import numpy as np
import pandas as pd
import datetime as dt

from flask import Flask, jsonify


# Connect to database
engine=create_engine("sqlite:///Resources/hawaii.sqlite")
conn=engine.connect()
meta=MetaData()
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
# Create an inspector and connect it to the engine
inspector=inspect(engine)
#dir(inspector)
# View table names
tables=inspector.get_table_names()
tables

measurement = Base.classes.measurement
station=Base.classes.station

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"


    )


@app.route("/api/v1.0/names")
def hello():
    print("hello")





if __name__ == '__main__':
    app.run(debug=True)
