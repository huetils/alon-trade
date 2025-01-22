import sqlite3
import time
from typing import List, Tuple

DB_NAME: str = "orderbook_data.db"


def fetch_latest_rows(table_name: str, limit: int = 10) -> List[Tuple[str]]:
    """
    Fetch the latest rows from the specified table.
    :param table_name: The table to query.
    :param limit: Number of rows to fetch.
    :return: List of rows.
    """
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
    cursor: sqlite3.Cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT * FROM {table_name}
        ORDER BY timestamp DESC
        LIMIT ?
    """,
        (limit,),
    )

    rows: List[Tuple[str]] = cursor.fetchall()
    conn.close()
    return rows


def list_tables() -> List[str]:
    """
    List all tables in the database.
    :return: List of table names.
    """
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
    cursor: sqlite3.Cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables: List[Tuple[str]] = cursor.fetchall()
    conn.close()

    return [table[0] for table in tables]


def main() -> None:
    tables = list_tables()
    print("Available tables:")
    for table in tables:
        print(f"- {table}")

    while True:
        print("\nFetching latest rows...")
        for table in tables:
            print(f"\nTable: {table}")
            rows = fetch_latest_rows(table)
            for row in rows:
                print(row)
        time.sleep(5)  # Adjust the polling interval as needed


if __name__ == "__main__":
    main()
