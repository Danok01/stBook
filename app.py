import streamlit as st
from DB import get_db #get database conn
from psycopg2 import sql
from datetime import datetime

#page configuration settings and page setup
st.set_page_config(page_title="DBE", layout="centered") # webpage name
css= """
<style>
section.stMain.st-emotion-cache-bm2z3a.ea3mdgi8(
background-image: url("https://plus.unsplash.com/premium_photo-1668473366952-45f06fbf6492?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
)
</style>"""
st.markdown(css, unsafe_allow_html=True)

# global variables
time= datetime.now()
formatted_date = time.strftime("%Y%m%d_%H:%M:%S")
pdf_file_path= "DBE.pdf"

#Page writeup
st.title("Database Engineering")
st.write(
"""
My passion for Databases has made me write this short manual which wiil stand as
a serving point to direct your attention on the most important parts of Database
Management and Administration. The field being versatile has a twin which is
Database Development and they should not be confused. Read and Share.
""")

#Email input and button
gmail=st.text_input("""
Enter Gmail and download. Do come back to leave a comment and review anytime.
""", placeholder= "Enter mail")
submit_mail=st.button("Submit") 

if submit_mail:
    if gmail:
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="Download PDF Report",
            data=pdf_bytes,
            file_name=f"DBeng_{formatted_date}.pdf",
            mime="application/pdf",
        )
        conn = get_db()
        cur = conn.cursor()
        cur.execute(sql.SQL("INSERT INTO users (email) VALUES (%s);"), [gmail])
        conn.commit()
        st.success(f"inserted email: {gmail}")

    else:
        st.error("Please fill in your E-mail")
    if cur:
        cur.close()
    if conn:
        conn.close()


@st.dialog("Response/Feedback")
def submit_response():
    feedback= st.text_area(label="Enter Feedback", placeholder="My Review")
    rating= st.text_input(label="Rate Over 10", max_chars=2)
    response= st.button("Submit Response")

    if response:
        if feedback and rating:
            if gmail:
                conn = get_db()
                cur = conn.cursor()
                cur.execute(sql.SQL("UPDATE users SET feedback = %s, rating = %s WHERE email = %s;"), [feedback, rating, gmail])
                conn.commit()
                cur.close()
                conn.close()
            else:
                st.error("Please fill in your E-mail from Main Page")
            

        
if st.button("Submit Review"):
    submit_response()