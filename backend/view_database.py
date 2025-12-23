#!/usr/bin/env python3
"""
Script to view the contents of the SQLite database.
"""

import sqlite3
import os

def view_database():
    # Database path
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    
    # Check if database exists
    if not os.path.exists(db_path):
        print(f"Database file not found at {db_path}")
        return
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")
    
    print("\n" + "="*50 + "\n")
    
    # Display contents of each table
    for table in tables:
        table_name = table[0]
        print(f"Contents of table '{table_name}':")
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        print("Columns:", ", ".join(column_names))
        
        # Get all rows
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        
        # Display rows
        if rows:
            # Print header
            print("-" * (len(column_names) * 15))
            print(" | ".join(f"{col:<12}" for col in column_names))
            print("-" * (len(column_names) * 15))
            
            # Print data
            for row in rows:
                print(" | ".join(f"{str(item):<12}" for item in row))
        else:
            print("No data in this table.")
        
        print("\n" + "="*50 + "\n")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    view_database()
