import sqlite3
from database import get_connection

class City:
    def __init__(
        self,
        state,
        city,
        population=None,
        white=None,
        black=None,
        asian=None,
        latin=None,
        other=None,
        low_food_access=None,
        median_income=None,
        poverty_rate=None,
        unemployment_rate=None,
        id=None
    ):
        self.id = id
        self.state = state
        self.city = city
        self.population = population
        self.white = white
        self.black = black
        self.asian = asian
        self.latin = latin
        self.other = other
        self.low_food_access = low_food_access  
        self.median_income = median_income
        self.poverty_rate = poverty_rate
        self.unemployment_rate = unemployment_rate


    def __str__(self):
        return f"{self.city}, {self.state} (Population {self.population})"


class CityRepository:
    """
    Handles all database operations for City objects.
    """

    @staticmethod
    def add_city(city: City):
        connect = get_connection()
        cursor = connect.cursor()

        cursor.execute("""
        INSERT INTO cities (state, city, population, white, black, asian, latin, other,
                        low_food_access, median_income, poverty_rate, unemployment_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (city.state, city.city, city.population, city.white, city.black, city.asian, city.latin, city.other,
      city.low_food_access, city.median_income, city.poverty_rate, city.unemployment_rate))


        connect.commit()
        connect.close()

    @staticmethod
    def update_city(city: City):
        if city.id is None:
            raise ValueError("Cannot update city without an ID.")

        connect = get_connection()
        cursor = connect.cursor()

        cursor.execute("""
            UPDATE cities
            SET state = ?, city = ?, population = ?, white = ?, black = ?, asian = ?, latin = ?, other = ?,
                low_food_access = ?, median_income = ?, poverty_rate = ?, unemployment_rate = ?
            WHERE id = ?
        """, (city.state, city.city, city.population, city.white, city.black, city.asian, city.latin, city.other,
            city.low_food_access, city.median_income, city.poverty_rate, city.unemployment_rate, city.id))

        connect.commit()
        connect.close()

    @staticmethod
    def get_city_by_name(city_name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM cities WHERE city = ?", (city_name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return City(
                id=row[0], state=row[1], city=row[2], population=row[3],
                white=row[4], black=row[5], asian=row[6], latin=row[7], other=row[8]
            )
        return None

    @staticmethod
    def list_all_cities():
        connect = get_connection()
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM cities")
        rows = cursor.fetchall()
        connect.close()

        cities = []
        for row in rows:
            cities.append(
                City(
                    id=row[0], state=row[1], city=row[2], population=row[3],
                    white=row[4], black=row[5], asian=row[6], latin=row[7], other=row[8]
                )
            )
        return cities


class DataValidator:
    """
    Handles error checking and validation of user inputs.
    """
    @staticmethod
    def to_int(value, field_name):
        if value == "" or value is None:
            return None

        try:
            return int(value)
        except ValueError:
            print(f"Error: {field_name} must be a number.")
            return None
