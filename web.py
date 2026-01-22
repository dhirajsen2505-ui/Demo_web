import  streamlit as st

name = st.text_input("Enter your name : ")
adr = st.text_area("Enter your address : ")
quantity = st.selectbox("Enter How Many Water Bottel You Need :",(50,100,150,200,300,400,500,1000,1500))

button = st.button("Submit")
if button:
    st.markdown(f"""
    Name: {name}
    Address: {adr}
    quantity: {quantity}""")
