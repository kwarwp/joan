# joan.samantha.main.py
# lorinda.kathryn.main.py
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE
from _spy.vitollino.main import Inventario as inv

STYLE["width"] = 800
STYLE["height"] = "600px"

#CENA 1 VERBO LEMBRAR HEREDITARIEDADE

SALA_FIOCRUZ = "https://i.imgur.com/iUBolXC.jpg"
ROSALINDA = "https://i.imgur.com/qvuwHvs.png"
ZEZINHO = "https://i.imgur.com/94lhgKo.png"
NPC = " https://i.imgur.com/NEG2o8W.jpg"
PERGAMINHO = "https://i.imgur.com/Xe3zdhP.jpg"
PESSOA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/6vgubFm.jpg"
PESSOA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS = "https://i.imgur.com/wtpBiVS.jpg"
PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/ZcfLShe.jpg"
CRIANCA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/ISvWiD4.jpg"
CRIANCA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS = "https://i.imgur.com/qoGRKc8.jpg"
CRIANCA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/DtSbcLh.jpg"
QUADRO_1_PESSOA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/6vgubFm.jpg"
QUADRO_2_PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/6vgubFm.jpg"
QUADRO_3_PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/ZcfLShe.jpg"
QUADRO_4_CRIANCA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/ISvWiD4.jpg"
QUADRO_5_CRIANCA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS = "https://i.imgur.com/qoGRKc8.jpg"
QUADRO_6_CRIANCA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/DtSbcLh.jpg"
GENE0, GENE1 = "https://i.imgur.com/UAYR77L.jpg", "https://i.imgur.com/R4HE1ho.jpg"
GENE2, GENE3 = "https://i.imgur.com/ljpxkIt.jpg", "https://i.imgur.com/e3OfADM.jpg"
MUSEU_DA_VIDA = "https://i.imgur.com/s4ZBrRv.jpg"
DNA = "https://www.facebook.com/Projeto-SupyGirls-2062797764002029"
Genes = "https://i.imgur.com/SBcbyUc.gif"
Nucleotideos = "https://i.imgur.com/eUn2STG.png"
'''
Organismo
Sequência correta
Cofre
Abrir cofre

PenDrive

Poção mágica

Super poderes
'''


# O CÓDIGO DO MINE GAME ENTRA AQUI?

class MiniGame:
    """Usa um editor de imagem (https://www.online-image-editor.com/) e recorta a imagem em partes.
       No game, o jogador terá que clicar nas linhas em ordem certa para montar a figura corretamente.
    """
    def __init__(self, esta_cena, chama_quando_acerta, partes=(GENE3, GENE0, GENE2, GENE1)):
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=175, h=125, cena=esta_cena)
                self.linha.vai = self.clica_e_posiciona_a_linha #quando clica, monta o herdograma
            def zera(self):
                self.linha.x = self.posicao*200  # posiciona cada peça com 200 pixels de distância
                self.linha.y = 20  # posiciona a peça no topo da página
                self.linha.vai = self.clica_e_posiciona_a_linha
            def clica_e_posiciona_a_linha(self, *_):
                x, y = posiciona_proxima(self.posicao)
                if y:  # se o y retornou zero é porque o posiciona próxima detectou montagem errada
                    self.linha.x, self.linha.y = x, y # monta a linha no herdograma
                    self.linha.vai = lambda *_:None #desativa o click da linha

        # coloca cada uma das linhas embaralhadas 
        self.linhas = [
            LinhaGeracional(linha=uma_linha, posicao=uma_posicao)
            for uma_posicao, uma_linha in enumerate(partes)]
        self.acertou = chama_quando_acerta
        self.parte_inicial = -1
        self.altura_da_linha = 125  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [1, 3, 2, 0]  # lista das linhas montadas corretamente

    def posiciona_proxima(self, posicao):
        """Chamado pelo clique (vai) de cada peça. Atualiza a próxima posição da peça.
           Calcula se montou correto, comparando com a lista de posicões corretas.
           Se já montou quatro peças, e não acerto sinaliza com zero, para iniciar o jogo.
        """
        largura_da_peca, inicio_horizontal, inicio_vertical, numero_de_pecas = 175, 300, 200, 4
        numero_de_pecas_por_linha = 2
        self.parte_inicial += 1  # incrementa a posição para montar a próxima posiçao da peça
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
        else:
            if len(self.posicoes_montadas) == numero_de_pecas:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.parte_inicial = -1  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))

class Primeira_fase():
    def __init__(self):

        self.sala_fiocruz = sala_fiocruz = Cena(img= SALA_FIOCRUZ)
        MiniGame(sala_fiocruz, self.acertou)
        rosalinda = Elemento( img = ROSALINDA, tit= "Tenho que me apresar, preciso de dinheiro para continuar minha pesquisa." ,
                style=dict (left=400, top=350, width=300, height="200px",))
        npc = Elemento(img= NPC, y=400,  cena=sala_fiocruz)
        pessoa_branca_cabelo_liso = Elemento(img= PESSOA_BRANCA_CABELO_LISO_OLHOS_VERDES, y=500,  cena=sala_fiocruz)
        pessoa_negra_cabelo_black = Elemento (img = PESSOA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS, y=500, x=150, cena=sala_fiocruz)
        pessoa_ruiva_pele_branca_cabelovermelho = Elemento (img = PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO, y=500, x=250, cena=sala_fiocruz)
        crianca_branca_cabelo_iso_olhos_verdes = Elemento (img = CRIANCA_BRANCA_CABELO_LISO_OLHOS_VERDES, y=500, x=350, cena=sala_fiocruz)
        crianca_negra_cabelo_black_olhos_castanhos = Elemento (img = CRIANCA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS, y=500, x=450, cena=sala_fiocruz)
        crianca_ruiva_pele_branca_cabelo_vermelho = Elemento (img = CRIANCA_RUIVA_PELE_BRANCA_CABELO_VERMELHO, y=500, x=550, cena=sala_fiocruz )
        sala_fiocruz.vai()
        #CENA 2 VERBO ENTENDER HEREDITARIEDADE

        self.museu_da_vida = Cena(MUSEU_DA_VIDA)
    def acertou(self):
        Texto(self.sala_fiocruz, "Encontrei um pergaminho! Achei uma saída pela direita!").vai()
        pergaminho = Elemento(img=PERGAMINHO,  cena=self.sala_fiocruz)
        self.sala_fiocruz.direita = self.museu_da_vida

'''
O NPC DEVERÁ APRESENTAR AS SEGUINTES DICAS ORGANIZAR AS PALAVRAS UTILIZANDO A ORDEM CORRETA DE ENTENDIMENTO




Nucleotídeos

Características

Organismo

Sequência correta

Abrir cofre

PenDrive

Poção mágica

Super poderes
'''
if __name__ == "__main__":
    Primeira_fase()