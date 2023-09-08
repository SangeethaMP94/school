class school:
    def __init__(self,ques):
        self.questions = ques

    def get_answer(self,ans):
        self.answer=ans

    def corrections(self):
        self.final = {self.questions[i]:self.answer[i] for i in range(len(self.questions))}

    def generate_report(self,marks):
        self.marks =[]
        sum=0
        for j in marks:
           sum+=j
           self.marks.append(sum)
           print(sum)

        if sum<=15 and sum>=10:
          print("Grade A")
        elif sum<10 and sum>=5:
          print("Grade B")
        else:
          print("FAIL")

class teacher:
    def corrections(self,final,quest):
        mark=[]
        self.mark = mark
        for i,j in final.items():
            print("question:\t"+i+"\nanswer"+j)
            mark.append(float(input()))
        self.final_mark = {quest[i]:mark[i] for i in range(len(quest))}


class student:
    def start_exam(self,ques):
        self.answer=[]
        for i in ques:
            print(i)
            self.answer.append(input())


MMS = school(['What is Python','What is DS', 'What is Data science'])
Sangee = student()
Akila = teacher()

Sangee.start_exam(MMS.questions)

MMS.get_answer(Sangee.answer)
MMS.corrections()
MMS.final
Akila.corrections(MMS.final,MMS.questions)
Akila.final_mark
MMS.generate_report(Akila.mark)
