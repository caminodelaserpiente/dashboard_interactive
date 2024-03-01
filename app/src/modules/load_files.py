import os
import json


import pandas as pd
import streamlit as st


def select_json(output_folder):
    json_files = [f for f in os.listdir(output_folder) if f.endswith(".json")]
    selected_file = st.selectbox("Select a JSON file:", 
                            json_files
                            )
    with open(os.path.join(output_folder, selected_file), "r", encoding='utf-8') as document:
        data = json.load(document)
    return data


def select_df(json_data):
    df = pd.DataFrame(json_data['data'])
    df = pd.DataFrame({'username': json_data["data"]["username"],
                        'comment': json_data["data"]["comment"],
                        'emojis': [item[1] for item in json_data["data"]["comment_and_emojis"]],
                        'date_comment': json_data["data"]["date_comment"],
                        'likes_comment': json_data["data"]["likes_comment"],
                        'lang': json_data["data"]["lang"],
                        'emotion_comment': json_data["data"]["emotion_comment"],
                        'score_emotion': json_data["data"]["score_emotion"]}
                        )
    df['comment'].fillna('', inplace=True)
    df['emojis'] = df['emojis'].apply(lambda x: ''.join(x))
    df["likes_comment"] = df["likes_comment"].replace('', "0")
    df['score_emotion'] = pd.to_numeric(df['score_emotion'], errors='coerce')
    return df
