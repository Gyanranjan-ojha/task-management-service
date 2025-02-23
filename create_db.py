"""
Script to create PostgreSQL database based on environment settings.
"""
import sys
import os
import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Get the current script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.append(project_root)

from task_manager.config import env_settings


def create_database(db_name: str) -> None:
    """
    Creates a PostgreSQL database if it doesn't exist.
    
    Args:
        db_name: Name of the database to create
    """
    try:
        conn = psycopg2.connect(
            host=env_settings.DB_HOST,
            user=env_settings.DB_USER,
            password=env_settings.DB_PASSWORD.get_secret_value(),
            port=env_settings.DB_PORT,
            database='postgres'  # Default database for initial connection
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        # Check if database exists
        cur.execute("SELECT datname FROM pg_database;")
        databases = [db[0] for db in cur.fetchall()]
        
        if db_name not in databases:
            # Create database if it doesn't exist
            cur.execute(f"CREATE DATABASE {db_name}")
            print(f"{db_name} database successfully created...")
        else:
            print(f"{db_name} database already exists...")
            
    except Exception as e:
        print(f"Error in create_database: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    create_database(db_name=env_settings.DB_NAME)