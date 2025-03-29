import streamlit as st
import math
from streamlit import session_state as ss
import pandas as pd


st.markdown(
    """
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def find_circle_line_intersection(radius, x_value):
    y_squared = radius**2 - x_value**2
    y1 = math.sqrt(y_squared)

    return radius - y1


pipe_data = pd.read_csv("./data/pipedata.csv")
dn_list = pipe_data['DN'].tolist()

st.markdown('''### TCL Calculator''')
with st.form('form',clear_on_submit=False, enter_to_submit=False):
    c1, c2 = st.columns(2)
    with c1:
        st.selectbox('☀️ Select Pipe DN', options=dn_list, index=12, key='podk')
        st.number_input('Wear Plate Thickness',
                        min_value=0.0, max_value=150.0, step=0.1, key='wptk',
                        help='Input wear plate thickness if there is. If it is an RPad do not input.')
    with c2:
        st.selectbox('⭕ Select Trunnion DN', options=dn_list, index=10, key='todk')
        st.number_input('Input Trunnion Distance from top of plate to Pipe CL',
                        value=400.0, min_value=50.0, max_value=2000.0, step=0.1, key='dclk')
    cal = st.form_submit_button('Calculate', type='primary')

if cal:
    dn = ss.podk
    od = pipe_data.loc[pipe_data['DN'] == dn, 'OD'].values[0]
    r = od/2 + st.session_state.wptk

    tdn = ss.todk
    tod = pipe_data.loc[pipe_data['DN'] == tdn, 'OD'].values[0]
    tr = tod/2
    dcl = ss.dclk

    ss.tlen = ss.dclk

    with st.container(border=True):
        if tr >= r:
            st.error('Error, Trunnion OD must be less than Pipe OD.')
        else:
            res = find_circle_line_intersection(r, st.session_state.todk/2)
            tcl = dcl - r + res
            st.markdown(f'TCL: **{round(tcl, 1)}**')
