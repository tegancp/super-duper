import streamlit as st
import pandas as pd

st.title('this is the title', anchor='top')

st.header('you can *write* things...',
          divider='rainbow')

# st.write('I **like** sunglasses :sunglasses:')
'I **like** sunglasses :sunglasses:'
st.text('I **like** sunglasses :sunglasses:')

st.write('This is a number:', 562)

df = pd.DataFrame({'number': [5, 42, 200, 307]})

st.write('This is a dataframe:', df)
st.caption('This dataframe was brought to you by the letter :blue[**K**].')

st.title('this title should not be here',
         anchor=False,
         help='there should be only one title')

st.write({'one': 1, 'two': 'II', 'three': False})
