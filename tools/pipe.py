import streamlit as st
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


pipe_data = pd.read_csv("./data/pipedata.csv")

st.markdown('''### Pipe Dimensions''')
st.dataframe(
    pipe_data,
    column_config={
        "DN": st.column_config.Column(
            pinned=True,
        ),
        "NPS": st.column_config.Column(
            pinned=True,
        ),
        "OD": st.column_config.Column(
            pinned=True,
        )
    },
    hide_index=True,
    use_container_width=True,
    # height=250
)
