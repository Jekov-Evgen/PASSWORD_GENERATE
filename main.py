from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from creating_a_password import CreatePasswordWindow
from const import CONST_HEDING, CONST_CULE, CONST_GENERATE_BUTTON, CONST_PLATFORM_NAME, CONST_MAIN_WINDOW

class SavingToFile:
    def save(self, name_platform):
        password = CreatePasswordWindow()
        
        with open('YourPasswor.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{name_platform}: {password.get_password()}\n')

class MainWindow(QMainWindow):
    def get_platform_name(self):
        return self.platform_name.text()  
    
    def calling_functions(self):
        name = self.get_platform_name()
        self.click_button_generate()
        
        saving_class_management = SavingToFile()
        saving_class_management.save(name)
        
    
    def click_button_generate(self):
        self.generation_password()
    
    def __init__(self):
        super().__init__()
        
        generation_class = CreatePasswordWindow()
        self.generation_password = generation_class.show_password_output
        self.heading = QLabel("Password generator", self)
        self.clue = QLabel("Введите для какой платформы пароль", self)
        self.platform_name = QLineEdit(self)
        self.generate_password_button = QPushButton("Генерация пароля", self)
        
        self.setFixedSize(QSize(300, 250))
        self.setWindowIcon(QIcon("photo/icon.png"))
        
        self.heading.setStyleSheet(CONST_HEDING)
        self.heading.setFixedWidth(300)
        self.heading.setFixedHeight(60)
        self.heading.move(60, 20)
        
        self.clue.setStyleSheet(CONST_CULE)
        self.clue.setFixedWidth(500)
        self.clue.setFixedHeight(60)
        self.clue.move(10, 80)
        
        self.platform_name.setStyleSheet(CONST_PLATFORM_NAME)
        self.platform_name.setFixedHeight(50)
        self.platform_name.setFixedWidth(150)
        self.platform_name.move(75, 140)
        
        self.generate_password_button.setStyleSheet(CONST_GENERATE_BUTTON)
        self.generate_password_button.setFixedWidth(150)
        self.generate_password_button.move(75, 200)
        self.generate_password_button.clicked.connect(self.calling_functions)


app = QApplication([])

window = MainWindow()
window.setStyleSheet(CONST_MAIN_WINDOW)
window.show()

app.exec()