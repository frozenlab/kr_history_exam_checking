import streamlit as st
from kr_history_exam_DB import HanunggeomDB
from src.grader import ExamGrader

db = HanunggeomDB()
grader = ExamGrader(db)
