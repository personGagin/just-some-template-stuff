import sys
from os import path
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QCoreApplication, Qt

html = str
MAIN_TEMPLATE: html = """
<div class="signature">
<style type="text/css">
    .signature {{
        background-color: white;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        width: fit-content;
        margin-bottom: 0;
        margin-top: 0.2em;
        font-size: 13px;
        color: #272725;
        padding: 0;
    }}

    .orange.signature {{
        color: #de6a19;
    }}

    .gray.signature {{
        color: #515151;
    }}

    .line.signature {{
        height: 8px;
        width: 600px;
        background-color: #de6a19;
        margin-top: 0.5em;
    }}
</style>
<br>
<p class="signature">
    С уважением,<br />
    {first_name} <b>{last_name}</b>
</p>

<img class="signature" src=https://mail.kr-drive.ru/img/kr-logo-black.svg
    alt="KR Automation" align="bottom" width="84" height="60" style="margin-top: 30px; margin-bottom: 30px;"/>
<p class="gray signature" style="margin-bottom: 30px;">
    {position}
</p>
<p class="orange signature">КР Автоматизация</p> 
<p class="signature">	600033, г. Владимир | ул. Мостостроевская, д. 18 </p>
<p class="signature">
    +7 4922 37 24 80 | +7 4922 37 24 81{phones}
</p>
<p class="signature">
    <a class="orange signature" href="mailto:{email}">{email}</a>
     | 
    <a class="gray signature" href="http://www.kr-automation.ru/">kr-automation.ru</a>
</p>
<div class="orange line signature"></div>
<br>
</div>
"""


def resource_path(relative) -> path:
    return path.join(path.dirname(__file__), relative)


def make_template_from_fields(template, window) -> str:
    if template is MAIN_TEMPLATE:
        fields: dict = {
            "first_name": window.nameLineEdit.text(),
            "last_name": window.surnameLineEdit.text(),
            "added_number": window.telInternalLineEdit.text(),
            "mobile_number": window.telMobileLineEdit.text(),
            "position": window.positionLineEdit.text(),
            "email": window.eMailLineEdit.text(),
        }
        phones = ""
        if fields["added_number"] != "":
            phones += f" | доб. {fields["added_number"]} "
        if fields["mobile_number"] != "":
            phones += f"<br>\n    моб. {fields["mobile_number"]}"
        return template.format(**fields, phones=phones)


def main() -> None:
    def on_click():
        path_dialog, _ = QFileDialog.getSaveFileName(
            window,
            "Сохранить",
            path.expanduser(f"~/Documents/{window.eMailLineEdit.text()}.html"),
        )
        w_file = open(path_dialog, "w", encoding="utf-8")
        w_file.write(make_template_from_fields(MAIN_TEMPLATE, window))

    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # warning fix
    app = QApplication(sys.argv)

    ui_file = QFile(resource_path("template.ui"))
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.show()
    window.saveButton.clicked.connect(on_click)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
