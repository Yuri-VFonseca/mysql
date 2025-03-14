import json
import mysql.connector
from geojson import Point, MultiPolygon
from typing import List
# Function to connect to MYSQL
def get_db_connection(): 
    return mysql.connector.connet(
        host = "localhost", 
        user = ""
        password = ""
        database = "ze_code"
    )

# Function to convert GeoJSON to WKT (Well-Known Text)

# Function to process the GeoJSON file and insert data into the database

# Connect to the MySQL database

# Iterate through each partner in the GeoJSON file

# Insert the data into the database

# Commit the changes and close the connection

# Path to the GeoJSON file