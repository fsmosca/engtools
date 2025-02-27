import streamlit as st
from streamlit_navigation_bar import st_navbar
import math


def find_circle_line_intersection(radius, x_value):
    y_squared = radius**2 - x_value**2
    y1 = math.sqrt(y_squared)

    return radius - y1


page = st_navbar(["Home", "Trunnion", "About"])

if page == 'Home':
    st.markdown('**Home**')

elif page == 'Trunnion':
    st.markdown('**Trunnion**')

    with st.form('form',clear_on_submit=False, enter_to_submit=False):
        st.number_input('Input Pipe OD', min_value=50.0, max_value=800.0, step=0.1, key='podk')
        st.number_input('Input Wear Plate Thickness', min_value=0.0, max_value=150.0, step=0.1, key='wptk')
        st.number_input('Input Trunnion OD', min_value=25.0, max_value=600.0, step=0.1, key='todk')
        cal = st.form_submit_button('Calculate', type='primary')

    if cal:
        r = st.session_state.podk/2 + st.session_state.wptk
        tr = st.session_state.todk/2

        with st.container(border=True):
            if tr >= r:
                st.error('Error, Trunnion OD must be less than Pipe OD.')
            else:
                res = find_circle_line_intersection(r, st.session_state.todk/2)
                st.markdown(f'Distance from BOP or BOWP: **{round(res, 1)}**')

elif page == 'About':
    st.markdown('**About**')
