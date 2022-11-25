import streamlit as st
import requests
import json
from datetime import datetime

URL = "http://localhost:8000"
BASE = "/api/v1"
USERS = "/users"
GAMES = "/games"

data = {
                "user_id": "637cbaf4c5c95d5ad268db93",
                "last_word": "",
                "history": [],
                "total_score": 0,
                "creation_date": str(datetime.now()),
                "update": False,
                "update_time": str(datetime.now()),
                "status": "1",
            }
data = json.dumps(data)

with st.container():
    st.title("Word Chains Game")
    if st.button("Start") and "start" not in st.session_state:
        st.session_state['start'] = True
        game = requests.post(
            f"{URL}{BASE}{GAMES}/",
            data=data
        )
        game = json.loads(game.text)
        st.session_state['game_id'] = game["_id"]

with st.container():
    if "start" in st.session_state:
        st.write(f"Game_id: {st.session_state['game_id']}")
        player_word = st.text_input("Write a word")
        if st.button("Play"):
            if len(player_word) != 0:
                game = requests.get(f"{URL}{BASE}{GAMES}/{st.session_state['game_id']}")
                st.session_state['last_word'] = json.loads(game.text)['last_word']
                payload = {
                    "id": st.session_state['game_id'],
                    "word": player_word
                }
                game = requests.post(
                    f"{URL}{BASE}{GAMES}/play",
                    data=str(game.text),
                    params=payload
                )
                if game.status_code != 200:
                    st.write(f"Not a valid word or already used, try again . Last word is: {st.session_state['last_word']}")
                else:
                    payload = {
                        "id": st.session_state['game_id']
                    }
                    update = requests.put(
                        f"{URL}{BASE}{GAMES}/",
                        data=str(game.text),
                        params=payload
                    )
                    new_word = json.loads(game.text)['last_word']

                    st.write(new_word)
