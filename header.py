import streamlit as st
import pandas as pd
st.title("Welcome to Home page")
st.header("We are in the streamlit header")
st.subheader("now you are in subheader")
st.write(pd.DataFrame({'Sr_no':[1,2,3,4],'Name':['Abhishek','Nitesh','Omy','Sangeeta']},index=['row1','row2','row3','row4']))
st.table(pd.DataFrame({'Sr_no':[1,2,3,4],'Name':['Abhishek','Nitesh','Omy','Sangeeta']},index=['row1','row2','row3','row4']))
st.text("this is the text part")

st.markdown("""
# H1 tag
            
## H2
### H3 
**BOLD Word** <br> 
_Italics_""")