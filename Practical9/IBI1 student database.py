class students(object):

    def __init__(self,name,major,score_for_their_code_portfolio,score_for_their_group_project,exam_score):
        self.name=name
        self.major=major
        self.score_for_their_code_portfolio=score_for_their_code_portfolio
        self.score_for_their_group_project=score_for_their_group_project
        self.exam_score=exam_score

    def information(self):
        print(f"Name:{self.name}, Major:{self.major}, Code_portfolio_score:{self.score_for_their_code_portfolio}, Group_project_score:{self.score_for_their_group_project}, Exam_score:{self.exam_score}")

student1=students('xjy','BMI','100','100','100')
student1.information()