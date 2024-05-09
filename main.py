import sys
from PyQt6.QtWidgets import QApplication, QWidget
from app3 import Ui_Conductorslog
import logic

class MainApp(QWidget):
    def __init__(self) -> None:
        """
        Starts the MainApp widget.
        """
        super().__init__()
        self.ui = Ui_Conductorslog()
        self.ui.setupUi(self)
        self.logic = logic.Logic(self.ui)
        self.init_ui()

    def init_ui(self) -> None:
        """
        Initialize the user interface.
        """
        self.ui.pushButton.clicked.connect(self.on_submit)

    def on_submit(self) -> None:
        """
        Handles the submit button click event.
        """
        self.logic.on_submit()

    def closeEvent(self, event, **kwargs) -> None:
        """
        Handles the  close event.
        """
        self.logic.calculate_and_append_summary()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
