import sys, os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore    import QFile, QCoreApplication, Qt

def resource_path(relative) -> os.path:
    return os.path.join(os.path.dirname(__file__), relative)

def make_template_from_fields(template, window) -> str: 
    from jinja2 import Environment, FileSystemLoader
    
    template = Environment(loader=FileSystemLoader(resource_path('.'))).get_template(template)
    return template.render(
        {
            "first_name": window.nameLineEdit.text(),
            "last_name": window.surnameLineEdit.text(),
            "added_number": window.telInternalLineEdit.text(),
            "mobile_number": window.telMobileLineEdit.text(),
            "position": window.positionLineEdit.text(),
            "email": window.eMailLineEdit.text(),
        }
    )
    
def main() -> None:
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts) # warning fix
    app = QApplication(sys.argv)
    
    ui_file = QFile(resource_path("template.ui"))
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.show()
    
    window.saveButton.clicked.connect(lambda: print(make_template_from_fields('new_template_r4.html.jinja2', window)))
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()