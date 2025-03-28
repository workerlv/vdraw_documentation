import streamlit as st

st.set_page_config(layout="wide")

st.header("V-Draw Documentation")

st.divider()
st.subheader("Quick intro:")
st.write(
    """
    V-Draw is a library with help tools for segmentation tasks.
    """
)
st.write(
    """
    This is interactive documentation for V-Draw. 
    Most of the functions you can try out with your own images.
    In future there will be more functions which will help you segmentation visualization.
    Currently project is in development phase and first tools are made for semantic segmentation.
    """
)

st.divider()
st.subheader("How to use:")
st.write("Project is uploaded on PyPi and can be installed with pip:")
st.code("pip install vdraw")
st.write(
    "Choose 'Semantic segmentation' on sidebar and choose function you want to test from dropdown menu."
)
