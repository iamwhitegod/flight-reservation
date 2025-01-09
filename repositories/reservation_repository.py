# To handle operations related t the FlightReservation and related tables.

import mysql.connector
from config.database_config import get_db_connection


# Task 8: Complete the implementation of the ReservationRepository class

class ReservationRepository:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()

    def get_reservation(self, reservation_number):
        query = "SELECT * FROM FlightReservation WHERE reservation_number = %s"
        self.cursor.execute(query, (reservation_number,))
        return self.cursor.fetchone()

    def get_reservations_by_user(self, user):
        username = user.username

        get_user_id_query = """
            SELECT acount_id FROM Account
            WHERE username = %s
        """

        self.cursor.execute(get_user_id_query, (username,))
        user_id_result = self.cursor.fetchone()
     
        if user_id_result:
            user_id = user_id_result[0]

            # Get reservation from the FlightReservation table for the user ID
            query = """
                SELECT * FROM FlightReservation
                WHERE user_id = %s
            """
            self.cursor.execute(query, (user_id,))
            return self.cursor.fetchall()
        
        else:
            return None # User with the given username not found

    
    def cancel_reservation(self, reservation_number):
        # Retrieve the reservation details
        get_reservation_query = """
            SELECT flight_no, seats
            FROM FlightReservation
            WHERE reservation_number = %s
        """
        self.cursor.execute(get_reservation_query, (reservation_number,))
        reservation = self.cursor.fetchone()

        if reservation:
            flight_no, seats = reservation

            delete_reservation_query = """
                DELETE FROM FlightReservation 
                WHERE reservation_number = %s
            """
            self.cursor.execute(delete_reservation_query, (reservation_number,))

            # Update booked seats in the flight table
            update_flight_query = """
                UPDATE Flight
                SET booked_seats = booked_seats - %s
                WHERE flight_no = %s
            """
            self.cursor.execute(update_flight_query, (seats, flight_no))

            # Commit the transaction to save the updates
            self.connection.commit()
            print(f"Reservation {reservation_number} has been successfully cancelled and deleted.")


        else:
            print(f"Reservation {reservation_number} not found.")

 
    def create_reservation(self, user, flight_no, seats, creation_date, payment_amount):
        username = user.username

        # First, get the user ID from the Account table based on the username
        get_user_id_query = """
            SELECT account_id FROM Account
            WHERE username = %s
        """

        self.cursor.execute(get_user_id_query, (username,))
        user_id_result = self.cursor.fetchone()

        if user_id_result:
            user_id = user_id_result[0]

        query = """
            INSERT INTO FlightReservation (user_id, flight_no, seats, creation_date, payment_amount)
            VALUES (%s, %s, %s, %s, %s)
        """

        self.cursor.execute(query, (user_id, flight_no, seats, creation_date, payment_amount))


        # Now, update the booked seats in the Flight table
        update_flight_query = """
            UPDATE Flight
            SET booked_seats = booked_seats + %s
            WHERE flight_no = %s
        """

        self.cursor.execute(update_flight_query, (seats, flight_no))
        self.connection.commit()


    def make_reservation(self, user, direct_flight=None, itinerary=None):
        print("Initiating reservation process...")
        num_seats = int(input("How many seats would you like to reserve?: "))

        # Check if it's a direct flight or itinerary reservation
        if direct_flight:
            available_seats = direct_flight.get_available_seats()

            if num_seats > available_seats:
                print(f"Sorry, only {available_seats} seats available for this flight.")
                return
            total_price = float(direct_flight.get_ticket_price()) * num_seats
            print(f"Total price for {num_seats} seat(s) is: ${total_price}")

            # print(f"Direct Flight: {direct_flight}")
            # Check seat availability for the direct flight

            self.reservation_repo.create_reservation(
                user=user, # Assuming the User object has this method
                flight_no=direct_flight.get_flight_no(),
                seats=num_seats,
                creation_date=datetime.now(),
                payment_amount=total_price
            )
            print(f"Reservation for flight {direct_flight.get_flight_no()} made successfully.")

        elif itinerary:
            total_price = 0
            all_available = True

            # Check seat availability for all flights in the itinerary
            for flight in itinerary:
                available_seats = flight.get_available_seats()

                if num_seats > available_seats:
                    print(f"Sorry, only {available_seats} seats available for flight {flight.get_flight_no()}.")
                    all_available = False
                    break
                total_price += float(flight.get_ticket_price()) * num_seats

            if not all_available:
                return
            
            print(f"Total price for {num_seats} seat(s) across the itinerary is: ${total_price}")

            # Create reservations for the entire itinerary
            for flight in itinerary:
                self.reservation_repo.create_reservation(
                    user=user,
                    flight_no=flight.get_flight_no(),
                    seats=num_seats,
                    creation_date=datetime.now(),
                    payment_amount=float(flight.get_ticket_price()) * num_seats
                )

            print("Itinerary reservation made successfully.")
