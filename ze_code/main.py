import json
import mysql.connector
from geojson import Point, MultiPolygon
from typing import List

def get_db_connection(): 
    try:
        return mysql.connector.connect(
            host = "localhost", 
            user = "root",
            password = "sua_senha", # coloque sua senha pessoal
            database = "ze_code"
        )
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

def geojson_to_wkt(geojson): 
    try:
        if geojson['type'] == "Point": 
            return f"POINT({geojson['coordinates'][0]} {geojson['coordinates'][1]})"
        elif geojson['type'] == "MultiPolygon":
            polygons = []
            for polygon in geojson["coordinates"]: 
                rings = []
                for ring in polygon: 
                    points = ', '.join(f"{p[0]} {p[1]}" for p in ring)
                    rings.append(f"({points})")
                polygons.append(f"({', '.join(rings)})")
            return f"MULTIPOLYGON({', '.join(polygons)})"
        raise ValueError("Invalid GeoJSON type")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def process_geojson_file(file_path): 
    try:
        with open(file_path, 'r', encoding="utf-8") as file: 
            geojson_data = json.load(file)
        
        conn = get_db_connection()
        if conn is None:
            print("Error: Could not establish a connection to the database.")
            return
        
        cursor = conn.cursor()

        for feature in geojson_data['pdvs']: 
            partner_data = feature
            coverage_area_wkt = geojson_to_wkt(feature['coverageArea'])
            address_wkt = geojson_to_wkt(feature['address'])    

            query = """
            INSERT INTO partners (id, trading_name, owner_name, document, coverage_area, address)
            VALUES (%s, %s, %s, %s, ST_GeomFromText(%s), ST_GeomFromText(%s))"""
            cursor.execute(query, (
                partner_data['id'],
                partner_data['tradingName'],
                partner_data['ownerName'], 
                partner_data['document'],
                coverage_area_wkt,
                address_wkt
            ))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error processing GeoJSON file: {e}")

def load_partner_by_id(partner_id):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Error: Could not establish a connection to the database.")
            return None

        cursor = conn.cursor()

        query = """
        SELECT id, trading_name, owner_name, document, 
               ST_AsText(coverage_area) AS coverage_area, 
               ST_AsText(address) AS address
        FROM partners
        WHERE id = %s
        """
        cursor.execute(query, (partner_id,))  # Fix here: pass as tuple
        partner = cursor.fetchone()

        cursor.close()
        conn.close()

        if partner:
            return {
                "id": partner[0],
                "trading_name": partner[1],
                "owner_name": partner[2],
                "document": partner[3],
                "coverage_area": partner[4],
                "address": partner[5]
            }
        else:
            print(f"Partner with ID {partner_id} not found.")
            return None
    except Exception as e:
        print(f"Error loading partner by ID: {e}")
        return None

def search_nearest_partner(lat, lon):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Error: Could not establish a connection to the database.")
            return None

        cursor = conn.cursor()

        point_wkt = f"POINT({lon} {lat})"

        query = """
        SELECT id, trading_name, owner_name, document, 
               ST_AsText(coverage_area) AS coverage_area, 
               ST_AsText(address) AS address
        FROM partners
        WHERE ST_Within(ST_GeomFromText(%s), coverage_area)
        """
        cursor.execute(query, (point_wkt,))
        partner = cursor.fetchone()

        cursor.close()
        conn.close()

        if partner:
            return {
                "id": partner[0],
                "trading_name": partner[1],
                "owner_name": partner[2],
                "document": partner[3],
                "coverage_area": partner[4],
                "address": partner[5]
            }
        else:
            print("No partner found near the specified location.")
            return None
    except Exception as e:
        print(f"Error searching for nearest partner: {e}")
        return None

def display_menu():
    print("\nMenu:")
    print("1. Process GeoJSON File")
    print("2. Load Partner by ID")
    print("3. Search Nearest Partner")
    print("4. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                geojson_file_path = input("Enter the path to the GeoJSON file: ")
                process_geojson_file(geojson_file_path)
            elif choice == 2:
                partner_id = input("Enter the partner ID: ")
                partner = load_partner_by_id(partner_id)
                if partner:
                    print("Partner loaded:", partner)
                else:
                    print(f"Partner with ID {partner_id} not found.")
            elif choice == 3:
                latitude = float(input("Enter latitude: "))
                longitude = float(input("Enter longitude: "))
                nearest_partner = search_nearest_partner(latitude, longitude)
                if nearest_partner:
                    print("Nearest partner found:", nearest_partner)
                else:
                    print("No partner found near the specified location.")
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid option, please choose a valid number (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
