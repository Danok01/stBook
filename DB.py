# import psycopg2
# import streamlit as st
from dotenv import load_dotenv
import os
# from supabase import create_client, Client
import psycopg2
# from app import gmail
# from datetime import datetime

# Load environment variables from .env
load_dotenv()


# Connect to the database
def get_db():
    conn=psycopg2.connect(
    user=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host"),
    port=os.getenv("port"),
    dbname=os.getenv("dbname")
    )
    return conn
# cur= conn.cursor()
# get_data= cur.execute("SELECT * FROM DB_user_lead;")

# get_db(cur.execute("SELECT * FROM users;"))
# def insert_data():
#     cur.execute("INSERT INTO users (email) VALUES (%(gmail))")
#     cur.close

# def update_rows():
#     cur.execute("UPDATE users WHERE email= (gmail)")
#     cur.close

# Create a cursor to execute SQL queries
# cursor = connection.cursor()
# insert into table
# print(gmail)
# cursor.execute("INSERT INTO DB_user_lead (email) VALUES (%s)", str(gmail))
# connection.commit
# Close the cursor and connection
# cursor.close()
# connection.close()
# print("Connection closed.")
# #DB_URL= ("postgresql://postgres.zfifhntsxhzjlsgofkgf:[YOUR-PASSWORD]@aws-0-eu-central-1.pooler.supabase.com:5432/postgres")

# url: str = os.getenv("SUPABASE_URL")
# key: str = os.getenv("SUPABASE_API_KEY")
# supabase: Client = create_client(url, key)

# def insert_to_table(gmail):
#     existing_data = supabase.table('DB_user_lead').select("*").filter("email", "eq", gmail).execute()

#     if not existing_data:
#         # Data does not exist, proceed to insert
#         supabase.table('DB_user_lead').insert({"email": gmail}).execute()
#     else:
#         st.write("Data already exists")


# def update_table(feedback, rating):
#     supabase.table('DB_user_lead').update({"feedback": feedback, "rating": rating}).execute()
"-------------------------------------------------------------"
# def download_btn():
#     """Downloads a pre-made PDF file."""

#     # 1. Path to your PDF file (replace with your actual file path)
#     pdf_file_path = "Creativ-Writing.pdf" # Place your pdf file in the same directory as the python script.
#     time= datetime.now()
#     formatted_date = time.strftime("%Y%m%d_%H:%M:%S")
#     # Check if the PDF file exists
#     if os.path.exists(pdf_file_path):
#         try:
#             # 2. Read the PDF file in binary mode
#             with open(pdf_file_path, "rb") as pdf_file:
#                 pdf_bytes = pdf_file.read()
            
#             # 3. Streamlit download button
#             st.download_button(
#                 label="Download PDF Report",
#                 data=pdf_bytes,
#                 file_name=f"DBeng_{formatted_date}.pdf",
#                 mime="application/pdf",
#             )
#         except FileNotFoundError:
#             st.error("PDF file not found.")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#     else:
#         st.error("PDF file not found in the specified path.")