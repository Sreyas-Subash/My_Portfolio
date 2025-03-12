import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
from webpages.career_timeline import career_json

# lottie requests function
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# loading assets
robot_gif = load_lottieurl("https://lottie.host/0456ca17-ec67-449d-9566-132679a2963c/sMAxfvY3La.json")
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
data_viz_lottie = load_lottieurl("https://lottie.host/5b6c3945-86a7-4120-8e45-e1efcd35c70b/zWgh2uROdd.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
ai_lottie = load_lottieurl("https://lottie.host/69fa2dcb-0a2d-4ddb-ab90-13be7d68e69e/7uPt1Zs8f4.json")
support_tootls_lottie = load_lottieurl("https://lottie.host/5daf12d3-41ea-4bad-b5c5-ec28636b2e6f/auGCfmg4MU.json")
analytics_lottie = load_lottieurl("https://lottie.host/6eb53da2-910a-4734-b893-afdac4c62fc2/KnwvG38yD5.json")

# pic, intro
col1, col2, col3 = st.columns([0.15, 0.6, 0.15], gap="small", vertical_alignment="center", border=False)
with col1:
    st.image("assets/my_pic.png", width=230)
    pass
with col2:
    st.title("Sreyas Subash", anchor=False)
    st.write(
        """An individual with great interpersonal and leadership skills.
         Good understanding and proficiency in SQL, spreadsheets, Excel, Power BI and Python.
          Believes in life long learning.
          An ardent football fan. Finding ways to connect football and statistics."""
    )
with col3:
    st_lottie(robot_gif, height=200, width=200, key="robo", speed=2.5)

# -----------------career timeline------------------ #
with st.container():
    st.write("---")
    st.write("### 💼⏳ Career Timeline")
    # Display timeline
    timeline(career_json, height=540)


# ----------------- skillset ----------------- #
with st.container():
    st.write("---")
    st.write('### ⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=120,width=120, key="python", speed=2.5)
    with col2:
        st_lottie(data_viz_lottie, height=120,width=120, key="java", speed=2.5)
    with col3:
        st_lottie(my_sql_lottie,height=120,width=120, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=120,width=120, key="git", speed=2.5)
    with col1:
        # st_lottie(github_lottie,height=120,width=120, key="github", speed=1)
        st.image("assets/github1.png", width=125)
    with col2:
        st_lottie(ai_lottie,height=120,width=120, key="docker", speed=2.5)
    with col3:
        st_lottie(support_tootls_lottie,height=135,width=135, key="figma", speed=2.5)
    with col4:
        st_lottie(analytics_lottie,height=130,width=130, key="js", speed=1)




