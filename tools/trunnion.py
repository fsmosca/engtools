import streamlit as st
import math
from streamlit import session_state as ss
import pandas as pd


# Creating the dataframe
data = {
    "Nom. Size (inch)": [0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24],
    "Dia. (mm)": [21.3, 26.7, 33.4, 48.3, 60.3, 88.9, 114.3, 168.3, 219.1, 273.1, 323.9, 355.6, 406.4, 457.2, 508.0, 609.6],
    "Wall thk. (mm)": [3.73, 3.91, 4.55, 5.08, 5.54, 7.62, 8.56, 10.97, 12.7, 12.7, 14.27, 15.09, 16.66, 14.27, 15.09, 14.27],
    "Schedule": ["80S", "80S", "80S", "80S", "80S", "80S", "80S", "80S", "80S", "60", "60", "60", "60", "40", "40", "30"]
}


def find_circle_line_intersection(radius, x_value):
    y_squared = radius**2 - x_value**2
    y1 = math.sqrt(y_squared)

    return radius - y1


st.markdown('''### TCL Calculator''')
with st.form('form',clear_on_submit=False, enter_to_submit=False):
    st.number_input('Input Trunnion Distance from Pipe CL', value=400.0, min_value=50.0, max_value=2000.0, step=0.1, key='dclk')
    st.number_input('Input Pipe OD', value=114.3, min_value=50.0, max_value=800.0, step=0.1, key='podk')
    st.number_input('Input Wear Plate Thickness', min_value=0.0, max_value=150.0, step=0.1, key='wptk')
    st.number_input('Input Trunnion OD', value=88.9, min_value=25.0, max_value=600.0, step=0.1, key='todk')
    cal = st.form_submit_button('Calculate', type='primary')

if cal:
    r = st.session_state.podk/2 + st.session_state.wptk
    tr = st.session_state.todk/2
    dcl = ss.dclk

    ss.tlen = ss.dclk

    with st.container(border=True):
        if tr >= r:
            st.error('Error, Trunnion OD must be less than Pipe OD.')
        else:
            res = find_circle_line_intersection(r, st.session_state.todk/2)
            tcl = dcl - r + res
            st.markdown(f'TCL: **{round(tcl, 1)}**')


df = pd.DataFrame(data)
st.markdown('''### Pipe Dimensions''')
st.dataframe(df, hide_index=True, use_container_width=True)