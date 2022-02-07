# Code
```py
import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    b = QtWidgets.QPushButton(w)
    b.setText("Hello World!")
    b.move(250, 120)

    w.setGeometry(100, 100, 600, 200)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
    
```

# Results
![image](https://user-images.githubusercontent.com/84629235/152816700-3298d434-d17a-48a5-b666-ed68d710a56d.png)
