import  streamlit as st

name = st.text_input("Enter your name : ")
fname = st.text_input("Enter your father name : ")
adr = st.text_area("Enter your address : ")
classdata = st.selectbox("Enter Your Semester :",(1,2,3,4,5,6,7,8))

button = st.button("Submit")
if button:
    st.markdown(f"""
    Name: {name}
    Father: {fname}
    Address: {adr}
    classdata: {classdata}""")