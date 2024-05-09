class Logic:
    def __init__(self, ui):
        """
        Initialize Logic class.
        """
        self.ui = ui
        self.report_printed = False
        self.signal_tally = {
            # This is to store tally counts for each signal
            self.ui.radioButton.text(): 0,
            self.ui.radioButton_2.text(): 0,
            self.ui.radioButton_3.text(): 0,
            self.ui.radioButton_4.text(): 0,
            self.ui.radioButton_5.text(): 0,
            self.ui.radioButton_6.text(): 0,
            self.ui.radioButton_7.text(): 0,
            self.ui.radioButton_8.text(): 0,
            self.ui.radioButton_9.text(): 0,
        }
        self.total_speed = 0
        self.trip_count = 0


    def on_submit(self):
        """
        Handle submission of data.
        """
        data = {
            "Subdivision": self.ui.lineEdit.text(),
            "Conductor": self.ui.lineEdit_2.text(),
            "Departure Date": self.ui.dateEdit.date().toString("yyyy-MM-dd"),
            "Departure Time": self.ui.dateTimeEdit.time().toString("hh:mm"),
            "Train ID/Job": self.ui.lineEdit_5.text(),
            "Engineer": self.ui.lineEdit_6.text(),
            "Arrival Date": self.ui.dateEdit_2.date().toString("yyyy-MM-dd"),
            "Arrival Time": self.ui.dateTimeEdit_2.time().toString("hh:mm")
        }

        with open("ConLog.txt", "a") as file:
            if not self.report_printed:
                file.write("*" * 80 + "\n")
                file.write("-" * 80 + "\n")
                file.write("*" * 80 + "\n")
                file.write("CONDUCTORS REPORT\n")
                file.write("-" * 80 + "\n")
                file.write(f"Subdivision: {data['Subdivision']: <42}Train/Job ID: {data['Train ID/Job']}\n")
                file.write(f"Conductor: {data['Conductor']: <45}Engineer: {data['Engineer']}\n")
                file.write(f"Departure Date: {data['Departure Date']: <40}Arrival Date: {data['Arrival Date']}\n")
                file.write(f"Departure Time: {data['Departure Time']: <39}Arrival Time: {data['Arrival Time']}\n\n")
                self.report_printed = True

            signal_selected = self.get_selected_signal()
            speed = self.ui.lineEdit_11.text()
            location = self.ui.lineEdit_10.text()
            time = self.ui.timeEdit.time().toString("hh:mm")
            comments = self.ui.textEdit.toPlainText()

            if signal_selected:
                file.write("-" * 80 + "\n")
                file.write(f"Signal:{signal_selected}, Time (24hr format): {time}, Location Mile Post: {location}, Speed: {speed}\n")
                file.write(f"Delay Comments: {comments}\n\n")

                # Adds to tally for the selected signal
                self.signal_tally[signal_selected] += 1

                # Update total speed and trip count for calculating average speed later
                self.total_speed += int(speed)
                self.trip_count += 1

        self.clear_input_fields()
        self.uncheck_radio_buttons()

    def clear_input_fields(self):
        """
        Clear input fields
        """
        for line_edit in [self.ui.textEdit, self.ui.lineEdit_11, self.ui.lineEdit_10]:
            line_edit.clear()

    def uncheck_radio_buttons(self):
        """
        Uncheck radio buttons
        """
        for button in [
            self.ui.radioButton, self.ui.radioButton_2, self.ui.radioButton_3,
            self.ui.radioButton_4, self.ui.radioButton_5, self.ui.radioButton_6,
            self.ui.radioButton_7, self.ui.radioButton_8, self.ui.radioButton_9
        ]:
            button.setChecked(False)

    def get_selected_signal(self) -> str:
        """
        Get the selected signal from radio buttons.
        """
        if self.ui.radioButton.isChecked():
            return self.ui.radioButton.text()
        elif self.ui.radioButton_2.isChecked():
            return self.ui.radioButton_2.text()
        elif self.ui.radioButton_3.isChecked():
            return self.ui.radioButton_3.text()
        elif self.ui.radioButton_4.isChecked():
            return self.ui.radioButton_4.text()
        elif self.ui.radioButton_5.isChecked():
            return self.ui.radioButton_5.text()
        elif self.ui.radioButton_6.isChecked():
            return self.ui.radioButton_6.text()
        elif self.ui.radioButton_7.isChecked():
            return self.ui.radioButton_7.text()
        elif self.ui.radioButton_8.isChecked():
            return self.ui.radioButton_8.text()
        elif self.ui.radioButton_9.isChecked():
            return self.ui.radioButton_9.text()
        else:
            return ""

    def calculate_and_append_summary(self):
        """
        Calculate average speed and print summary to file.
        """
        # Calculate average speed
        if self.trip_count != 0:
            average_speed = self.total_speed / self.trip_count
        else:
            average_speed = 0

        # Append  summary to the file
        with open("ConLog.txt", "a") as file:
            file.write("\nSUMMARY\n")
            file.write("-" * 80 + "\n")
            for signal, tally in self.signal_tally.items():
                file.write(f"{signal}: {tally}\n")
            file.write(f'Average Speed: {average_speed:.2f}\n')
            file.write("*" * 80 + "\n")
            file.write("-" * 80 + "\n")
            file.write("*" * 80 + "\n")
