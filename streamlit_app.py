import streamlit as st
import pandas as pd
import numpy as np

import urllib.request
import re
import random

import pandas as pd
import numpy as np




st.set_page_config(
        page_title="Dancing Panda",
        page_icon=":bear:",
        initial_sidebar_state="expanded",
    )

st.title('Dancing Panda')
st.markdown("![Dancing Panda](https://tenor.com/view/panda-dance-cute-dancing-happy-dance-gif-13886194.gif)")

st.header("Let's learn some dance moves today")


title = st.text_input('Enter the song', 'Believer')
#st.write('The current song is ', title)

title = title.replace(" ", "")
search_keyword = title +"dance"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

yt_suggestion = "https://www.youtube.com/watch?v=" + random.choice(video_ids)
#print("youtube link", yt_suggestion)

if st.button("Get a youtube dance suggestion"):
    st.write(yt_suggestion)
else:
    pass

if st.button("Get a 3-D generated dance video based on song type predicted using Spotify API"):
    st.write("3D video: ")
    st.write("Predicted medium group")
    vidoe_file = open("break.mov", 'rb')
    video_bytes = vidoe_file.read()

    st.video(video_bytes)

else:
    pass


if st.button("Get a step-by-step tutorial"):
    st.write("Step-by-step: ")

    vidoe_file = open("tutorial.mp4", 'rb')
    video_bytes = vidoe_file.read()

    st.video(video_bytes)

else:
    pass