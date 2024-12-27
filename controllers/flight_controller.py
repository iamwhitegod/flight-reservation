# Add the project root directory to the sys.path

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from models.auth import CLIAuthenticator # Authenticator for login, signup, etc.
from datetime import datetime # Useful for working wit date and time related flight schedules


# Task 5: Import modules
from models.flight import Flight
from repositories.flight_repository import FlightRepository

# Task 5: Update the FlightController

class FlightController:
  def __init__(self):
    self.flight_repository = FlightRepository()

  def add_flight(self, user):
    print("Add Flight:")
    airline_code = input("Airline Code: ")
    distance_km = float(input("Distance (in km): "))
    dep_time = input("Departure Time (YYY-MM-DD HH:MM:SS): ")
    arri_time = input("Arrival Time (YYY-MM-DD HH:MM:SS): ")
    dep_port = input("Departure Airport Code: ")
    arri_port = input("Arrival Airport Code: ")
    flight = Flight(airline_code, distance_km, dep_time, arri_time, dep_port, arri_port)
    self.flight_repository.add_flight(flight)
    print("Flight added successfully.")

  def delete_flight(self, user):
    if not user._is_admin():
      print("Only admins can cancel flight.")
      return
    print("Delete Flight:")
    flight_no = input("Flight Number: ")
    deleted = self.flight_repository.delete__flight(flight_no)


    if deleted:
      print(f"Flight {flight_no} cancelled successfully.")
    else:
      print(f"Flight {flight_no} not found.")


