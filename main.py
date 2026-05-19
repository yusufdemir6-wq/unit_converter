import sys
from PySide6.QtWidgets import (  #this brings in all the visual widgets
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox
)

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Unit Converter") #puts the title at the top of the window
        
        
        self.input = QLineEdit() # text box where user types the number
        self.input.setPlaceholderText("Enter value...") # grey hint text in the input box

        # this is to choose your conversion type
        self.combo = QComboBox() # creates the  menu
        self.combo.addItems([  #adds all the conversion options
            "Kilometers to Miles",
            "Miles to Kilometers",
            "Kilograms to Pounds",
            "Pounds to Kilograms",
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius"
        ])

        # the convert button
        self.button = QPushButton("Convert")
        self.button.clicked.connect(self.convert) # links the button click to the convert function

        # the result
        self.result = QLabel("Result will appear here")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.combo)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        self.setLayout(layout)

    def convert(self): # runs when the button is clicked
        try:
            value = float(self.input.text())
            choice = self.combo.currentText()

            if choice == "Kilometers to Miles":
                result = value * 0.621371
                self.result.setText(f"{value} km = {result:.2f} miles")
            elif choice == "Miles to Kilometers":
                result = value * 1.60934
                self.result.setText(f"{value} miles = {result:.2f} km")
            elif choice == "Kilograms to Pounds":
                result = value * 2.20462
                self.result.setText(f"{value} kg = {result:.2f} lbs")
            elif choice == "Pounds to Kilograms":
                result = value * 0.453592
                self.result.setText(f"{value} lbs = {result:.2f} kg")
            elif choice == "Celsius to Fahrenheit":
                result = (value * 9/5) + 32
                self.result.setText(f"{value}°C = {result:.2f}°F")
            elif choice == "Fahrenheit to Celsius":
                result = (value - 32) * 5/9
                self.result.setText(f"{value}°F = {result:.2f}°C")

        except ValueError:
            self.result.setText("Please enter a valid number!") # if the user types letters instead of numbers, show an error

app = QApplication(sys.argv)
window = UnitConverter()
window.show()
sys.exit(app.exec())