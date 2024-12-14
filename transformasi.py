import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
from PIL import Image

members = [
    {"name": "Kania Ananda Hendrajaya", "photo": "KAH.jpg", "id": "004202300035"},
    {"name": "Nayla Chairunnisa Putri Hermawan", "photo": "NCPH.jpg", "id": "004202300026"},
    {"name": "Rameyza Bertalenta", "photo": "RB.jpg", "id": "004202300039"},
    {"name": "Resi Ayu Jenar", "photo": "RAJ.JPG", "id": "004202300019"}
]

# halaman tranformation
def apply_transformations(image, scale_factor, angle, tx, ty, skew_x, skew_y):
    h, w = image.shape[:2]

    #Scaling Function
    image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

    #Rotation Function
    rot_matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    image = cv2.warpAffine(image, rot_matrix, (w, h))

    #Translation Function
    trans_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    image = cv2.warpAffine(image, trans_matrix, (w, h))

    #Skewing Function
    skew_matrix = np.float32([
        [1, skew_x, 0],
        [skew_y, 1, 0]
    ])
    image = cv2.warpAffine(image, skew_matrix, (w, h))

    return image

#web
st.set_page_config(page_title="Digital Image Editing", layout="wide", page_icon="favicon.ico")

# navigation
st.sidebar.title("Find your needs")
page = st.sidebar.radio("Go to", ["Home", "Group Members", "Upload Photo & Transform"])

if page == "Upload Photo & Transform":
    st.title("Digital Image Editing")

    # Upload file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        # Read the image
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        st.sidebar.header("Transformations")

        # Scaling
        scale_factor = st.sidebar.slider("Scaling Factor", 0.1, 3.0, 1.0)

        # Rotation
        angle = st.sidebar.slider("Rotation Angle", -180, 180, 0)

        # Translation
        tx = st.sidebar.slider("Translate X", -200, 200, 0)
        ty = st.sidebar.slider("Translate Y", -200, 200, 0)

        # Skewing
        skew_x = st.sidebar.slider("Skew X", -0.5, 0.5, 0.0, 0.01)
        skew_y = st.sidebar.slider("Skew Y", -0.5, 0.5, 0.0, 0.01)

        # Apply transformations
        transformed_image = apply_transformations(image_np, scale_factor, angle, tx, ty, skew_x, skew_y)

        #Original and Transformed
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)

        with col2:
            st.subheader("Transformed Image")
            st.image(transformed_image, caption="Transformed Image", use_container_width=True)

#page 1
elif page == "Home":
    col1, col2 = st.columns([3, 7])
    with col1:
        st.image("President_University_Logo.png", width=220)
    with col2:
        st.title("Edit Your Image with")
        st.title("Digital Image Editing")
        background_color = "black"
        font_color = "white" if background_color == "black" else "black"
        st.markdown(
                f"""
                <p style='text-align: left; font-size: 20px; color: white; font-family: Roboto, times new roman;'
                >{"From Now On, You can do Image Processing as fast as possible by just upload your image here. This web is specially made by Group 3 just for you!!"}
                </p>
                """,
                unsafe_allow_html=True
            )
#page 2
elif page == "Group Members":
    st.title("Group 3")
    st.subheader("Industrial Engineering Class 3")
    st.subheader("Members:")
    for member in members:
        st.image(member["photo"], width=180)
        background_color = "black"
        font_color = "white" if background_color == "black" else "black"
        st.markdown(
            f"""
            <p style='text-align: left; font-size: 25px; color: white; font-family: Roboto, times new roman;'>{member['name']}</p>
            <p style='text-align: left; font-size: 20px; color: white; font-family: Roboto, times new roman;'>SID: {member['id']}</p>
            """,
            unsafe_allow_html=True
        )
