import streamlit as st

def app():
    with st.sidebar.form(key='my_form'):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            submit_button = st.form_submit_button(label='Login')