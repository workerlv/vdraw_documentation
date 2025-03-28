from scripts.examples.example_images import draw_3_predefined_figures
from vdraw.semantic_segmentation.utils import clean, find
import streamlit as st
from PIL import Image
import numpy as np
import cv2


def sidebar():
    st.sidebar.divider()
    st.sidebar.subheader("parameters:")
    mask = st.sidebar.file_uploader("Upload binary mask", type=["jpg", "jpeg", "png"])
    color_r = st.sidebar.number_input("Red", min_value=0, max_value=255, value=120)
    color_g = st.sidebar.number_input("Green", min_value=0, max_value=255, value=120)
    color_b = st.sidebar.number_input("Blue", min_value=0, max_value=255, value=120)
    color = (color_b, color_g, color_r)
    st.sidebar.write("Save image in path (use locally)")

    return mask, color


def documentation():
    st.divider()
    st.subheader("combine_overlapping_bboxes()")
    st.write("parameters:")
    st.code(
        """
        bboxes: List of BBox objects.
        """
    )
    st.write("returns:")
    st.code("List of BBox objects [BBox, ...]")


def raw_usage():
    st.divider()
    st.write("example:")
    st.code(
        """
        # import find for finding bboxes and clean for combining overlapping bboxes
        from vdraw.semantic_segmentation.utils import clean, find
        
        mask = draw_3_predefined_figures() # mask from examples (you can upload your own mask)
        
        all_bboxes = find.mask_bboxes(mask) # returns list of bounding boxes (BBox objects)
        
        # draw bounding boxes on mask (optional)
        debug_find_img = mask.copy()
        for bbox in all_bboxes:
            debug_find_img = bbox.draw_bbox(debug_find_img)
        
        # returns list of combined bounding boxes (BBox objects)
        combined_bboxes = clean.combine_overlapping_bboxes(all_bboxes) 
        
        # draw combined bounding boxes on mask (optional)
        debug_comb_img = mask.copy()
        for bbox in combined_bboxes:
            debug_comb_img = bbox.draw_bbox(debug_comb_img)
        
        """
    )

    uploaded_mask, color = sidebar()

    if uploaded_mask is None:
        mask = draw_3_predefined_figures()
    else:
        mask = np.array(Image.open(uploaded_mask))
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    all_bboxes = find.mask_bboxes(mask)

    debug_find_img = mask.copy()
    for bbox in all_bboxes:
        debug_find_img = bbox.draw_bbox(debug_find_img, color=color)

    combined_bboxes = clean.combine_overlapping_bboxes(all_bboxes)

    debug_comb_img = mask.copy()
    for bbox in combined_bboxes:
        debug_comb_img = bbox.draw_bbox(debug_comb_img, color=color)

    col_1, col_2, col_3 = st.columns(3)

    col_1.image(mask, caption="input mask")
    col_2.image(debug_find_img, caption="image with raw bboxes")
    col_2.image(debug_comb_img, caption="image with combined bboxes")

    with col_3:
        st.write("bboxes result:")
        st.write(all_bboxes)
        st.write("combined bboxes result:")
        st.write(combined_bboxes)
