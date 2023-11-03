import streamlit as st
from langchain.chat_models import ChatOpenAI

api_key = st.text_area("API-Key를 입력하세요.", value='', placeholder='여기에 API-Key를 입력하세요.')

if api_key:
    chat_model = ChatOpenAI(openai_api_key=api_key)
else:
    placeholder = st.empty()
    
st.title("Game Character 생성")

character_background = st.text_area("캐릭터의 배경을 설정해주세요.")
character_personality = st.text_area("캐릭터의 성격을 정해주세요.")
character_class = st.selectbox("캐릭터의 직업을 선택해주세요.", ["전사", "마법사", "도적"])

if st.button("캐릭터 만들기"):
    with st.spinner('캐릭터 분석중...'):
        if character_background and character_personality and character_class:
            character_description = f"Background: {character_background}, Personality: {character_personality}. Class: {character_class}"

            character_info = ("해당 캐릭터의 배경은 다음과 같습니다 : " + character_background +
                                      "해당 캐릭터의 성격은 다음과 같습니다 : " + character_personality +
                                      "해당 캐릭터의 직업은 다음과 같습니다 : " + character_class)
            response = chat_model.predict("해당 캐릭터의 정보를 가지고 캐릭터에 어울리는 공격력, 방어력, 이동속도를 추천해주세요." + 
                                          "이때 제공해주는 형식은 다음과 같습니다 : 공격력 : , 방어력 : , 이동속도 : " +
                                          "정보는 다음과 같습니다 : " + character_info)
            st.write(response)