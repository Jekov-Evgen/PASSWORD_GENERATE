import random
import string
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
import pyperclip
from const import STYLE_OUTPUT, CONST_RESULT_WINDOW

class Copying:
    def copy_password(self, __copy_password):
        pyperclip.copy(__copy_password)
        pyperclip.paste()
        
class ResultWindow:
    def result_window(self):
        msg = QMessageBox()
        
        msg.setWindowIcon(QIcon("icon.png"))
        msg.setWindowTitle("Результат работы")
        msg.setText("Просмотрите папку приложения, там пароль")
        msg.setStyleSheet(CONST_RESULT_WINDOW)
        
        msg.exec()
        
class Generate:
    def generate_password(self):
        length = random.randint(12, 20)
    
        password = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
    
        characters = string.ascii_letters + string.digits + string.punctuation
        password += [random.choice(characters) for _ in range(length - 3)]
    
        random.shuffle(password)
    
        return ''.join(password)

class CreatePasswordWindow:
    def show_password_output(self):
        created_password = self.get_password()
        msg = QMessageBox()
        
        msg.setWindowIcon(QIcon("icon.png"))
        msg.setWindowTitle("Сгенерированный пароль")
        msg.setText(f"{created_password}")
        msg.setStyleSheet(STYLE_OUTPUT)
        copy_button = msg.addButton("COPY", QMessageBox.ButtonRole.RejectRole)
        msg.buttonClicked.connect(lambda button: self.button_click(button, created_password))

        msg.exec()
    
    def button_click(self, button, text):
        button_text = button.text()
        
        if button_text == "COPY":
            self.button_click_copy(text)
            call_result = ResultWindow()
            call_result.result_window()
    
    def button_click_copy(self, text):
        copy = Copying()
        copy.copy_password(text)
        
    def get_password(self):
        created = Generate()
        result_created_password = created.generate_password()
        return result_created_password