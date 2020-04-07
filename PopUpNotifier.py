from PyQt5.QtWidgets import  QMessageBox

class PopUpNotifier(object):

    # PopUpNotifier implements SingleTon pattern

    obj = None

    def __new__(cls, *dt, **mp):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt, **mp)  # вызовем __new__ родительского класса
            return cls.obj

    def ConnectionProgressNotify(self, if_connected):
        msg = QMessageBox()
        succeeded = 'Connection Successful!'
        failed = 'Connection with FT failed'
        msg.setWindowTitle('Connection Progress')

        if(if_connected):
            msg.setText(succeeded)
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setText(failed)
            msg.setIcon(QMessageBox.Warning)
        msg.exec_()


