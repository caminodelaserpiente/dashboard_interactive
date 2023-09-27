import streamlit as st


def set_page_config():
    st.set_page_config(
        page_title="interactive-dashboard",
        page_icon= ":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'mailto:caminodelaserpiente.py@gmail.com',
            'Report a bug': None,
            'About': 'By. 蛇道 @caminodelaserpiente'
        }
    )


def header():
    with st.container():
        st.title("Interactive dashboard :bar_chart:", anchor=False)
        st.write("---")
