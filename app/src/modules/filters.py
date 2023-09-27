import streamlit as st


def filter_words():
    if 'words_filter' not in st.session_state:
        st.session_state.words_filter = []

    word = st.text_input("Enter a word to filter comments", 
                            value="", 
                            placeholder="Enter a word to filter comments",
                            label_visibility="visible"
                        )
        
    if word.strip() != "" and word.strip() != "Write your word" and word not in st.session_state.words_filter:
        st.session_state.words_filter.append(word)

    container2 = st.container()
    
    if st.button("Reset", key="rest"):
        st.session_state.words_filter = []
        st.success("The list has been successfully reset.")

    options = container2.multiselect(
        'Filter by words',
        st.session_state.words_filter,
        st.session_state.words_filter
    )

    return options
    


def filter_emotion():
    genre = st.radio(
        "Filter emotion",
        ["ALL", "POS", "NEU", "NEG"],
        captions = None
        )
    if genre != 'ALL':
        emotio = []
        emotio.append(genre)
        return emotio
    else:
        emotion = ['POS', 'NEU', 'NEG']
        return emotion
