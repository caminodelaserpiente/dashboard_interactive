import streamlit as st


def css(): 
    
    st.markdown(
        """
        <style>
        footer {
            visibility: hidden;
        }
        </style>
        
        <style>
            .st-emotion-cache-15yi2hn p:nth-child(2) {
                display: none;
            }
        </style>

        """,
        unsafe_allow_html=True
    )
