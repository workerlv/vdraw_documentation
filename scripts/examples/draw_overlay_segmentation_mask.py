from vdraw.semantic_segmentation.utils import draw
import streamlit as st
from PIL import Image
import numpy as np
import cv2


def sidebar():
    st.sidebar.divider()
    st.sidebar.subheader("parameters:")
    image = st.sidebar.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
    mask = st.sidebar.file_uploader("Upload mask", type=["jpg", "jpeg", "png"])
    color_r = st.sidebar.number_input("Red", min_value=0, max_value=255, value=0)
    color_g = st.sidebar.number_input("Green", min_value=0, max_value=255, value=255)
    color_b = st.sidebar.number_input("Blue", min_value=0, max_value=255, value=0)
    color = (color_b, color_g, color_r)
    alpha = st.sidebar.number_input("Alpha", min_value=0.0, max_value=1.0, value=0.6)
    st.sidebar.write("Save image in path (use locally)")

    return image, mask, color, alpha


def documentation():
    st.divider()
    st.subheader("overlay_segmentation_mask()")

    st.write("parameters:")
    st.code(
        """ 
            image: np.ndarray => image to overlay mask on
            mask: np.ndarray => mask to overlay on image
            color=(0, 255, 0) => (tuple) color to use for overlay (optional)
            alpha=0.6 => (float) alpha value to use for overlay (optional)
            save_image_in_path=None => (string) path to save image (optional)
        """
    )
    st.write("returns:")
    st.code("Image with overlayed mask.")

    st.write("example:")
    st.code(
        """ 
            from vdraw.semantic_segmentation.utils import draw
            
            image = cv2.imread("examples/dog.jpg")
            mask = cv2.imread("examples/dog_mask.png", cv2.IMREAD_GRAYSCALE)

            image_with_overlay = draw.overlay_segmentation_mask(image, mask)
        """
    )


def raw_usage():

    uploaded_image, uploaded_mask, color, alpha = sidebar()

    if uploaded_image is None:
        image = cv2.imread("examples/dog.jpg")
    else:
        image = cv2.cvtColor(np.array(Image.open(uploaded_image)), cv2.COLOR_RGB2BGR)

    if uploaded_mask is None:
        mask = cv2.imread("examples/dog_mask.png", cv2.IMREAD_GRAYSCALE)
    else:
        mask = np.array(Image.open(uploaded_mask))
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    image_with_overlay = draw.overlay_segmentation_mask(image, mask, color, alpha)

    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        st.write("image")
        st.image(image, channels="BGR")

    with col_2:
        st.write("mask")
        st.image(mask)

    with col_3:
        st.write("result")
        st.image(image_with_overlay, channels="BGR")
