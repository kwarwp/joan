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


class Joao:
    CIBELE = "https://i.imgur.com/HMuEhac.png"
    JOAO = "https://lh6.googleusercontent.com/proxy/-uO97CDohujBTk6epLFDcJFgb4cluV2hXkaw-c0Cz-o-ciPynGSuD8VDroJcU-gTBLVSNvJxDVaagCgPEyChHqZDalbvFz9qqw=w1200-h630-p-k-no-nu"
    def __init__(self):
        self.joao = J.c(self.JOAO)
        self.cibele = J.a(self.CIBELE, y=400, w=200, h=250, cena=self.joao)
        fala = ('Olá, eu sou a catequista Cibele, e hoje vamos falar sobre São João Batista.'
        ' Clique no X para fechar esta fala e clique em São João para continuar.')
        self.isaias = Isaias()

        self.fala = J.n(self.joao, fala)
        self.joao.meio = J.c("", vai=self.voz)
        self.joao.esquerda = J.c("", vai=self.voz)
    def vai(self):
        self.joao.vai()
        self.fala.vai()
    def voz(self, _=0):
        self.cibele.x = -10000
        self.isaias.vai()


class Isaias:
    ISAIAS = "https://i.imgur.com/acDFUaT.jpg"
    def __init__(self):
        self.isaias = J.c(self.ISAIAS)
        fala = 'Há uma voz que clama: “Em meio à terra desértica preparai o caminho para Yahweh;' 
        ' na estepe, aplanai uma vereda para o nosso Deus!"'
        self.cibele = J.a(Joao.CIBELE, y=400, w=200, h=250, cena=self.isaias)
        falacib = ('Este é o profeta Isaías. No ano de 711 antes de Cristo ele anunciou uma profecia.'
        ' Clique no X para fechar esta fala e clique no profeta Isaías para continuar.')

        self.fala = J.n(self.isaias, fala)
        self.falacib = J.n(self.isaias, falacib)
        self.isaias.esquerda = J.c("", vai=self.voz)
        self.isaias.meio = J.c("", vai=self.voz)
    def vai(self):
        self.isaias.vai()
        self.falacib.vai()
    def voz(self, _=0):
        self.cibele.x = -10000
        self.fala.vai()


if __name__ == "__main__":
    Joao().vai()