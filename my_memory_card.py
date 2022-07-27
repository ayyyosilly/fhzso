from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout, QGroupBox
from random import randint, shuffle

class Questionn():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

'''список вопросов'''

qlist = []
q1 = Questionn('how much did G2 buy m0NESY for?', '$600.000', '$50.000', '$1.000.000', '$100.000')
qlist.append(q1)
q2 = Questionn('who is NOT a hyperpop artist?', 'Eminem', '17 SEVENTEEN', '44neverluv', 'rizza') 
qlist.append(q2)
q3 = Questionn('who wrote "War and Peace?', 'Tolstoy', 'Gogol', 'Ostrovsky', 'Griboyedov')
qlist.append(q3)
q4 = Questionn('Rating 2.0 m0NESY for the last 3 months is..', '1.16', '1.20', '1.08', '1.01')
qlist.append(q4)
q5 = Questionn('Which countrys capital has the name Caracas?', 'Venezuela', 'Colombia', 'Nicaragua', 'Guinea')
qlist.append(q5)
q6 = Questionn('when WW2 started?', 'september 1, 1939', ' august 29, 1939', '22 june, 1941', '25 jule, 1941')
qlist.append(q6)
q7 = Questionn('developer of Gothic?', 'Piranha Bytes', 'Akella', 'BioWare', 'THQ Nordic')
qlist.append(q7)
q8 = Questionn('what was the score of the match Vitality - 9z?','Vit 1:2 9z, Nuk 16:9, Over 11:16, Inf 12:16' ,'Vit 2:0 9z, Nuke 16:12, Mir 16:5', 'Vit 2:1 9z, Over 16:2, Ver 14:16, Inf 16:10', 'Vit 0:2 9z, Anc 5:16, Nuk 14:16')
qlist.append(q8)
q9 = Questionn('which country has the tallest building in the world?', 'UAE', 'Indonesia', 'France', 'Saidu Arabia')
qlist.append(q9)
q10 = Questionn('in which country is Nokia manufactured?', 'Finland', 'Russia', 'Japan', 'China')
qlist.append(q10)

app = QApplication([])

window = QWidget()
window.setWindowTitle('memory card')

'''интерфейс m-card'''

btn_ok = QPushButton('Ответить') #answer button
lb_question = QLabel('who is NOT a hyperpop artist?') #question text

RadioGroupBox = QGroupBox('Варианты ответов') #on-screen group for radio buttons with responses
rbtn_1 = QRadioButton('17 SEVENTEEN')
rbtn_2 = QRadioButton('rizza')
rbtn_3 = QRadioButton('Eminem')
rbtn_4 = QRadioButton('44neverluv')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('text result')
lb_Result = QLabel('are you right or not?')
lb_Correct = QLabel('the answer will be here')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
#RadioGroupBox.hide()


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok,stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Next question')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('reply')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Questionn):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\nВсего вопросов ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\nВсего вопросов ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(qlist) - 1)
    q = qlist[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'reply':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_ok.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()