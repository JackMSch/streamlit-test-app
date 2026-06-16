import streamlit as st
import datetime

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Shawty like a melody some lyrics i dont remember")

st.autorefresh(interval=1000)
st.write(datetime.time)