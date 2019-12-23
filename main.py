from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QRect
import pyautogui
import sys
import webbrowser
import os

screenWidth, screenHeight = pyautogui.size()
LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
WEBFILE = 'piramides.html'
NOME_ARQ = ['./saida/basica.txt', './saida/social.txt', './saida/pessoal.txt', './saida/destino.txt', './saida/ano.txt']
INDEX_NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8']
INDEX_LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if(not os.path.isdir(LOCAL_PATH + "/saida")):
    os.mkdir('saida')

def confere_texto(linha):
    print(linha)
    for l in linha:
        if l > 'a' and l < 'z':
            return True
    return False

def mexeTxt(nome, tipo):
    newFile = open(nome, tipo)
    return newFile

def inseriDados(arq, texto):
    arq.write(texto)

def transformaLinha(linha, num):
    newline = ""
    minlen = 2
    if (linha.__len__() > minlen):
        indexMax = linha.__len__() - 1
        index = 1
        while (index < indexMax):
            primeiro = int(linha[index - 1])
            ultimo = int(linha[index])
            soma = primeiro + ultimo
            while (soma > 9):
                soma = str(soma)
                digito1 = int(soma[0])
                digito2 = int(soma[1])
                soma = digito1 + digito2
            newline = newline + str(soma)
            index = index + 1
        inserir = mexeTxt(NOME_ARQ[num], 'a')
        newline = newline + '\n'
        inseriDados(inserir, newline)
        inserir.close()

def linhaUmBasica():
    readfile = mexeTxt(NOME_ARQ[0], 'r')
    linha = readfile.readline()
    transformaLinha(linha, 0)
    while linha:
        linha = readfile.readline()
        transformaLinha(linha, 0)
    return True



