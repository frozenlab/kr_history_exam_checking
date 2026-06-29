import streamlit as st
from hanunggom_db import HanunggeomDB
from src.grader import ExamGrader

db = HanunggeomDB()
grader = ExamGrader(db)
st.title("한국사능력검정시험 채점기")

exam_no = st.number_input("회차", min_value=11, step=1)
exam_type = st.selectbox("시험종류", ["고급", "중급", "초급", "심화", "기본"])
answer_text = st.text_area("답안 입력\n예 : 1 2 3 4 5 ...")

if st.button("채점"):
    try:
        answers = [int(x) for x in answer_text.split()]
        result = grader.grade(exam_no, exam_type, answers)
        st.success(f"점수 : {result["점수"]} / {result["만점"]}")
        st.wirte(f"정답 수 : {result["정답수"]}")
    
    except Exception as e:
        st.error(str(e))