import mysql.connector
from datetime import datetime
from collections import deque
from config.database_config import get_db_connection

class FlightRepository:
  def __init__(self):
    self.connection = get_db_connection()
    self.cursor = self.connection.cursor()

  def add_flight(self, flight):
    airline_code = flight.get_airline_code()
    distance_km = flight.get_distance_km()
    dep_time = flight.get_dep_time()
    arri_time = flight.get_arri_time()
    dep_port = flight.get_dep_port()
    arri_port = flight.get_arri_port()
    query = """
        INSERT INTO Flight (airline_code, distance_km, dep_time, arri_time, dep_port, arri_port)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    self.cursor.execute(query, (airline_code, distance_km, dep_time, arri_time, dep_port, arri_port))
    self.connection.commit()


    # Get the auto-incremented flight number (last inserted ID)
    inserted_flight_no = self.cursor.lastrowid

    # Display the inserted flight number
    print(f"Flight added successfully. Flight Number: {inserted_flight_no}")
    return inserted_flight_no
  
  def delete_flight(self, flight_no):
    query = "DELETE FROM Flight WHERE flight_no = %s"
    self.cursor.execute(query, (flight_no,))
    self.connection.commit()

    # Check how many rows were affected
    if self.cursor.rowcount() > 0:
      return True
    
    else:
      return False
    
  def _find_direct_flights(self, date, departure_airport, destination_airport):
    pass

  def _find_itineraries(self, date, departure_airport, destination_airport, max_stops):
    pass

  def find_flights(self, date, departure_airport, destination_airport):
    """Find direct flights and possible connecting itineraries"""
    pass

  # Task 4: Define the function to add flight


  # Task 4: Define the function to delete flight



  # Task 4, 11: Find a direct flight



  # Task 4, 12: Find the itineraries



  # Task 4, 13: Define the function to find flights
  