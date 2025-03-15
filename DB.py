import psycopg2
from dotenv import load_dotenv
import os
#from app import gmail

# Load environment variables from .env
load_dotenv()

#DB_URL= ("postgresql://postgres.zfifhntsxhzjlsgofkgf:[YOUR-PASSWORD]@aws-0-eu-central-1.pooler.supabase.com:5432/postgres")
def get_db(gmail):
    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    # Connect to the database
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        print("Connection successful!")
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        #insert into table
        print(str(gmail));
        cursor.execute("INSERT INTO DB_user_lead (email) VALUES (%s)", str(gmail))
        connection.commit
        # Close the cursor and connection
        cursor.close()
        connection.close()
        # print("Connection closed.")

    except Exception as e:
        print(f"Failed to connect: {e}")


