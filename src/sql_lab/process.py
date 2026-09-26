import os
import logging
import pandas as pd
import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Read database information from environment variables.
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")

def read_data(filename):
    """Load a CSV file into a pandas DataFrame."""
    logging.info("Reading data from %s", filename)
    data = pd.read_csv(filename)
    logging.info("Data loaded successfully")
    return data

def clean_data(data):
    """Remove rows containing missing values from the DataFrame."""
    logging.info("Cleaning data")

    # Remove rows with missing values.
    cleaned_data = data.dropna()

    logging.info("Data cleaned successfully")
    return cleaned_data

def load_data(data, table):
    """Upload cleaned data to a MySQL table."""
    logging.info("Loading data")

    try:
        conn = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = conn.cursor()

        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id BIGINT PRIMARY KEY,
                `group` VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255),
                gender VARCHAR(255),
                ip_address VARCHAR(255)
            )
        """)

        query = f"""
            INSERT INTO {table}
            VALUES (%s, %s, %s, %s, %s, %s)
        """

# Insert each row into the database.
        for _, row in data.iterrows():
            cursor.execute(query, tuple(row))

        conn.commit()
        logging.info("Data uploaded successfully")

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals() and conn.is_connected():
            conn.close()

def main():
    """Run the data processing and upload workflow."""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")


if __name__ == "__main__":
    main()