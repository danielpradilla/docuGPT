import streamlit as st
import requests
import time     


def app():  
    if "linkkk" not in st.session_state:
        st.session_state["linkkk"] = ""
    st.set_page_config(page_title="docuGPT", page_icon=":robot_face:", layout="centered")
    st.title('Welcome to docuGPT! 🥳')

    st.text_input(label="Please enter the link below: ", key="link", placeholder="https://wipo.int/...")
    if st.button("Submit :heart:"):
        if check_link(st.session_state.link):
            # if "link" not in st.session_state:
            #     st.session_state.link = "{}".format(st.session_state.link)
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.linkkk = st.session_state.link
            st.balloons()
            st.success("✅ Link is submitted. ✅")
            st.markdown("## Please head over to Interact to interact with your Docs. :muscle:")
            if "link_submitted" not in st.session_state:
                st.session_state["link_submitted"] = "Done"
        else:
            st.warning("❌ Link is not valid. Please try again. ❌")
            st.write("Format: https://readthedocs.io/... or https://wipo.int/...")

def check_link(link):
    if link == "" or link == None:
        return False
    if "wipo.int" not in link and "readthedocs.io" not in link:
        return False
    else:
        progress_bar()
        try:
            r = requests.get(link)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError) as error:
            return False
        if r.status_code == 200:
            return True
        else:
            return False

def progress_bar():
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.0055)
        progress_bar.progress(i + 1)    



if __name__ == "__main__":
    app()



