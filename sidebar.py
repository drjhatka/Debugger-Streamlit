import streamlit as st


def sidebar():
    with st.sidebar:
        st.sidebar.subheader("Upload your code error screenshot here", width="stretch")
        images =st.sidebar.file_uploader("Upload your code error screenshot here", 
                                         accept_multiple_files=True, 
                                         type=["jpg", "jpeg", "png"],
                                         key="file_uploader") 
        if images:
            col = st.columns(len(images))
            for i, image in enumerate(images):
                with col[i]:
                    st.image(image, caption=f"Uploaded Image {i+1}")
        
        
        selected_option = st.selectbox("Select the type of assistance you need:", 
                                       options=["Get Hints", "Solution with code fix"], index=None,
                                       placeholder="Select an option")
        
        clicked = st.button("Debug Code", type="primary", width="stretch")
        
        with st.expander("Instructions", expanded=False, ):
            st.markdown("1. Click the 'Browse files' button to upload your code error screenshot from your device.")
            st.markdown("2. After selecting the file, select if you want hint for the error or complete error fix.")
        
    return clicked, selected_option, images

            
           

        