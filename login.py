from PyQt5 import uic,QtWidgets

def chama_tela_ok():
	primeira_tela.lab_1.setText('')
	usuario = primeira_tela.lin_1.text()
	senha = primeira_tela.lin_2.text()
	if usuario == 'José99' and senha == 'abc123':
		primeira_tela.close()
		segunda_tela.show()
	else:
		primeira_tela.lab_1.setText("Ooop's usuário e/ou senha incorretos!!!")

def logout():
	segunda_tela.close()
	primeira_tela.show()

app = QtWidgets.QApplication([])
primeira_tela=uic.loadUi('login_inicio.ui')
segunda_tela=uic.loadUi('logout.ui')
primeira_tela.but_1.clicked.connect(chama_tela_ok)
segunda_tela.but_1.clicked.connect(logout)
primeira_tela.lin_2.setEchoMode(QtWidgets.QLineEdit.Password)

primeira_tela.show()
app.exec()