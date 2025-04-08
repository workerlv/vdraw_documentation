from scripts.examples.example_images import draw_3_predefined_figures
from vdraw.semantic_segmentation.utils import clean, find
import streamlit as st
from PIL import Image
import numpy as np
import cv2


# TODO: FIX CORRECT SIDEBAR
def sidebar():
    st.sidebar.divider()
    st.sidebar.subheader("parameters:")
    mask = st.sidebar.file_uploader("Upload binary mask", type=["jpg", "jpeg", "png"])
    color_r = st.sidebar.number_input("Red", min_value=0, max_value=255, value=120)
    color_g = st.sidebar.number_input("Green", min_value=0, max_value=255, value=120)
    color_b = st.sidebar.number_input("Blue", min_value=0, max_value=255, value=120)
    color = (color_b, color_g, color_r)
    expand_mask = st.sidebar.number_input("Expand mask", value=120)

    return mask, color, expand_mask


def documentation():
    st.divider()
    st.subheader("out_of_bounds_bbox()")
    st.write("parameters:")
    st.code(
        """
        bbox: BBox object.
        image: RGB image as a NumPy array.
        """
    )
    st.write("returns:")
    st.code("Clipped BBox object")


def raw_usage():
    st.divider()
    st.write("example:")
    st.code(
        """
        # import find for finding bboxes and clean for out of bounds bboxes cliping
        from vdraw.semantic_segmentation.utils import clean, find
        
        mask = draw_3_predefined_figures() # mask from examples (you can upload your own mask)
        
        all_bboxes = find.mask_bboxes(mask) # returns list of bounding boxes (BBox objects)
        
        for bbox in all_bboxes:
            bbox.expand(120) # expand bboxes for example purposes
        
        # draw bounding boxes on mask (optional)
        debug_find_img = mask.copy()
        for bbox in all_bboxes:
            debug_find_img = bbox.draw_bbox(debug_find_img, color=(120, 120, 120))
        
        # returns new bbox with clipped coordinates (if out of bounds)
        # draw new bbox on mask (optional)    
        debug_clipped_img = mask.copy()
        for bbox in all_bboxes:
            clipped_bbox = clean.out_of_bounds_bbox(bbox, debug_clipped_img)
            debug_clipped_img = clipped_bbox.draw_bbox(debug_clipped_img, color=color)
        """
    )

    uploaded_mask, color, expand_mask = sidebar()

    if uploaded_mask is None:
        mask = draw_3_predefined_figures()
    else:
        mask = np.array(Image.open(uploaded_mask))
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    all_bboxes = find.mask_bboxes(mask)

    for bbox in all_bboxes:
        bbox.expand(expand_mask)

    debug_find_img = mask.copy()
    for bbox in all_bboxes:
        debug_find_img = bbox.draw_bbox(debug_find_img, color=color)

    debug_clipped_img = mask.copy()
    for bbox in all_bboxes:
        clipped_bbox = clean.out_of_bounds_bbox(bbox, debug_clipped_img)
        debug_clipped_img = clipped_bbox.draw_bbox(debug_clipped_img, color=color)

    col_1, col_2, col_3 = st.columns(3)

    col_1.image(mask, caption="input mask")
    col_2.image(debug_find_img, caption="image with raw expanded bboxes")
    col_3.image(debug_clipped_img, caption="image with clipped bboxes")
