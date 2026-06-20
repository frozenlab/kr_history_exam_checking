class ExamGrader:
    def __init__(self, db):
        self.db = db
    
    def validate_answers(self, exam_no, exam_type, answers):
        info = self.db.get_exam_info(exam_no, exam_type)
        question_count = int(info["문항수"])
        max_choice = int(info["선택지수"])

        if len(answers) != question_count:
            raise ValueError(f"{exam_type} 시험은"
                            f"{question_count}문항입니다.")
        
        for i, answer in enumerate(answers):
            if not isinstance(answer, int):
                raise ValueError(f"{i+1}번 답안은 숫자여야 합니다.")
            if answer < 1 or answer > max_choice:
                raise ValueError(f"{i+1}번 답안 {answer}은"
                f"허용 범위를 벗어났습니다.")
    
    def check_answer(self, user_answer, correct_answer):
        correct_answer = str(correct_answer).strip()

        if correct_answer == "x":
            return True
        if "," in correct_answer:
            return (str(user_answer) in [x.strip() for x in correct_answer.split(",")])
        
        return (str(user_answer) == correct_answer)
    
    def grade(self, exam_no, exam_type, answers):
        self.validate_answers(exam_no, exam_type, answers)
        answer_row = self.db.get_answer_row(exam_no, exam_type)
        score_row = self.db.get_score_row(exam_no, exam_type)

        earned = 0
        total = 0
        details = []

        for i in range(len(answers)):
            col = f"{i+1}번"
            correct = answer_row[col]
            score = score_row[col]
            total += score

            result = self.check_answer(answers[i], correct)

            if result:
                earned += score
            
            details.append({
                "문항" : i +1,
                "제출" : answers[i],
                "정답" : correct,
                "정오" : result
            })
        
        return {
            "점수" : earned,
            "만점" : total,
            "정답수" : sum(d["정오"] for d in details)
            "상세결과" : details
        }
