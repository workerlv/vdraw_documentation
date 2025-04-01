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
    min_width = st.sidebar.number_input("Min width", value=150)
    min_height = st.sidebar.number_input("Min height", value=150)

    return mask, min_width, min_height


def documentation():
    st.divider()
    st.subheader("small_bboxes_out_of_list()")
    st.write("parameters:")
    st.code(
        """
        bboxes: List of BBox objects.
        min_width: Minimum width of the bounding box (Optional)
        min_height: Minimum height of the bounding box (Optional)
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
            debug_find_img = bbox.draw_bbox(debug_find_img, color=(120, 120, 120))
        
        # returns list of combined bounding boxes (BBox objects)
         without_small_bboxes = clean.small_bboxes_out_of_list(all_bboxes, min_width, min_height)
        
        # draw combined bounding boxes on mask (optional)
        debug_img = mask.copy()
        for bbox in without_small_bboxes:
            debug_img = bbox.draw_bbox(debug_img, color=(120, 120, 120))
        
        """
    )

    uploaded_mask, min_width, min_height = sidebar()

    if uploaded_mask is None:
        mask = draw_3_predefined_figures()
    else:
        mask = np.array(Image.open(uploaded_mask))
        if len(mask.shape) == 3:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    all_bboxes = find.mask_bboxes(mask)

    debug_find_img = mask.copy()
    for bbox in all_bboxes:
        debug_find_img = bbox.draw_bbox(debug_find_img, color=(120, 120, 120))

    without_small_bboxes = clean.small_bboxes_out_of_list(
        all_bboxes, min_width, min_height
    )

    debug_img = mask.copy()
    for bbox in without_small_bboxes:
        debug_img = bbox.draw_bbox(debug_img, color=(120, 120, 120))

    col_1, col_2, col_3 = st.columns(3)

    col_1.image(mask, caption="input mask")
    col_2.image(debug_find_img, caption="image with raw bboxes")
    col_2.image(debug_img, caption="image without small bboxes")

    with col_3:
        st.write("bboxes result:")
        st.write(all_bboxes)
        st.write("combined bboxes result:")
        st.write(without_small_bboxes)
