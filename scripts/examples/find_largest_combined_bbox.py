from scripts.examples.example_images import draw_3_predefined_figures
from vdraw.semantic_segmentation.utils import find
import streamlit as st
from PIL import Image
import numpy as np
import cv2


def sidebar():
    st.sidebar.divider()
    st.sidebar.subheader("parameters:")
    mask = st.sidebar.file_uploader("Upload mask", type=["jpg", "jpeg", "png"])
    color_r = st.sidebar.number_input("Red", min_value=0, max_value=255, value=120)
    color_g = st.sidebar.number_input("Green", min_value=0, max_value=255, value=120)
    color_b = st.sidebar.number_input("Blue", min_value=0, max_value=255, value=120)
    color = (color_b, color_g, color_r)
    st.sidebar.write("Save image in path (use locally)")

    return mask, color


def documentation():
    st.divider()
    st.subheader("largest_combined_bbox()")

    st.write("parameters:")
    st.code(
        """ 
            mask: np.ndarray => segmentation mask as a NumPy array (grayscale or binary)
            save_image_in_path => if provided, saves the image with bounding boxes at the given path (optional)
        """
    )
    st.write("returns:")
    st.code("BBox object")


def raw_usage():
    st.subheader("Example:")

    st.code(
        """
            from vdraw.semantic_segmentation.utils import find

            mask = draw_3_predefined_figures()  # example image (random mask from examples)
            bboxes = find.largest_combined_bbox(mask) # returns largest combined bounding box (BBox objects)
            
            # draw bounding boxes on mask (optional)
            debug_image = mask.copy()
            debug_image = bbox.draw_bbox(debug_image, color=(120, 120, 120))
        """
    )

    uploaded_mask, color = sidebar()

    if uploaded_mask is None:
        mask = draw_3_predefined_figures()
    else:
        mask = np.array(Image.open(uploaded_mask))
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    bbox = find.largest_combined_bbox(mask)

    debug_image = mask.copy()
    debug_image = bbox.draw_bbox(debug_image, color=color)

    col_1, col_2, col_3 = st.columns(3)

    col_1.image(mask, caption="input mask")
    col_2.image(debug_image, caption="image with bbox")

    with col_3:
        st.write("bbox result:")
        st.write(bbox.get_dict())
