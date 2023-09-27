import pandas as pd
from pandas_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


from app.src.modules import *


def body():

    tab1, tab2 = st.tabs(["Comments", "Report"])
    with tab1:

        output_folder = './data'
        json_file = select_json(output_folder)
        st.json(json_file, expanded=False)
        st.write('---')
        
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                df = select_df(json_file)
                emotion_filter = filter_emotion()
                filter_df_emotion = df['emotion_comment'].isin(emotion_filter)
                df_filter = df[filter_df_emotion]
                words_filter = filter_words()
                filter_df_words = df_filter['comment'].str.contains('|'.join(words_filter), case=False)
                df_filter = df_filter[filter_df_words]
            with col2:
                st.dataframe(df_filter)

        with st.expander("Análisis de sentimiento en comentarios", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                pie_chart_emotions(df_filter)
            with col2:
                box_plot_emotions(df)

        with st.expander("Comentarios", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                bar_chart_top_words(df_filter)
            with col2:
                wordcloud_words(df_filter)

        with st.expander("Emojis", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                bar_chart_top_emoji(df_filter)
            with col2:
                wordcloud_emojis(df_filter)

    with tab2:

        with st.expander("Report", expanded=True):
            profile = ProfileReport(df, minimal=True)
            st_profile_report(profile)
