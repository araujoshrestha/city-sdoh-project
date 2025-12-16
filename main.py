from models import City, CityRepository, DataValidator
from database import initialize_database
from analysis import (
    city_sdoh_summary,
    top_cities_by_population,
    top_cities_by_poverty,
    top_cities_by_unemployment
)

# Initialize database and create tables if needed
initialize_database()

def print_menu():
    print("\n--- City Data CLI ---")
    print("1) Register a new city")
    print("2) Update an existing city")
    print("3) Add demographic/SDOH data to an existing city")
    print("4) View all cities")
    print("5) Exit")
    print("6) City Demographics & SDOH Summary")
    print("7) Top cities by population")
    print("8) Top cities by poverty rate")
    print("9) Top cities by unemployment rate")

def get_city_input(existing_city=None):
    state = input(f"Enter the state [{existing_city.state if existing_city else ''}]: ") or (existing_city.state if existing_city else '')
    city_name = input(f"Enter the city name [{existing_city.city if existing_city else ''}]: ") or (existing_city.city if existing_city else '')
    population = DataValidator.to_int(input(f"Enter population [{existing_city.population if existing_city else ''}]: "), "Population") or (existing_city.population if existing_city else None)
    white = DataValidator.to_int(input(f"Demographics - White [{existing_city.white if existing_city else ''}]: "), "White") or (existing_city.white if existing_city else None)
    black = DataValidator.to_int(input(f"Demographics - Black [{existing_city.black if existing_city else ''}]: "), "Black") or (existing_city.black if existing_city else None)
    asian = DataValidator.to_int(input(f"Demographics - Asian [{existing_city.asian if existing_city else ''}]: "), "Asian") or (existing_city.asian if existing_city else None)
    latin = DataValidator.to_int(input(f"Demographics - Latin [{existing_city.latin if existing_city else ''}]: "), "Latin") or (existing_city.latin if existing_city else None)
    other = DataValidator.to_int(input(f"Demographics - Other [{existing_city.other if existing_city else ''}]: "), "Other") or (existing_city.other if existing_city else None)
    
    # SDOH fields
    low_food_access = DataValidator.to_int(input(f"Population with low food access [{existing_city.low_food_access if existing_city else ''}]: "), "Low Food Access") or (existing_city.low_food_access if existing_city else None)
    median_income = DataValidator.to_int(input(f"Median household income [{existing_city.median_income if existing_city else ''}]: "), "Median Income") or (existing_city.median_income if existing_city else None)
    poverty_rate = DataValidator.to_int(input(f"Poverty rate (percent) [{existing_city.poverty_rate if existing_city else ''}]: "), "Poverty Rate") or (existing_city.poverty_rate if existing_city else None)
    unemployment_rate = DataValidator.to_int(input(f"Unemployment rate (percent) [{existing_city.unemployment_rate if existing_city else ''}]: "), "Unemployment Rate") or (existing_city.unemployment_rate if existing_city else None)

    return City(
        state, city_name, population, white, black, asian, latin, other,
        low_food_access, median_income, poverty_rate, unemployment_rate,
        id=(existing_city.id if existing_city else None)
    )

def main():
    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == '1':
            city = get_city_input()
            new_id = CityRepository.add_city(city)
            print(f"City '{city.city}' added with ID {new_id}.")

        elif choice == '2':
            name = input("Enter the name of the city to update: ")
            city = CityRepository.get_city_by_name(name)
            if city:
                city = get_city_input(existing_city=city)
                CityRepository.update_city(city)
                print(f"City '{city.city}' updated successfully.")
            else:
                print("City not found.")

        elif choice == '3':
            name = input("Enter the name of the city to add data: ")
            city = CityRepository.get_city_by_name(name)
            if city:
                city = get_city_input(existing_city=city)
                CityRepository.update_city(city)
                print(f"Data for city '{city.city}' updated successfully.")
            else:
                print("City not found.")

        elif choice == '4':
            cities = CityRepository.list_all_cities()
            if cities:
                for c in cities:
                    print(f"{c.id}: {c.city}, {c.state} | Population: {c.population}")
            else:
                print("No cities registered yet.")

        elif choice == '5':
            print("Exiting...")
            break

        elif choice == '6':
            city_sdoh_summary()

        elif choice == '7':
            top_cities_by_population()

        elif choice == '8':
            top_cities_by_poverty()

        elif choice == '9':
            top_cities_by_unemployment()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
