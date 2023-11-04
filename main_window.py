from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGroupBox,\
    QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox

win_card = QWidget()
win_card.resize(600,500)
win_card.move(300,300)
win_card.setWindowTitle('Memory Card')

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочть')

lb_rest = QLabel('хвилини')

sb_rest = QSpinBox()
sb_rest.setValue(30)

lineH_1 = QHBoxLayout()
lineH_1.addWidget(btn_menu)
lineH_1.addWidget(btn_rest)
lineH_1.addWidget(sb_rest)
lineH_1.addWidget(lb_rest)


lineH_1 = QHBoxLayout()
lineH_1.addWidget(btn_menu)
lineH_1.addWidget(sb_rest)
lineH_1.addWidget(sb_rest)
lineH_1.addWidget(lb_rest)


