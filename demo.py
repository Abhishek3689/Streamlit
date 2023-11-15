import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
place=st.text_input("Enter the place you want to search")
st.write(place)
city=st.radio(label="Place",options=["Nagpur","Raipur"])
if city==place:
    st.write("City is correct")
else:
    st.write("You need to enter diffrenet value")

brand=st.sidebar.selectbox("Car Brand",['Maruti','BMW','Mercedes'])
if brand=="Maruti":
    st.multiselect("Models",['Dezire','Swift','Celerio'])
elif brand=="BMW":
    st.multiselect("Models",['X1','X3','X7'])
else:
    st.multiselect('Models',['A Class','S Class','GLB'])
fig,ax=plt.subplots()
ax.plot([1,2,3,4],[5,7,9,4])
st.pyplot(fig)