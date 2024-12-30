import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
import mysql.connector

# Task 9: Import modules

from models.flight import Flight
from models.flight_reservation import FlightReservation

# Modules handling the database-related operations
from repositories.flight_repository import FlightRepository
from repositories.reservation_repository import ReservationRepository

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
    self.flight_repo = FlightRepository()
    self.reservation_repo = ReservationRepository()

  # A helper function to create Flight objects out of database tuples
  def create_flight_object(self, flight_data):
    # Reorder tuple to match the Flight initializer
    reordered_flight_data = flight_data[1:] + (flight_data[0],)
    return Flight(*reordered_flight_data)
  

  # Task 9: Define the view_reservations() function
  def view_reservations(self, user):
    print("In the function View Reservations:")
    reservations = self.reservation_repo.get_reservations_by_user(user)

    if not reservations:
      print("No reservations found for you")
      return
    
    for reservation in reservations:
      print(reservation)

  # Task 9: Define the cancel_reservations() function
  def cancel_reservation(self, user):
    reservation_number = input("Please enter the reservation number you want to cancel: ")

    # Validate the input
    if not reservation_number:
      print("Reservation number is required to cancel a reservation.")
      return
    
    # Check if the user is authorized to cancel this reservation
    user_reservations = self.reservation_repo.get_reservations_by_user(user)

    if reservation_number not in user_reservations:
      print(f"User {user.username} is not authorized to cancel reservation {reservation_number}.")
      return
    
    # Call the repository layer to cancel the reservation
    try:
      self.reservation_repo.cancel_reservation(reservation_number)
      print(f"Reservation {reservation_number} has been canceled.")

    except Exception as e:
      print(f"Error cancelling reservation: {e}")

  # Task 9: Define the process_payment() function
  def process_payment(self, user, price):
    # Dummy payment processing logic to simulate successful payment
    print(f"Processing payment for {user.username} for total of: {price}")
    return True

   # Task 9, 16: Define the make_reservation() function

  def make_reservation(self, user, direct_flight=None, itinerary=None):
    print("Initialing reservation process...")
    return



  # Task 15: Define the function to find the cheapest route



  # Task 13: Define the function to search flights
  def search_flight(self, user):
    print("Search Flight:")
    date = input("Date (YYYY-MM-DD): ")
    departure = input("Departure Airport: ")
    destination = input("Destination Airport: ")


    flights_or_itineraries = self.flight_repo.find_flights(date, departure, destination)

    # VAriables to keep track of the shortest flights
    shortest_itinerary = None
    shortest_itinerary_distance = float('inf')
    shortest_direct_flight = None
    shortest_direct_flight_distance = float('inf')


    for option in flights_or_itineraries:
      if isinstance(option, list):
        # It's an itinerary with multiple flights
        itinerary_flights = [self.create_flight_object(flight_tuple) for flight_tuple in option]
        total_distance = sum(flight.get_distance_km() for flight in itinerary_flights)

        if total_distance < shortest_itinerary_distance:
          shortest_itinerary = itinerary_flights
          shortest_itinerary_distance = total_distance

      else:
        # It's a direct flight
        flight_obj = self.create_flight_object(option)
        if flight_obj.get_distance_km() < shortest_direct_flight_distance:
          shortest_direct_flight = flight_obj
          shortest_direct_flight_distance = flight_obj.get_distance_km()

    # Output results
    if shortest_itinerary:
      print("\n\nShortest Itinerary found:")
      total_price = 0
      for flight in shortest_itinerary:
        price = flight.get_ticket_price()
        if price:
          total_price += float(price)
          print(flight)
          print(price, "$")

      print(f"Total ticket price for the itinerary: {total_price} \n")

    else:
      print("No itineraries found.")

    if shortest_direct_flight:
      print(f"\n\nShortest Direct Flight: {shortest_direct_flight}")
      print(f"Ticket price: ", shortest_direct_flight.get_ticket_price(), "$")

    else:
      print("No direct flights found. \n")




    



    # Task 15: Call the _find_cheapest_route() function



  # Task 17: Create the _handle_user_choice() function


  



  


