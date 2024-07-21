import random
import pandas as pd
import streamlit as st

def main():
    
    df = pd.read_csv('wisesay.csv')
    random_n = random.randint(0,len(df)-1)
    wise_say = df.iloc[random_n]
    
    st.header("경쟁상태 불안 평가 및 명언 제시 :sunglasses:")
    st.write("")
    with st.container():
        st.write("아래 설문에 답을 하고 결과 보기 버튼을 눌러 보세요.")
        st.write("현재 당신의 불안 상태와 함께 위로의 명언이 제공됩니다.")
    st.write("")
    with st.container():
    # 질문을 담을 리스트
        questions = [
            "Q1. 나는 이 시합(상황)이 걱정된다.",
            "Q2. 나는 긴장된다.",
            "Q3. 나는 걱정이 없다.",
            "Q4. 나는 내가 잘 할 수 있을지 걱정의심스럽다.",
            "Q5. 나는 초조하다.",
            "Q6. 나는 편안하다.",
            "Q7. 나는 이 시합에서 내가 가진 기량을 발휘하지 못할까봐 걱정된다.",
            "Q8. 내 몸이 긴장했다.",
            "Q9. 나는 자신있다.",
        ]

        options = ["전혀 아니다.", "약간 그렇다.", "대체로 그렇다.", "매우 그렇다."]

        # 사용자가 선택한 값을 담기 위한 상태 초기화
        if 'responses' not in st.session_state:
            st.session_state.responses = [None] * len(questions)

        # 각 질문에 대해 RadioButton 생성
        for i, question in enumerate(questions):
            st.session_state.responses[i] = st.radio(f"**{question}**", options, horizontal=True, index=0, key=f"question_{i}")
            st.write("")

    # 결과 보기 버튼
    if st.button("결과 보기"):
        # 모든 문항이 선택되지 않았으면 경고 메시지 출력
        if None in st.session_state.responses:
            st.warning("모든 문항에 응답해 주세요.")
        else:
            total_score = sum([options.index(response) + 1 if (i + 1) in (1, 2, 4, 5, 7, 8) else 5 - options.index(response) - 1 for i, response in enumerate(st.session_state.responses)])
            
            st.write(f"점수: {total_score}")
            if total_score <= 12:
                st.write("낮은 수준의 상태불안을 느낌")
            elif 13 <= total_score <= 24:
                st.write("중간 수준의 상태불안을 느낌")
            if 25 <= total_score <= 36:
                st.write("높은 수준의 상태불안을 느낌")
            st.write("")
            st.subheader('오늘의 명언')
            st.write("")
            st.markdown(f"**{wise_say['명언']}** :trophy:")
            st.write("")
            st.write(wise_say['해설'])
            st.write("")

    # 다시하기 버튼
    if st.button("다시하기"):
        # 상태 초기화
        st.session_state.responses = [None] * len(questions)
        st.rerun()

if __name__ == "__main__":
    main()




