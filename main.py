import PyQt5.QtWidgets as wid
import PyQt5.QtCore as core
import sys
import os
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak

'''

Mudancas do mainAntigo para o novo:

Alterando forma de retorno, sera usado .pdf
removendo funcoes que nao sao mais necessarias
comentando codigo

'''

# Variveis globais com informacoes que serao usadas durante todo o programa
LOCALPATH = os.path.dirname(os.path.abspath(__file__))
INDEX_NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2',
                 '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8']
INDEX_LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# confere existencia do local de saida e, se nao existir, cria ele
if not os.path.isdir(LOCALPATH+'/saida'):
    os.mkdir('saida')


# função de abrir files, nao necessaria
def alteraArquivo(nome, tipo):
    newFile = open(nome, tipo)
    return newFile

# função que confere de failsafe o texto


def confereTexto(linha):
    print(linha)
    for l in linha:
        if l > 'a' and l < 'z':
            return True
    return False
# Classe principal, janela do programa e suas funcionalidades


class Window(wid.QMainWindow):
    # Init da classe criando a tela do programa
    def __init__(self):
        super().__init__()
        title = "Numerologia"
        width = 450
        height = 300
        top = 100
        left = 100

        self.NUMEROS_INICIAIS = ''
        self.NOME_PESSOA = ''
        self.DATA_NASC = ''
        self.DATA_DESEJADA = ''
        self.PIRAMIDE_BASICA = []
        self.PIRAMIDE_SOCIAL = []
        self.PIRAMIDE_DESTINO = []
        self.PIRAMIDE_PESSOAL = []
        self.PIRAMIDE_ANO = []

        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)

        self.UiComponents()

        self.show()

    # Função que efetivamente cria os butoes na tela e ja poem eles como self para podermos pegar os valores em outras funções
    def UiComponents(self):
        buttonSend = wid.QPushButton("Rodar", self)
        buttonSend.setGeometry(core.QRect(60, 80, 80, 30))
        buttonSend.setToolTip("Clique no botao para rodar o programa")

        self.nomeInput = wid.QLineEdit(self)
        self.nomeInput.move(20, 20)
        self.nomeInput.resize(160, 20)
        self.nomeInput.setPlaceholderText("Insira o nome completo")

        self.diaInput = wid.QLineEdit(self)
        self.diaInput.move(40, 45)
        self.diaInput.resize(30, 30)
        self.diaInput.setPlaceholderText("Dia")

        self.mesInput = wid.QLineEdit(self)
        self.mesInput.move(80, 45)
        self.mesInput.resize(30, 30)
        self.mesInput.setPlaceholderText("Mes")

        self.anoNascInput = wid.QLineEdit(self)
        self.anoNascInput.move(120, 45)
        self.anoNascInput.resize(60, 30)
        self.anoNascInput.setPlaceholderText("Ano Nascimento")

        self.anoDesInput = wid.QLineEdit(self)
        self.anoDesInput.move(190, 45)
        self.anoDesInput.resize(60, 30)
        self.anoDesInput.setPlaceholderText("Ano Desejado")

        buttonSend.clicked.connect(self.RunProgram)

    '''
        Funcao que pega os inputs e confere eles
        conferindo se o texto esta digitado de forma correta
        e se as datas estao corretas no formato dd/mm/aaaa
    '''

    def ConfereInputs(self):
        dia = self.diaInput.text()
        mes = self.mesInput.text()
        anoD = self.anoDesInput.text()
        anoN = self.anoNascInput.text()
        nome = self.nomeInput.text()
        try:
            if dia.__len__() != 2 or mes.__len__() != 2 or anoD.__len__() != 4or anoN.__len__() != 4:
                return False
            dia = int(dia)
            mes = int(mes)
            anoD = int(anoD)
            anoN = int(anoN)
            for letra in nome:
                if letra == ' ' or (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
                    print("Funcionando por enquanto.")
                else:
                    return False
        except Exception:
            return False
        return True

    '''
        Funções das piramides, idealmente uma so que recebe parametros para as diferenças
    '''

    def PreenchePiramide(self, somarLinha):
        novaPiramide = []
        novaLinha = ''
        ultimaLinha = ''
        linhasFeitas = 1
        '''
        Transforma os numeros iniciais basicos com a soma para cada piramide especial
        antes salva a ultima linha para podermos ir transformando sempre diminuindo um
        '''
        for numero in self.NUMEROS_INICIAIS:
            if not numero == ' ' and not numero == '\n':
                novoNumero = int(numero) + somarLinha
            while novoNumero > 9:
                num1 = int(novoNumero / 10)
                num2 = int(novoNumero % 10)
                novoNumero = num1 + num2
            if not numero == ' ' and not numero == '\n':
                novaLinha += str(novoNumero) + ' '

        ultimaLinha = novaLinha
        novaPiramide.append(novaLinha)
        novaLinha = ''

        '''
         Adiciona as novas linhas ja espaçadas para estarem prontas para serem inseridas no pdf
         Pegamos os digitos da ultima linha, começando pelo primeiro e pelo segundo
         e transformamos no primeiro da nova linha, quando a linha acabar,
         transformamos ela na ultima linha
        '''

        while ultimaLinha.__len__() > linhasFeitas + 2:
            indexMaximo = ultimaLinha.__len__() - 1
            i = linhasFeitas + 1

            # podno espaços nas linhas para alinhar elas
            iLinhas = 0
            while iLinhas < linhasFeitas:
                novaLinha += ' '
                iLinhas += 1
            # voltando para preencher corretamente a piramide
            while i < indexMaximo:
                num1 = int(ultimaLinha[i - 2])
                num2 = int(ultimaLinha[i])
                soma = num1 + num2
                while soma > 9:
                    num1 = int(soma / 10)
                    num2 = int(soma % 10)
                    soma = num1 + num2
                novaLinha += str(soma) + ' '
                i += 2

            ultimaLinha = novaLinha

            novaPiramide.append(novaLinha)
            linhasFeitas += 1
            novaLinha = ''

        return novaPiramide

    def CriaPDF(self):
        try:

            ########################################################################
            pdf = canvas.Canvas(
                f'./saida/{self.NOME_PESSOA} {self.DATA_DESEJADA}.pdf')
            pdf.setTitle(f'Piramides de {self.NOME_PESSOA}')

            pdf.setFont('Courier', 14)

            '''
                Vamos printar cada piramide no pdf e por o titulo de cada uma também
                '''

            pdf.drawCentredString(
                300, 650, f'Nome: {self.NOME_PESSOA.title()}')
            pdf.drawCentredString(
                300, 620, f'Data Nasc: {self.diaInput.text()}/{self.mesInput.text()}/{self.DATA_NASC}')

            pdf.drawCentredString(295, 580, f"Ano {self.DATA_DESEJADA}")
            ano = pdf.beginText(200, 550)
            for linha in self.PIRAMIDE_ANO:
                ano.textLine(linha)
            pdf.drawText(ano)

            pdf.showPage()

            pdf.setFont('Courier', 14)

            pdf.drawCentredString(115, 780, 'Basica')
            basica = pdf.beginText(20, 750)
            for linha in self.PIRAMIDE_BASICA:
                basica.textLine(linha)
            pdf.drawText(basica)

            pdf.drawCentredString(475, 780, 'Social')
            social = pdf.beginText(380, 750)
            for linha in self.PIRAMIDE_SOCIAL:
                social.textLine(linha)
            pdf.drawText(social)

            pdf.drawCentredString(115, 350, 'Pessoal')
            pessoal = pdf.beginText(20, 320)
            for linha in self.PIRAMIDE_PESSOAL:
                pessoal.textLine(linha)
            pdf.drawText(pessoal)

            pdf.drawCentredString(475, 350, 'Destino')
            destino = pdf.beginText(380, 320)
            for linha in self.PIRAMIDE_DESTINO:
                destino.textLine(linha)
            pdf.drawText(destino)

            pdf.save()

            ########################################################################
        except Exception:
            return False
        return True

    def RunProgram(self):
        '''
        - transforma o nome no tamanho certo caso menor que 12 caracteres
        - transforma o dia e mes nos numeros de soma

        Confere os inputs numericos desejados e como eles estão. Também confere se preencheou o nome
        Pega o texto e tira os espaços e utliza lower()
        se o texto for menor do que 12 caracteres, repete ele ate precisar
        '''
        if self.ConfereInputs():
            '''
            Pega os valores e passa para as variaveis que serao usadas para formatação
            transforma o texto do nome em 12 caracteres seguidos sem espaço em letra minuscula
            caso o nome tenha menos que 12 caracteres repete ele ate ter 12
            '''
            self.NOME_PESSOA = self.nomeInput.text()
            self.DATA_NASC = self.anoNascInput.text()
            self.DATA_DESEJADA = self.anoDesInput.text()
            caixaTextoValor = self.nomeInput.text()
            nMaximo = 12
            caixaTextoValor = caixaTextoValor.lower()

            novoTexto = ""
            for letra in caixaTextoValor:
                if novoTexto.__len__() >= nMaximo:
                    break
                if letra >= 'a' and letra <= 'z':
                    novoTexto += letra

            if novoTexto.__len__() < nMaximo:
                for i in range(nMaximo - 1):
                    if novoTexto.__len__() >= nMaximo:
                        break
                    novoTexto += novoTexto[i]

          # transforma as letras em numeros que serao usados nas piramides
            for letra in novoTexto:
                index = 0
                while index <= 25:
                    if letra == INDEX_LETRAS[index]:
                        self.NUMEROS_INICIAIS += INDEX_NUMEROS[index] + ' '
                        break
                    index += 1

            self.NUMEROS_INICIAIS = self.NUMEROS_INICIAIS[:-1]

            '''
            Agora que temos os numeros iniciais podemos, somando os digitos do mes e dia criar a social, pessoal e destino, e usando o ano desejado, podemos criar a do ano também.
            precisamos fazer algumas contas simples, como a soma do nome para fins da numerologia.
            Isso pode ser feito antes das piramides e ser salvo no que sera o cabeçalho

            '''

            soma_nome = 0

            soma_ano = int(self.anoDesInput.text()[0]) + int(self.anoDesInput.text()[
                1]) + int(self.anoDesInput.text()[2]) + int(self.anoDesInput.text()[3])

            soma_mes = int(self.mesInput.text()[
                           0]) + int(self.mesInput.text()[1])

            soma_dia = int(self.diaInput.text()[
                           0]) + int(self.diaInput.text()[1])

            while soma_ano > 9:
                num1 = int(soma_ano / 10)
                num2 = int(soma_ano % 10)
                soma_ano = num1 + num2

            while soma_dia > 9:
                num1 = int(soma_dia / 10)
                num2 = int(soma_dia % 10)
                soma_dia = num1 + num2

            while soma_mes > 9:
                num1 = int(soma_mes / 10)
                num2 = int(soma_mes % 10)
                soma_mes = num1 + num2

            soma_datas = soma_mes + soma_dia

            while soma_datas > 9:
                num1 = int(soma_datas / 10)
                num2 = int(soma_datas % 10)
                soma_datas = num1 + num2

            for num in range(0, int(self.NUMEROS_INICIAIS.__len__() / 2) + 1):
                soma_nome = int(num) + soma_nome

            '''
            Agora nos vamos efetivamente criar as piramides 
            e iremos ir pondo elas em um pdf que vai ser criado

            primeiramente vamos as piramides...
            '''

            self.PIRAMIDE_PESSOAL = self.PreenchePiramide(soma_dia)
            self.PIRAMIDE_SOCIAL = self.PreenchePiramide(soma_mes)
            self.PIRAMIDE_BASICA = self.PreenchePiramide(0)
            self.PIRAMIDE_DESTINO = self.PreenchePiramide(soma_datas)
            self.PIRAMIDE_ANO = self.PreenchePiramide(soma_ano)

            '''
            Agora vamos preencher o pdf com as piramides, o cabeçalho e qualquer outra
            informação que possa vir a ser importante

            usaremos uma função para termos um "callback" quando ela
            acabar retornando algum tipo de informação para o nosso usuario
            '''

            if self.CriaPDF():
                wid.QMessageBox.about(
                    self, 'Concluido!', f"Seu PDF foi criado com sucessoe está salvo na pasta Saida com o nome: {self.NOME_PESSOA} {self.DATA_DESEJADA}.pdf!")
                self.diaInput.clear()
                self.mesInput.clear()
                self.anoNascInput.clear()
                self.anoDesInput.clear()
                self.nomeInput.clear()
            else:
                wid.QMessageBox.about(
                    self, 'Erro', "Ocorreu algum erro desconhecido, favor relatar o problema para o criador do programa.")

            # prints para fins de testes
            print(soma_dia)
            print(soma_mes)
            print(soma_nome)
            print(self.NUMEROS_INICIAIS)
            print(self.NOME_PESSOA.title())

        else:
            wid.QMessageBox.about(
                self, "Erro em Data", "Voce precisa digitar somente numeros na area de DD/MM/AAAA (Dia Mes Ano) e/ou o seu texto tem que ser somente de caracteres(sem ~ ou ç)")


if __name__ == "__main__":
    app = wid.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
