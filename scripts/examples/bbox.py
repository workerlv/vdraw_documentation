from vdraw.semantic_segmentation.bbox import BBox
import streamlit as st
import numpy as np


def documentation():
    st.divider()
    st.subheader("Properties:")  # -------------------------------------------------

    st.code(f"x1     => x coordinate of the top left corner")
    st.code(f"y1     => y coordinate of the top left corner")
    st.code(f"width  => width of the bounding box")
    st.code(f"height => height of the bounding box ")
    st.code(
        f"x2     => x coordinate of the bottom right corner (calculated from x_1 and width)"
    )
    st.code(
        f"y2     => y coordinate of the bottom right corner (calculated from y_1 and height)"
    )

    st.divider()
    st.subheader("Methods:")  # ----------------------------------------------------

    st.code("get_XYXY_list() => returns a list of [x1, y1, x2, y2] coordinates")
    st.code("get_XYWH_list() => returns a list of [x1, y1, width, height] coordinates")
    st.code(
        "get_dict() => returns a dictionary of => x1 / x2 / y1 / y2 / width / height"
    )
    st.code(
        """
            draw_bbox()     => draws a bounding box on an image
            
              parameters:
                image: np.ndarray => image to draw bounding box on
                color=(120, 120, 120) => (tuple) color to use for bounding box (optional)
                thickness=5 => (int) thickness to use for bounding box (optional)
                save_image_in_path: str = None => (string) path to save image (optional)
            """
    )
    st.code(
        """
        expand_horizontally() => expands the bounding box horizontally by a given amount

          parameters:
            amount: int => amount to expand the bounding box horizontally
        """
    )

    st.code(
        """
        expand_vertically() => expands the bounding box vertically by a given amount

          parameters:
            amount: int => amount to expand the bounding box vertically
        """
    )

    st.code(
        """
        expand() => expands the bounding box in all directions by a given amount

          parameters:
            amount: int => amount to expand the bounding box in all directions
        """
    )


def raw_usage():

    st.divider()
    st.subheader("Examples")  # ---------------------------------------------------

    with st.echo():
        new_bbox = BBox(x1=50, y1=50, width=100, height=100)  # create new BBox

        st.write(
            f"get_XYXY_list() result = {new_bbox.get_XYXY_list()}"
        )  # print x1, y1, x2, y2 coordinates

    with st.echo():
        st.write(
            f"get_XYWH_list() result = {new_bbox.get_XYWH_list()}"
        )  # print x1, y1, width, height

    with st.echo():
        st.write(f"get_dict() result = {new_bbox.get_dict()}")  # print dictionary

    with st.echo():
        empty_image = np.zeros((300, 300, 3), dtype=np.uint8)  # create empty image
        image_with_bounding_box = new_bbox.draw_bbox(
            empty_image
        )  # draw bounding box on empty image
        st.image(image_with_bounding_box)  # display image

    with st.echo():
        new_bbox.expand(
            20
        )  # expand previously created bounding box by 20 pixels in all directions

        image_with_additional_bbox = new_bbox.draw_bbox(
            image_with_bounding_box, color=(0, 255, 0)
        )  # draw additional bounding box on previously created image

        st.image(
            image_with_additional_bbox,
            caption="gray original bbox and green expanded bbox",
        )
