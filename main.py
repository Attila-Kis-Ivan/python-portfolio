import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/home-img.svg")
    
with col2:
    st.header("Attila Kis-Ivan")
    content ="""
    Hi everyone, I'm Attila Kis-Ivan a self-taught web developer with degree of MSc Engineering Management from London UK. I fell in love with programming in 2020. Currently I'm developing products with React andReact-Native. I'm interested in AI so Python and PyTorch are on the way 😊.
    """
    st.info(content)
    
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!

"""    
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        
      
      
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        