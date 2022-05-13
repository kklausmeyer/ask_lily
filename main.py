import pandas as pd
import streamlit as st
import os
from PIL import Image


# Get answers
in_csv = os.path.join(os.getcwd(),'tables','ask_lily.csv')
#
df = pd.read_csv(in_csv, encoding='cp1252')



st.title('Ask Lily')

img_path = os.path.join(os.getcwd(),'graphics','Ask_Lily.JPG')

image = Image.open(img_path)
st.image(image, width = 300)

# Instructions
st.subheader("Instructions")
st.markdown('''
- Close your eyes and ask Soothsayer Lily a yes-no question
- Click the "Ask Lily" button
- Your answer is revealed (Lily never lies!)
''')
if st.button('Ask Lily'):
    df1 = df.sample()
    st.write("Lily says: {}".format(df1.iloc[0]['answer']))
    img_path2 = os.path.join(os.getcwd(),'graphics','{}'.format(df1.iloc[0]['photo']))
    image2 = Image.open(img_path2)
    st.image(image2)
     
