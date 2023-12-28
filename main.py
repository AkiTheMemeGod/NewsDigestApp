import streamlit as st
import requests as rs
import os
st.set_page_config(layout="wide", page_title="Daily News")
api_key = os.getenv('NEWSAPI')
sortby_options = ["relevancy", "popularity", "publishedAt"]
c1, c2, c3 = st.columns([4, 3, 3])
with c2:
    st.title("YOUR DAILY NEWS")
    st.markdown("###")
    st.markdown("###")


def fetch():
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy={sortBy}&apiKey={api_key}&language={language}"
    req = rs.get(url)
    cont = req.json()
    return cont


n1, n2 = st.columns([2, 1])
with n1:
    query = st.text_input(label="Read about ? ", placeholder="ex: 'Tesla'", on_change=fetch)
with n2:
    st.markdown("###")
    with st.expander("🛞 Filters"):
        limit = st.slider(label="Feed limit", min_value=0, max_value=100, step=10, on_change=fetch)
        sortBy = st.radio(label="Filter", options=sortby_options, on_change=fetch)
        language = st.radio(label="language", options=["en", "es", "fr", "ru"], on_change=fetch)
    st.markdown("###")
    st.markdown("###")
n1, n2, n3 = st.columns(3)
content = fetch()
try:
    with n1:
        for article in content["articles"][0:round((int(limit))/3)]:
            if article is not None:
                with st.container(border=1):
                    st.subheader(f':blue[{article["title"]}]')
                    st.markdown("---")
                    st.write(article["description"])
                    st.markdown("###")
                    st.info(f':green[{article["url"]}]')
            st.markdown("###")

    with n2:
        for article in content["articles"][round((int(limit))/3)-1:round(2*(int(limit))/3)]:
            if article is not None:
                with st.container(border=1):
                    st.subheader(f':blue[{article["title"]}]')
                    st.markdown("---")
                    st.write(article["description"])
                    st.markdown("###")
                    st.info(f':green[{article["url"]}]')
            st.markdown("###")
    with n3:
        for article in content["articles"][round(2*(int(limit))/3):int(limit)]:
            if article is not None:
                with st.container(border=1):
                    st.subheader(f':blue[{article["title"]}]')
                    st.markdown("---")
                    st.write(article["description"])
                    st.markdown("###")
                    st.info(f':green[{article["url"]}]')
            st.markdown("###")
except KeyError:
    with n2:
        st.markdown("###")
        st.markdown("###")
        st.markdown("###")
        st.markdown("###")
        st.markdown("###")
        st.markdown("###")
        st.markdown("###")
        st.info(" Try Searching for something in the searchbar", icon="📰")
