import pandas as pd
import sqlite3
from database import DB_NAME

def load_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM cities", conn)
    conn.close()
    return df

def city_sdoh_summary():
    df = load_data()
    if df.empty:
        print("No data available.")
        return

    # Calculate racial percentages
    df['white_pct'] = (df['white'] / df['population'] * 100).round(2)
    df['black_pct'] = (df['black'] / df['population'] * 100).round(2)
    df['asian_pct'] = (df['asian'] / df['population'] * 100).round(2)
    df['latin_pct'] = (df['latin'] / df['population'] * 100).round(2)
    df['other_pct'] = (df['other'] / df['population'] * 100).round(2)
    df['low_food_access_pct'] = (df['low_food_access'] / df['population'] * 100).round(2)

    print("\n--- City Demographics & SDOH Summary ---")
    print(df[['city','state','population','white_pct','black_pct','asian_pct','latin_pct','other_pct',
              'low_food_access','low_food_access_pct','median_income','poverty_rate','unemployment_rate']])

def top_cities_by_population(n=5):
    df = load_data()
    if df.empty:
        print("No data available.")
        return

    top = df.sort_values(by='population', ascending=False).head(n)
    print(f"\nTop {n} cities by population:")
    print(top[['city','state','population']])

def top_cities_by_poverty(n=5):
    df = load_data()
    if df.empty:
        print("No data available.")
        return

    top = df.sort_values(by='poverty_rate', ascending=False).head(n)
    print(f"\nTop {n} cities by poverty rate:")
    print(top[['city','state','poverty_rate','population']])

def top_cities_by_unemployment(n=5):
    df = load_data()
    if df.empty:
        print("No data available.")
        return

    top = df.sort_values(by='unemployment_rate', ascending=False).head(n)
    print(f"\nTop {n} cities by unemployment rate:")
    print(top[['city','state','unemployment_rate','population']])
