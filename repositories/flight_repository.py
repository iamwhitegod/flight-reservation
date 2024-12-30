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
    """Find direct flights only."""
    query = """
      SELECT * FROM Flight
      WHERE dep_port = %s AND arri_port = %s AND DATE(dep_time) = %s
    """

    self.cursor.execute(query, (departure_airport, destination_airport, date))
    return self.cursor.fetchall()

  def _find_itineraries(self, date, departure_airport, destination_airport, max_stops):
    """Find possible connecting flights with a maximum of 2 stops using BFS."""
    itinerary_list = []

    # Use BFS to find paths between departure_airport and destination_airport
    queue = deque([(destination_airport, [], None, 0)])
    visited = set()

    while queue:
      current_airport, flights_taken, last_arrival_time, stops_count = queue.popleft()

      if current_airport in visited:
        continue
      visited.add(current_airport)

      if stops_count > max_stops:
        continue # Skip this branch if stops exceeded max_stops

      # Find all flight from the airport
      query = """
        SELECT * FROM Flight
        WHERE dep_port = %s AND DATE(dep_time) = %s
      """
      self.cursor.execute(query, (current_airport, date))
      connecting_flights = self.cursor.fetchall()

      for flight in connecting_flights:
        flight_no, airline_code, distance_km, dep_time, arri_time, dep_port, arri_port, seats = flight

        # Skip direct flight (i.e., where arrival port matches the destination airport).
        if dep_port == departure_airport and arri_port == destination_airport:
          continue # Skip direct flight

        if last_arrival_time is None or (dep_time > last_arrival_time + timedelta(hours=1)):
          new_flights_taken = flights_taken + [flight]

          if arri_port == destination_airport:
            itinerary_list.append(new_flights_taken)
          else:
            queue.append((arri_port, new_flights_taken, arri_time, stops_count + 1))

      return itinerary_list

  def find_flights(self, date, departure_airport, destination_airport):
    """Find direct flights and possible connecting itineraries"""
    direct_flights = self.__find_direct_flights(date, departure_airport, destination_airport)

    # Find possible connecting itineraries with a maximum of 2 stops
    itineraries = self.__find_itineraries(date, departure_airport, destination_airport, max_stops=2)
    return direct_flights + itineraries

  # Task 4: Define the function to add flight


  # Task 4: Define the function to delete flight



  # Task 4, 11: Find a direct flight



  # Task 4, 12: Find the itineraries



  # Task 4, 13: Define the function to find flights
  