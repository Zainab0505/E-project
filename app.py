import streamlit as st
from PIL import Image
#from streamlit_lottie import st_lottie (for graphics in further steps)
st.set_page_config(page_title='Piezoelectricity!', page_icon=":bulb:", layout="wide")
with st.container():
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Message from Fatma :speech_balloon:")
        img1= Image.open('./media/fatma_ph.jpg')
        st.image(img1)
        st.title("Project Supervisor")
        st.markdown("""Everything is energy, and that's all there is to it. I live by these words as an Egyptian Materials Science Masters student at TU Darmstadt, Germany. I have acquired my Bachelor's degree in the same 
                 field with an extra minor in Nanotechnology and Nanoelectronics Engineering. My ancient ancestors and the formidable civilization they have built guide my passion in science. I seek interdiciplinarity 
                 in every aspect of my work combining not only the different fields of science and technology, but also the arts and philosophy.""")
    with middle_column:
        st.subheader("Message from Masuma :speech_balloon:")
        img2= Image.open('./media/masuma_ph.jpg')
        st.image(img2)
        st.title("Website Manager")
        st.markdown('''Being from Baku, Azerbaijan, I hold a Bachelor's degree in Chemical Engineering. Before starting the Master's in Materials Engineering I worked as Laboratory Assistant at local university. 
                 My interests include watching movies 'n' series, riding a bike and philosophy. Also, my personality type is "The Mediator" (INFP) which is, believing psychologists, is less likely to be suitable for pursuing 
                 engineering speciality and scientific mindset in general. For the last few years I am doing my best to prove this opinion wrong :)''')
    with right_column:
        st.subheader("Message from Zainab :speech_balloon:")
        st.write()
        st.write()
        img3= Image.open('./media/zainab_ph.jpg')
        st.image(img3)
        st.title("Project Manager")
        st.markdown("""Hey there, I am Zainab, born and raised in Pakistan. I have a Bachelor's degree in Metallurgical Materials Engineering. People say I'm an adventurous person, maybe a part of the reason why engineering always 
                   had an attractive touch for me. I have been thinking of ways to introduce myself. For long, I've just used "I am a materials engineer". Wasn't working so I started saying "We're the reason your cell phone isn't the size of a brick anymore". """)        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Piezoelectricity, oh my!")
        st.write('##')
        st.markdown('''Facing current environmental challenges modern solutions are required to ensure sustainable energy production. One of the actualities nowadays includes the replacement of batteries which can be 
                 impractical to use on a long period of service by a smaller electronic device powered by ambient energy harvesting. Unlike the batteries, the energy produced by the harvester is not sufficient to power 
                 the electric devices directly, therefore the energy is first accumulated in a storage medium such as capacitors and rechargeable batteries [1]. Energy harvesting is reached by converting the mechanical energy 
                 triggered by wind or human motion into electrical energy. Several methods to achieve the conversion are studied up to date, among which the **piezoelectric effect** has demonstrated a higher energy production and better 
                 application to daily-life conditions. Piezoelectric materials can generate electric charge due to their crystalline structure, which allows the re-orientation of molecular dipole moments under applied mechanical stress.''') 
    with right_column:
        st.header("Operation and Materials")
        st.write('##')
        st.markdown('''Four types of piezoelectric materials are available based on their characteristics and properties. These are ceramics, single crystals, polymers, and composites (a combination of single crystal and polymer). 
                 Among them, ceramic materials demonstrate higher energy output, although they are more brittle and less stress-resistant than polymers [1]. The most common piezoelectric materials being used today are metal oxides, especially 
                 those with the perovskite ABX<sub>3</sub> structure. PZT (lead zirconate titanate) ceramics have dominated the market for sixty years [2]. Another typical example is PMN-PT (the solid solution of lead magnesium niobate and lead titanate). 
                 The new stream of research is to combine piezoelectric materials with pyroelectric (energy conversion from heat) or ferroelectrics (energy conversion from light) for better efficiency and enhanced output [3]. The energy generated by 
                 the harvester device depends both on intrinsic (piezoelectric and mechanical properties of selected material, device configuration) and extrinsic (frequency and amplitude of applied stress) properties [1].''', unsafe_allow_html= True) 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Here's the catch")
        st.write('##')
        st.markdown('''There are some loss mechanisms that need also be considered, along with the potential scale of the system (cm to nm) to make a viable energy harvesting device using these combinations, however, there are three major phases in piezoelectric energy harvesting:

1) The mechanical stability of the piezoelectric transducer under large stresses
2) The mechanical–electrical energy transformation
3) The efficient utilization of the produced electrical energies within circuitries [2] ''')
    with right_column:
        st.header("Eureka!")
        st.write('##')

        st.markdown('''We draw inspiration from **Belatchew Arkitekter** who combines these ideas in a sleek strawscraper [4]. By creating PbTiO<sub>3</sub> nanotubes (PTO NTs) by anodic oxidation and utilizing a hydrothermal approach using TiO<sub>2</sub> NT as a positive template, the Belatchew Architect's strawscrapper 
                 concept may be used. Ti fibers acting as the core electrode linking the individual piezoelectric nanotubes enable the fabrication of flexible, dense, and radially aligned perovskite PTO NTs. By bending or from wind motion in any direction, these free-standing fiber-type nanogenerators 
                 produce a consistent quantity of electric power, expanding the range of possible practical applications. Mass production is possible with simple control over the diameter, length, and base materials for various purposes [5].''', unsafe_allow_html=True)
        
with st.container():
    st.header('References')
    st.markdown('''1. Li, H., Tian, C., & Deng, Z. D, “Energy harvesting from low frequency applications using piezoelectric materials.” *Applied Physics Reviews*, vol. 1, no. 4, pp. 041301, 2014. DOI: https://doi.org/10.1063/1.4900845
2. K. Uchino, “Piezoelectric Energy Harvesting Systems—Essentials to Successful Developments”, *Energy Technol.* vol. 6, no. 829, 2018. DOI: https://doi.org/10.1002/ente.201700785
3. C.R. Bowen, H.A. Kim, P.M. Weaver, & S. Dunn, “Piezoelectric and ferroelectric materials and structures for energy harvesting applications.” *Energy & Environmental Science*, vol. 7, no. 1, pp. 25–44, 2013. DOI: https://doi.org/10.1039/C3EE42454E 
4. “Strawscraper,” Belatchew. [Online]. Available: https://belatchew.com/en/projekt/strawscraper/. [Accessed: 17-Nov-2022]''')