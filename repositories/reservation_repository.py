# To handle operations related t the FlightReservation and related tables.

import mysql.connector
from config.database_config import get_db_connection


# Task 8: Complete the implementation of the ReservationRepository class

class ReservationRepository:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()