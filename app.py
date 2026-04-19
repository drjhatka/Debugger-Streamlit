
from api_call import errorFixer 
from sidebar import sidebar as sidebar 
from streamlit import streamlit as st

from PIL import Image


st.set_page_config(layout="wide")
def run():
    with st.container(border=True, width="stretch"):
        st.markdown(
        "<h4 style='color: blue; margin-bottom: 10px;'>Code Debugger App</h4>",
        unsafe_allow_html=True
        )
     
     


#response = client.models.generate_content(model="gemini-2.5-flash", contents="What is the capital of France?")
# for model in client.models.list():
#     if "generateContent" in model.supported_actions:
#         print(f"- {model.name}")
#print(client.models.list().  )
# images =st.file_uploader("Upload your code error screenshot here", 
#                                          type=["jpg", "jpeg", "png"], accept_multiple_files=True, 
#                                          key="file_uploader") 
clicked, selected_option, images = sidebar()

print(len(images))
if images:
    response = errorFixer(images, selected_option)
run()
if  clicked:
    with st.container(border=True, width="stretch"):
        st.markdown(
        "<h6 style='color: blue; margin-bottom: 10px;'>Based on your input " \
        "here is a breakdown of the issue:</h6>",
        unsafe_allow_html=True
        )
        st.markdown(f"**Selected Option:** {selected_option} {response}")

#response