import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class SlotMachine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Slots")
        self.setGeometry(600, 200, 400, 300)
        self.balance = 100

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Balance display
        self.balance_label = QLabel(f"Balance: ${self.balance}")
        self.balance_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.balance_label)

        # Bet input
        bet_layout = QHBoxLayout()
        self.bet_input = QLineEdit()
        self.bet_input.setPlaceholderText("Enter your bet")
        bet_layout.addWidget(self.bet_input)

        self.bet_button = QPushButton("Spin")
        self.bet_button.clicked.connect(self.play_round)
        bet_layout.addWidget(self.bet_button)

        layout.addLayout(bet_layout)

        # Slot display
        self.slot_labels = [QLabel("❓") for _ in range(3)]
        slot_layout = QHBoxLayout()
        for lbl in self.slot_labels:
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("font-size: 40px;")
            slot_layout.addWidget(lbl)
        layout.addLayout(slot_layout)

        # Result display
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def spin_row(self):
        symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
        return [random.choice(symbols) for _ in range(3)]

    def get_payout(self, row, bet):
        if row[0] == row[1] == row[2]:
            if row[0] == '🍒':
                return bet * 5
            elif row[0] == '🍉':
                return bet * 10
            elif row[0] == '🍋':
                return bet * 15
            elif row[0] == '🔔':
                return bet * 20
            elif row[0] == '⭐':
                return bet * 25
        return 0

    def play_round(self):
        bet_text = self.bet_input.text()
        if not bet_text.isdigit():
            QMessageBox.warning(self, "Invalid Bet", "Please enter a valid number.")
            return

        bet = int(bet_text)

        if bet <= 0:
            QMessageBox.warning(self, "Invalid Bet", "Bet must be greater than 0.")
            return
        if bet > self.balance:
            QMessageBox.warning(self, "Insufficient Funds", "You don't have enough balance.")
            return

        self.balance -= bet

        row = self.spin_row()
        for i in range(3):
            self.slot_labels[i].setText(row[i])

        payout = self.get_payout(row, bet)

        if payout > 0:
            self.result_label.setText(f"You won ${payout}!")
        else:
            self.result_label.setText("Sorry, you lost this round.")

        self.balance += payout
        self.balance_label.setText(f"Balance: ${self.balance}")

        if self.balance <= 0:
            QMessageBox.information(self, "Game Over", "Your balance is 0. Game over!")
            self.bet_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SlotMachine()
    window.show()
    sys.exit(app.exec_())
