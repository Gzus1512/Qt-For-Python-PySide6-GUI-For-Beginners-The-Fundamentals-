import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "widget.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)

    def do_something() :
        print(window.full_name_line_edit.text(),"is a ", window.occupation_line_edit.text())

    #Changing the properties in the form
    window.setWindowTitle("User data")

    #Accessing widgets in the form
    window.submit_button.clicked.connect(do_something)
    window.show()

    sys.exit(app.exec())