# joan.grace.batista.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" História de São João Batista.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    21.06
        Profeta Isaías.

"""
from _spy.vitollino.main import STYLE, JOGO as J
STYLE.update(width=1150, height="650px")
LIMBO = J.c("")

class Joao:
    CIBELE = "https://i.imgur.com/HMuEhac.png"
    JOAO = "https://lh6.googleusercontent.com/proxy/-uO97CDohujBTk6epLFDcJFgb4cluV2hXkaw-c0Cz-o-ciPynGSuD8VDroJcU-gTBLVSNvJxDVaagCgPEyChHqZDalbvFz9qqw=w1200-h630-p-k-no-nu"
    def __init__(self):
        self.joao = J.c(self.JOAO)
        self.cibele = J.a(self.CIBELE, y=400, w=200, h=250, cena=self.joao)
        fala = ('Olá, eu sou a catequista Cibele, e hoje vamos falar sobre São João Batista.'
        ' Clique no X para fechar esta fala e clique em São João para continuar.')
        self.isaias = Isaias()

        self.fala = J.n(self.joao, fala, foi=self.foi)
        self.joao.meio = J.c("", vai=self.voz)
        self.joao.esquerda = J.c("", vai=self.voz)
    def vai(self):
        self.joao.vai()
        self.fala.vai()
    def foi(self, _=0):
        self.cibele.entra(LIMBO)
    def voz(self, _=0):
        self.isaias.vai()


class Isaias:
    ISAIAS = "https://i.imgur.com/acDFUaT.jpg"
    def __init__(self):
        self.isaias = J.c(self.ISAIAS)
        self.deserto = Deserto()
        fala = 'Há uma voz que clama: “Em meio à terra desértica preparai o caminho para Yahweh;' 
        ' na estepe, aplanai uma vereda para o nosso Deus!"'
        self.cibele = J.a(Joao.CIBELE, y=400, w=200, h=250, cena=self.isaias)
        falacib = ('Este é o profeta Isaías. No ano de 711 antes de Cristo ele anunciou uma profecia.'
        ' Clique no X para fechar esta fala e clique no profeta Isaías para continuar.')

        self.fala = J.n(self.isaias, fala)
        self.falacib = J.n(self.isaias, falacib, foi=self.foi)
        self.isaias.esquerda = J.c("", vai=self.voz)
        self.isaias.meio = J.c("", vai=self.voz)
    def foi(self):
        self.cibele.entra(LIMBO)
    def vai(self):
        self.isaias.vai()
        self.falacib.vai()
    def voz(self, _=0):
        self.deserto.vai()


class Deserto:
    DESERTO = "https://largest.org/wp-content/uploads/2018/12/Arabian-Desert.jpg"
    JOAO = "https://i.imgur.com/bDzsF58.png"
    def __init__(self):
        self.deserto = J.c(self.DESERTO)
        self.cibele = J.a(Joao.CIBELE, y=400, w=200, h=250, cena=self.deserto)
        falacib = ('Este é o deserto da Arábia, região que o povo de Deus teve que atravessar'
        ' voltando do exílio da Babilônia até Jerusalém. Nada cresce neste lugar e não há caminhos'
        ' que se possa seguir. Foi em um lugar como esse que o último profeta da Bíblia morou.'
        ' Clique no deserto e depois no que vai aparecer.')
        self.falacib = J.n(self.deserto, falacib, foi=self.foi)
        self.deserto.esquerda = J.c("", vai=self.voz)
        self.deserto.meio = J.c("", vai=self.voz)
    def foi(self, _=0):
        self.cibele.entra(LIMBO)
    def vai(self):
        self.deserto.vai()
        self.falacib.vai()
    def voz(self, _=0):
        self.joao = J.a(self.JOAO,x=300, y=200, w=200, h=250, cena=self.deserto)
        self.cibele.entra(LIMBO)


class Zacarias:
    ANUNCIA = "https://mydestinysharinghope.com/wp-content/uploads/2011/12/zechariah-and-angel.jpg"
    JOAO = "https://i.imgur.com/bDzsF58.png"
    ANJO = "https://i.imgur.com/7ct92uB.png"
    CORTINA = "https://i.imgur.com/RO0oeZI.jpg"
    def __init__(self):
        self.anuncia = J.c(self.ANUNCIA)
        self.cibele = J.a(Joao.CIBELE, y=400, w=200, h=250, cena=self.anuncia)
        self.cortina = J.a(self.CORTINA, x=700, y=100, w=450, h=550, cena=self.anuncia)
        self.anjo = J.a(self.ANJO, x=950, y=100, w=180, h=280, cena=self.anuncia, vai=self.dica2)
        self.bebele = J.a(Joao.CIBELE, x=750, y=200, w=180, h=280, cena=self.anuncia, vai=self.dica0)
        self.joao = J.a(Deserto.JOAO, x=950, y=350, w=280, h=280, cena=self.anuncia, vai=self.dica1)
        falacib = ('Este é Zacharias, ele é um sacerdote no templo e já é bem velho.'
        ' Ele recebe uma visita no templo, quem foi visitá-lo? Clique no seu palpite.')
        self.palpites = (' Quem eu? Bem que gostaria de dar esta notícia, mas isto aconteceu há mais de 2000 anos',
        'Bom, Jõao Batista não tinha nascido ainda, e esta era a razão desta visita',
        'Foi então que um anjo do Senhor apareceu a Zacarias, à direita do altar do incenso. Clique na cortina para saber mais')
        self.falacib = J.n(self.anuncia, falacib, foi=self.foi)
    def foi(self, _=0):
        self.cibele.entra(LIMBO)
    def vai(self):
        self.anuncia.vai()
        self.falacib.vai()
    def dica0(self, _=0):
        J.n(self.anuncia, self.palpites[0], foi=self.foi).vai()
    def dica1(self, _=0):
        J.n(self.anuncia, self.palpites[1], foi=self.foi).vai()
    def dica2(self, _=0):
        J.n(self.anuncia, self.palpites[2], foi=self.foi).vai()
        self.cortina.vai = self.abre_cortina
    def abre_cortina(self, _=0):
        self.cortina.entra(LIMBO)
        self.anjo.entra(LIMBO)
        self.bebele.entra(LIMBO)
        self.joao.entra(LIMBO)
        fala = ('Não tenhas medo, Zacarias; eis que a tua súplica foi ouvida.'
        ' Isabel, tua esposa, te dará à luz um filho, e tu lhe porás o nome de João.')
        J.n(self.anuncia, fala).vai()
        
if __name__ == "__main__":
    Joao().vai()
    #Zacarias().vai()
    