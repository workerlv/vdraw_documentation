from pathlib import Path
import streamlit as st
import importlib

EXAMPLES = {
    "BBox": "bbox",
    "Clean -> combine overlapping bboxes": "clean_combine_overlapping_bboxes",
    "Clean -> out of bounds bbox": "clean_out_of_bounds_bbox",
    "Clean -> small bboxes out of list": "clean_small_bboxes_out_of_list",
    "Draw -> overlay segmentation mask": "draw_overlay_segmentation_mask",
    "Find -> largest combined bbox": "find_largest_combined_bbox",
    "Find -> mask bboxes": "find_mask_bbox",
}


def sidebar():
    selected_function = st.sidebar.selectbox("Select example", EXAMPLES.keys())
    return selected_function


def display_function(selected_function):
    module = importlib.import_module(f"scripts.examples.{EXAMPLES[selected_function]}")
    module.documentation()
    module.raw_usage()


def main():
    st.header("Semantic Segmentation")

    selected_function = sidebar()
    display_function(selected_function)


if __name__ == "__main__":
    main()
