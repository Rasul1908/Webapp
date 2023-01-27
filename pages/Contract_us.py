import pandas
import streamlit as st
from emailsender import send_email

st.header('Contact us')
df=pandas.read_csv('topics.csv')

with st.form(key='email_forms'):
    user_email=st.text_input('Your email address')
    user_selectbox=st.sidebar.selectbox('What is the topic of the discussion? ',df['topic'])
    user_email_message=st.text_area('Your email message')

    message = f"""\
Subject:App email from {user_email} regarding {user_selectbox}


Email from:{user_email}

{user_email_message}

Message completed

"""
    button=st.form_submit_button('Submit')

    if button:
        send_email(message)
        st.info('Successfully sent an email')


