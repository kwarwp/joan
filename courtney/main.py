# joan.courtney.main.py
# Miguel Roman-Okami Shiranui
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO, ISTYLE,  ESTYLE, Inventario
STYLE.update(width=1150, height="600px")
ISTYLE.update(height="60px", minHeight="60px")
ESTYLE.update(width="60px", height="60px", minHeight="60px")
ESTYLE["min-height"]="60px"
print(ESTYLE)
INVENTARIO = Inventario()

linkilhadeusas = "https://i.imgur.com/5UvVC5M.png"
linkOkami1 = "https://i.imgur.com/hr6DsqU.png"
linkWaka1 = "https://i.imgur.com/e641yTi.png"
linkArk1 = "https://imgur.com/zzfVPmy.png"
linkGruta1 = "https://4.bp.blogspot.com/-MplqVVRjFCo/VzYD90Cm5jI/AAAAAAAAX_Q/x2JbhgAwJwAi0cNTQq2l2j6hLCEX--gZgCLcB/s1600/Gruta%2Bde%2BBacaetava.jpg"
linkRat1 = "https://i.imgur.com/Mm8ebIk.png"
linkArk2 = "https://i.imgur.com/DhV0DOD.png"
inventario = "https://i.imgur.com/OhT5Wxa.png"
quest_img = "https://i.imgur.com/rVZ1nFW.png"
option_img = "https://i.imgur.com/xmMC1Se.png"
okami_fala = 0
"""As cenas são criadas primeiro, aqui em cima"""
cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
cena_gruta = Cena(img = linkGruta1)
    
def gruta(_=0):
    """Você tem um 'def' (função) para cada cena, esta aqui faz a cena da gruta"""
    global cenaIlha
    cena_gruta = Cena(img = linkGruta1)
    
    rat1 = Elemento(img = linkRat1, tit = "Rat godess",
                         y = 300, x = 170, h = 400, w = 400)
    rat1.entra(cena_gruta)
    txtrat1 = Texto(cena_gruta, "afie minha espada mas por um porem prove sue valor completando ésa missão.")
    rat1.vai = txtrat1.vai
    ark2 = Elemento(img = linkArk2, tit = "Ark",
                         y = 350, x = 830, h = 100, w = 100)
    ark2.entra(cena_gruta) 
    ark2.vai = cenaIlha.vai
    cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
    cenaIlha.meio = cena_gruta
    okami1 = Elemento(img = linkOkami1, tit = "Okami",
                         y = 400, x = 170, h = 200, w = 200)
    okami1.entra(cena_gruta)
    cena_gruta.vai()
    # fim da função gruta

def jogo():
    """Esta função cria a cena inicial."""
    INVENTARIO.style["min-height"] = "60px"
    INVENTARIO.inicia()
    invent = Elemento(img = inventario, tit = "inventário", h = 200, w = 200)
    INVENTARIO.bota(invent)
    invent.elt.style.width="60px"
    invent.elt.style.height="60px"
    quest = Elemento(img = quest_img, tit = "quest", h = 200, w = 200)
    INVENTARIO.bota(quest)
    option = Elemento(img = option_img, tit = "options", h = 200, w = 200)
    INVENTARIO.bota(option)
    cenaIlha.meio = Cena() # criei uma cena falsa para usar o vai dela 
    cenaIlha.meio.vai = gruta # o vai na verdade chama a função gruta
    okami1 = Elemento(img = linkOkami1, tit = "Okami",
                         y = 400, x = 170, h = 200, w = 200)
    okami1.entra(cenaIlha)
    waka1 = Elemento(img = linkWaka1, tit = "Waka",
                         y = 340, x = 305, h = 250, w = 200)
    waka1.entra(cenaIlha)
    txtwaka1 = Texto(cenaIlha, "Vamos para a ilha das deusas.")
    txtokami1 = Texto(cenaIlha, "Oi Waka.")
    txtokami2 = Texto(cenaIlha, "Então vamos.")
    textos_okami = [txtokami1, txtokami2]
    
    def fala_okami(_):
        global okami_fala
        textos_okami[okami_fala].vai()
        okami_fala -= 1
    okami1.vai = fala_okami
    waka1.vai = txtwaka1.vai
    
    ark1 = Elemento(img = linkArk1, tit = "Ark",
                         y = 450, x = 40, h = 150, w = 500)
    ark1.entra(cenaIlha)
    
    cenaIlha.vai()
    invent.elt.style.width="60px"
    invent.elt.style.height="60px"
    invent.elt.style = ESTYLE

jogo()