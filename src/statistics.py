class Statistics:
    def __init__(self, db):
        self.db = db
    
    def get_grade_statistics(self, exam_no, exam_type):
        info = self.db.get_exam_info(exam_no, exam_type)
        grade_df = (self.db.grade_stats[(self.db.grade_stats["회차"] == exam_no)
        & (self.db.grade_stats["시험종류"] == exam_type)]).copy()

        grade_df["응시자대비합격률"] = (grade_df["합격자수"] / info["응시자수"] *100)
        grade_df["합격자비율"] = (grade_df["합격자수"]/info["합격자수"]*100)

        return grade_df