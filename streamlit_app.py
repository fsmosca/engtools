import streamlit as st
from streamlit import session_state as ss
import time


st.set_page_config(layout='centered')


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    with st.form('form_login', clear_on_submit=True, enter_to_submit=False):
        username = st.text_input('Username')
        pw = st.text_input('Password', type='password')
        is_login = st.form_submit_button('Login', type='primary')

    if is_login:
        if username == st.secrets['USERNAME'] and pw == st.secrets['PASSWORD']:
            ss.logged_in = True
            st.rerun()
        else:
            st.error('Incorrect username or password.')
            time.sleep(1)
            st.rerun()


def logout():
    if st.button("Log out", type='primary'):
        st.session_state.logged_in = False
        st.rerun()


login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
trunnion = st.Page("tools/trunnion.py", title="Trunnion", icon=":material/arrow_upward:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Tools": [trunnion],
        }
    )
else:
    pg = st.navigation([login_page])


pg.run()
