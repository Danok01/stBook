import streamlit as st
import DB

#st.set_page_config(page_title="DBE", layout="centered") # webpage name

st.title("Database Engineering")
st.write(
"""
My passion for Databases has made me write this short manual which wiil stand as
a serving point to direct your attention on the most important parts of Database
Management and Administration. The field being versatile has a twin which is
Database Development and they should not be confused. Read and Share.
""")
gmail=st.text_input("""
Enter Gmail and download. Do come back to leave a comment and review anytime.
""", placeholder= "Enter mail")


if st.button("Submit"):
    st.button("Download PDF")
    #st.download_button(label="Download PDF", file_name="DBeng.pdf")

    st.text_area(label="Enter Feedback", placeholder="My Review")
    st.number_input(label="Rate Over 10", min_value=1, max_value=10)
    st.button("Submit Response")
    DB.get_db(gmail)