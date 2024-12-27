# Task 14: Import the Amadeus components



# Task 3: Define the Flight class


class Flight:
  def __init__(self, airline_code, distance_km, dep_time, arri_time, dep_port, arri_port, booked_seats = 0, flight_no = None):
    self.__flight_no = flight_no
    self.__airline_code - airline_code
    self.__distance_km = distance_km
    self.__dep_time = dep_time
    self.__arri_time = arri_time
    self.__dep_port = dep_port
    self.__arri_port = arri_port
    self.__total_seats = 50
    self.__booked_seats = 0
  

  def get_flight_no(self):
    return self.__flight_no
  
  def get_airline_code(self):
    return self.__airline_code
  
  def get_distance_km(self):
    return self.__distance_km
  
  def get_dep_time(self):
    return self.__dep_time
  
  def get_arri_time(self):
    return self.__arri_time
  
  def get_dep_port(self):
    return self.__dep_port
  
  def get_arri_port(self):
    return self.__arri_port
  
  def get_available_seats(self):
    return self.__total_seats - self.__booked_seats
  

  # Setters
  def set_flight_no(self, flight_no):
    self.__flight_no = flight_no

  def set_airline_code(self, airline_code):
    self.__airline_code = airline_code

  def set_dep_time(self, dep_time):
    self.__dep_time = dep_time

  def set_arri_time(self, arri_time):
    self.__arri_time = arri_time

  def set_arri_port(self, arri_port):
    self.__arri_port = arri_port

  

  # Book seats
  def book_seats(self, num_seats):
    if num_seats <= self.get_available_seats():
      self.__booked_seats += num_seats
      print(f"{num_seats} seat(s) successfully booked. ")

    else:
      print(f"Not enough seats available. Only {self.get_available_seats()} left.")



  # Seat availability
  def get_total_seats(self):
    return len(self.__seats)
  

  # String representation
  def __repr__(self):
    return (f"Flight No: {self.__flight_no}, Airline Code: {self.__airline_code},"
            f"Departure from: {self.__dep_port} at {self.__dep_time},"
            f"Arrival at: {self.__arri_port} at {self.arri_time}")
  
  
  # Task 14: Implement the get_ticket_price() function

  


