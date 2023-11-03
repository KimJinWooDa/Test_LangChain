#from dotenv import load_dotenv
#load_dotenv()
from langchain.chat_models import ChatOpenAI
import streamlit as st


chat_model = ChatOpenAI()

st.title('인공지능 시인')

title = st.text_input('주제를 쓰세요')

if st.button('만들기 버튼'):   
    with st.spinner('시 작성중...'):
        result = chat_model.predict(title + "에 대한 시를 써줘!")
        st.write('시의 내용은', result)



