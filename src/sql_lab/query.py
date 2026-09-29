import os
import logging
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

def get_data_by_group(value):
    """Return all rows where the group column equals the given value."""
    logging.info("Getting data for group %s", value)

    try:
        conn = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = conn.cursor()

        # Use a parameterized query to safely filter by group.
        query = "SELECT * FROM mock WHERE `group` = %s"
        cursor.execute(query, (value,))

        results = cursor.fetchall()
        logging.info("Data retrieved successfully")
        return results

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals() and conn.is_connected():
            conn.close()

def plot_counts(groupby):
    """Count rows for each distinct value of the given column."""
    logging.info("Counting rows by %s", groupby)

    try:
        conn = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = conn.cursor()

        # Use predefined queries so column names are not inserted into SQL directly.
        queries = {
            "id": "SELECT id, COUNT(*) FROM mock GROUP BY id",
            "group": "SELECT `group`, COUNT(*) FROM mock GROUP BY `group`",
            "last_name": "SELECT last_name, COUNT(*) FROM mock GROUP BY last_name",
            "email": "SELECT email, COUNT(*) FROM mock GROUP BY email",
            "gender": "SELECT gender, COUNT(*) FROM mock GROUP BY gender",
            "ip_address": "SELECT ip_address, COUNT(*) FROM mock GROUP BY ip_address"
        }

        if groupby not in queries:
            raise ValueError("Invalid column name")

        cursor.execute(queries[groupby])

        results = cursor.fetchall()
        logging.info("Counts retrieved successfully")
        return results

    except (mysql.connector.Error, ValueError) as error:
        logging.error("Error: %s", error)
        return []

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals() and conn.is_connected():
            conn.close()

def main():
    """Run the database query functions and display their results."""
    # Show all rows belonging to group A.
    group_data = get_data_by_group("A")
    print("Rows in group A:")
    for row in group_data:
        print(row)

    # Show the number of rows in each group.
    counts = plot_counts("group")
    print("\nCounts by group:")
    for row in counts:
        print(row)


if __name__ == "__main__":
    main()