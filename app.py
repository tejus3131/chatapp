import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Application")
        self.resize(400, 500)

        self.chat_display = QTextBrowser()
        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_display)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.fetch_messages()

    def fetch_messages(self):
        response = requests.get("https://chatapp3131-tejus3131.vercel.app/messages")
        if response.status_code == 200:
            messages = response.json()
            for message in messages:
                self.chat_display.append(f"=> {message['content']}")
        else:
            print("Failed to fetch messages")

    def send_message(self):
        content = self.message_input.text().strip()
        if content:
            payload = {"content": content}
            response = requests.post("https://chatapp3131-tejus3131.vercel.app/messages", json=payload)
            if response.status_code == 200:
                self.chat_display.append(f"=> {content}")
                self.message_input.clear()
            else:
                print(response.status_code)
                print("Failed to send message")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
