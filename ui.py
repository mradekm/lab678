from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import converter
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Data Converter')
        layout = QVBoxLayout()

        self.open_button = QPushButton('Open File')
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.save_button = QPushButton('Save File')
        self.save_button.clicked.connect(self.save_file)
        layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)", options=options)
        if file_path:
            self.input_path = file_path

    def save_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)", options=options)
        if file_path:
            self.output_path = file_path
            threading.Thread(target=self.convert_files).start()

    def convert_files(self):
        try:
            converter.convert(self.input_path, self.output_path)
            self.show_message("Success", "File converted successfully")
        except Exception as e:
            self.show_message("Error", str(e))

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
