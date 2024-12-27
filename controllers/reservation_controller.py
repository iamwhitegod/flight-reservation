import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
import mysql.connector

# Task 9: Import modules

__all__ = ['ReservationController']
class ReservationController:
  def __init__(self):
    # Establish a database connection
    self.connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="z7fnvxQ2@",
      database="flight"
    )

    # Task 9: Instantiate the repository objects

  # A helper function to create Flight objects out of database tuples
  def create_flight_object(self, flight_data):
    # Reorder tuple to match the Flight initializer
    reordered_flight_data = flight_data[1:] + (flight_data[0],)
    return Flight(*reordered_flight_data)
  

  # Task 9: Define the view_reservations() function


  # Task 9: Define the cancel_reservations() function


  # Task 9: Define the process_payment() function


   # Task 9, 16: Define the make_reservation() function



  # Task 15: Define the function to find the cheapest route



  # Task 13: Define the function to search flights



    # Task 15: Call the _find_cheapest_route() function



  # Task 17: Create the _handle_user_choice() function


  



  