def criaImagem():
    indexMain = 0
    while indexMain < NOME_ARQ.__len__():
        file = mexeTxt(NOME_ARQ[indexMain], 'r')
        linha = file.readline()
        newline = []
        index = 0
        i=0
        while linha:
            doing = 1
            newline.append("")
            while doing != index and doing < index:
                newline[index] = newline[index] + " "
                doing = doing + 1
            for l in linha:
                newline[index] = newline[index] + l + " "
            index = index + 1
            linha = file.readline()
        file.close()
        file = mexeTxt(NOME_ARQ[indexMain], 'w')
        while i < index:
            file.write(newline[i])
            i = i + 1
        indexMain = indexMain + 1
    return True

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Numerologia"
        width = 200
        height = 150
        top = (screenHeight - height) / 2
        left = (screenWidth - width) / 2

        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)

        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Rodar", self)
        button.setGeometry(QRect(60, 80, 80, 30))
        button.setToolTip("Clique no botão para rodar o programa")

        self.textinput = QLineEdit(self)
        self.textinput.move(20,20)
        self.textinput.resize(160,20)
        self.textinput.setPlaceholderText("Insira o Nome Completo")

        self.diainput = QLineEdit(self)
        self.diainput.move(40,45)
        self.diainput.resize(30,30)
        self.diainput.setPlaceholderText("Dia")

        self.mesinput = QLineEdit(self)
        self.mesinput.move(80,45)
        self.mesinput.resize(30,30)
        self.mesinput.setPlaceholderText("Mes")

        self.anoinput = QLineEdit(self)
        self.anoinput.move(120,45)
        self.anoinput.resize(60,30)
        self.anoinput.setPlaceholderText("Ano Desejado")

        button.clicked.connect(self.run_Program)

    def confere_Inputs(self):
        dia = self.diainput.text()
        mes = self.mesinput.text()
        ano = self.anoinput.text()
        try:
            if dia.__len__() != 2 or mes.__len__() != 2 or ano.__len__() != 4:
                return False
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
        except Exception:
            return False
        return True

    def Social(self):
        lerPrimeiraLinha = mexeTxt(NOME_ARQ[0], 'r')
        primeiraLinha = lerPrimeiraLinha.readline()
        newline = ""
        numSoma = int(self.mesinput.text())
        primeiro = int(numSoma / 10)
        segundo = int(numSoma % 10)
        numSoma = primeiro + segundo
        while numSoma > 9:
            primeiro = int(numSoma / 10)
            segundo = int(numSoma % 10)
            numSoma = primeiro + segundo
        for l in primeiraLinha:
            if l != '\n' and l:
                resp = int(l) + int(numSoma)
                while resp > 9:
                    primeiro = int(resp / 10)
                    segundo = int(resp % 10)
                    resp = primeiro + segundo
                newline = newline + str(resp)
        newline = newline + '\n'
        newFile = mexeTxt(NOME_ARQ[1], 'w')
        inseriDados(newFile, newline)
        newFile.close()

        endFile = mexeTxt(NOME_ARQ[1], 'r')
        linha = endFile.readline()
        while linha:
            transformaLinha(linha,1)
            linha = endFile.readline()


    def Destino(self):
        lerPrimeiraLinha = mexeTxt(NOME_ARQ[0], 'r')
        primeiraLinha = lerPrimeiraLinha.readline()
        newline = ""
        numSoma = int(self.mesinput.text())
        primeiro = int(numSoma / 10)
        segundo = int(numSoma % 10)
        numSoma = primeiro + segundo
        newSoma = int(self.diainput.text())
        newp = int(newSoma / 10)
        news = int(newSoma % 10)
        newSoma = newp + news
        fullsoma = newSoma + numSoma
        while fullsoma > 9:
            primeiro = int(fullsoma / 10)
            segundo = int(fullsoma % 10)
            fullsoma = primeiro + segundo
        numSoma = fullsoma
        for l in primeiraLinha:
            if l != '\n' and l:
                resp = int(l) + int(numSoma)
                while resp > 9:
                    primeiro = int(resp / 10)
                    segundo = int(resp % 10)
                    resp = primeiro + segundo
                newline = newline + str(resp)
        newline = newline + '\n'
        newFile = mexeTxt(NOME_ARQ[3], 'w')
        inseriDados(newFile, newline)
        newFile.close()

        endFile = mexeTxt(NOME_ARQ[3], 'r')
        linha = endFile.readline()
        while linha:
            transformaLinha(linha, 3)
            linha = endFile.readline()

    def Pessoal(self):
        lerPrimeiraLinha = mexeTxt(NOME_ARQ[0], 'r')
        primeiraLinha = lerPrimeiraLinha.readline()
        newline = ""
        numSoma = int(self.diainput.text())
        primeiro = int(numSoma / 10)
        segundo = int(numSoma % 10)
        numSoma = primeiro + segundo
        while numSoma > 9:
            primeiro = int(numSoma / 10)
            segundo = int(numSoma % 10)
            numSoma = primeiro + segundo
        for l in primeiraLinha:
            if l != '\n' and l:
                resp = int(l) + int(numSoma)
                while resp > 9:
                    primeiro = int(resp / 10)
                    segundo = int(resp % 10)
                    resp = primeiro + segundo
                newline = newline + str(resp)
        newline = newline + '\n'
        newFile = mexeTxt(NOME_ARQ[2], 'w')
        inseriDados(newFile, newline)
        newFile.close()

        endFile = mexeTxt(NOME_ARQ[2], 'r')
        linha = endFile.readline()
        while linha:
            transformaLinha(linha, 2)
            linha = endFile.readline()

    def Ano(self):
        lerPrimeiraLinha = mexeTxt(NOME_ARQ[0], 'r')
        primeiraLinha = lerPrimeiraLinha.readline()
        newline = ""
        numSoma = int(self.anoinput.text())
        primeiro = int(numSoma / 1000)
        segundo = int((numSoma / 100) % 10)
        terceiro = int((numSoma / 10) % 10)
        quarto = int(((numSoma % 1000)%100)%10)
        numSoma = primeiro + segundo + terceiro + quarto
        while numSoma > 9:
            primeiro = int(numSoma / 10)
            segundo = int(numSoma % 10)
            numSoma = primeiro + segundo
        for l in primeiraLinha:
            if l != '\n' and l:
                resp = int(l) + int(numSoma)
                while resp > 9:
                    primeiro = int(resp / 10)
                    segundo = int(resp % 10)
                    resp = primeiro + segundo
                newline = newline + str(resp)
        newline = newline + '\n'
        newFile = mexeTxt(NOME_ARQ[4], 'w')
        inseriDados(newFile, newline)
        newFile.close()

        endFile = mexeTxt(NOME_ARQ[4], 'r')
        linha = endFile.readline()
        while linha:
            transformaLinha(linha, 4)
            linha = endFile.readline()

    def ProjetaTela(self):
        f = open(WEBFILE, 'w')
        piramide1 = ""
        piramide2 = ""
        piramide3 = ""
        piramide4 = ""
        piramide5 = ""

        lerfile = mexeTxt(NOME_ARQ[0], 'r')
        linha = lerfile.readline()
        while linha:
            for l in linha:
                if l == '\n':
                    piramide1 = piramide1 + '<br>'
                else:
                    piramide1 = piramide1 + l
            linha = lerfile.readline()
        lerfile.close()

        lerfile = mexeTxt(NOME_ARQ[1], 'r')
        linha = lerfile.readline()
        while linha:
            for l in linha:
                if l == '\n':
                    piramide2 = piramide2 + '<br>'
                else:
                    piramide2 = piramide2 + l
            linha = lerfile.readline()
        lerfile.close()

        lerfile = mexeTxt(NOME_ARQ[2], 'r')
        linha = lerfile.readline()

        while linha:
            for l in linha:
                if l == '\n':
                    piramide3 = piramide3 + '<br>'
                else:
                    piramide3 = piramide3 + l
            linha = lerfile.readline()
        lerfile.close()

        lerfile = mexeTxt(NOME_ARQ[3], 'r')
        linha = lerfile.readline()
        while linha:
            for l in linha:
                if l == '\n':
                    piramide4 = piramide4 + '<br>'
                else:
                    piramide4 = piramide4 + l
            linha = lerfile.readline()

        lerfile = mexeTxt(NOME_ARQ[4], 'r')
        linha = lerfile.readline()

        while linha:
            for l in linha:
                if l == '\n':
                    piramide5 = piramide5 + '<br>'
                else:
                    piramide5 = piramide5 + l
            linha = lerfile.readline()
        lerfile.close()

        mensagem = f"""<html>
        <head>
        <title>Resposta das Piramides</title>
         </head>
           <body>
             <div style='text-align: center;'>
                <h1> Basica <br>
                {piramide1}   <br>
                <br> Social <br> 
                {piramide2}
                Pessoal<br>  
                {piramide3} <br>
                <br> Destino<br> 
                {piramide4}<br>
                <br>Ano<br>
                {piramide5}</h1><
              /div>
            </body>
        </html>"""
        f.write(mensagem)
        f.close()

        index = 0
        while index < NOME_ARQ.__len__():
            os.remove(LOCAL_PATH + NOME_ARQ[index][1:])
            index = index + 1
        os.rmdir(LOCAL_PATH + "/Saida")
        webbrowser.open_new(LOCAL_PATH + '/' + WEBFILE)

    def run_Program(self):
        if self.confere_Inputs():
            textboxvalue = self.textinput.text()
            maxchars = 12
            textboxvalue = textboxvalue.lower()
            newtext = ""
            for letra in textboxvalue:
                if(newtext.__len__() >= maxchars):
                    break
                if((letra >= 'a' and letra <= 'z') or (letra >= "A" and letra <= "Z") or letra == "ç"):
                    newtext = newtext + letra
            if(confere_texto(newtext)):
                numeros = ""
                for letra in newtext:
                    index = 0
                    while(index <= 25):
                        if(letra == INDEX_LETRAS[index]):
                            numeros = numeros+INDEX_NUMEROS[index]
                            break
                        index = index + 1
                escrever = mexeTxt(NOME_ARQ[0], 'w')
                numeros = numeros + '\n'
                inseriDados(escrever, numeros)
                escrever.close()

                if linhaUmBasica():

                    self.Social()
                    self.Pessoal()
                    self.Destino()
                    self.Ano()

                    if criaImagem():
                        print("Tudo Ocorreu certo")
                        self.ProjetaTela()
                        os._exit(0)

                else:
                    print('Algo Deu Errado')
            else:
                QMessageBox.about(self, 'Erro em Nome', 'Digite o nome sem acentos ou caracteres especiais')
        else:
            QMessageBox.about(self, "Erro em Data", "Voce precisa digitar somente numeros na area de DD/MM/AAAA (Dia Mes Ano)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())