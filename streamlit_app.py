import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon=":wave:" , layout="wide")

## Page setup
about_me = st.Page(
    page="webpages/about_me.py",
    title="About Me",
    icon=":material/face:",
    default=True,
)

face_filter = st.Page(
    page="webpages/face_filter.py",
    title="face_filter",
    icon=":material/smart_toy:"
)

## Navigation setup
pg = st.navigation(
    {
        "Info":[about_me],
        "Projects":[face_filter],
    }
)


# st.sidebar.markdown("<br><br><br>" * 5, unsafe_allow_html=True)
# ## Sidebar
# st.sidebar.text(
#     '"If my mind can conceive it and my heart can believe it - Then I can achieve it"'
# )

pg.run()