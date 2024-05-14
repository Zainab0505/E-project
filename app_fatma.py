import streamlit as st
from PIL import Image
#from streamlit_lottie import st_lottie (for graphics in further steps)
st.set_page_config(page_title='Piezoelectricity!', page_icon=":bulb:", layout="wide")
with st.container():
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("A message from Fatma :speech_balloon:")
        img1= Image.open('./media/fatma_ph.jpg')
        st.image(img1)
        st.title("Project Supervisor")
        st.write("""Everything is energy, and that's all there is to it. I live by these words as an Egyptian Materials Science Masters student at TU Darmstadt, Germany. I have acquired my Bachelor's degree in the same 
                 field with an extra minor in Nanotechnology and Nanoelectronics Engineering. My ancient ancestors and the formidable civilization they have built guide my passion in science. I seek interdiciplinarity 
                 in every aspect of my work combining not only the different fields of science and technology, but also the arts and philosophy""")
    with middle_column:
        st.subheader("A message from Masuma :speech_balloon:")
        img2= Image.open("./media/masuma_ph.jpg")
        st.image(img2)
        st.title("Website Manager")
        st.write("Introduction")
    with right_column:
        st.subheader("A message from Zainab :speech_balloon:")
        img3= Image.open("./media/zainab_ph.jpg")
        st.image(img3)
        st.title("Project Manager")
        st.write("Code is like humor. When you have to explain it its bad.")        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Piezoelectricity, oh my!")
        st.write('##')
        st.write('') 
