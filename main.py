import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title("Game Character Generator")

character_background = st.text_area("Enter character background")
character_personality = st.text_area("Enter character personality")
character_class = st.selectbox("Select Character Class", ["Warrior", "Mage", "Rogue"])

if st.button("Generate Stats"):
    with st.spinner('캐릭터 분석중...'):
        if character_background and character_personality and character_class:
            character_description = f"Background: {character_background}, Personality: {character_personality}. Class: {character_class}"

            character_info = ("해당 캐릭터의 배경은 다음과 같습니다 : " + character_background +
                                      "해당 캐릭터의 성격은 다음과 같습니다 : " + character_personality +
                                      "해당 캐릭터의 직업은 다음과 같습니다 : " + character_class)
            response = chat_model.predict("해당 캐릭터의 정보를 가지고 캐릭터에 어울리는 공격력, 방어력, 이동속도를 추천해주세요. 정보는 다음과 같습니다 : " + character_info)
            st.write(response)