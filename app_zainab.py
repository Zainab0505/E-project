import streamlit as st

from PIL import Image
st.set_page_config(page_title='Introduction', layout="centered")
with st.container():
    picture, intro = st.columns(2)
    with picture:
        st.write('##')
        st.write('##')
        img1= Image.open('./Media/zainab_ph.jpg')
        st.image(img1, width=300)
    with intro:
        st.title("ZAINAB")
        st.write("**PROJECT MANAGER**")
        st.write('''Hey there! I'm Zainab, born and raised in Pakistan. I have a Bachelor's degree in Metallurgical and Materials Engineering. I’m currently pursuing FAMEAIS+ at INP Phelma.''')
        st.write("**MORE ABOUT ME!**")
        st.write('''People say I'm an adventurous person, maybe a part of the reason why engineering always had an attractive touch for me. I have been thinking of ways to introduce myself. For long, I've just used "I'm a materials engineer". Wasn't working so I started saying "We're the reason your cell phone isn't the size of a brick anymore"''')