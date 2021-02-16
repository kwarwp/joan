# Miguel Roman-Okami Shiranui
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO, ESTYLE
STYLE.update(width=1150, height="600px")
ESTYLE.update(width="60px", height="60px", minHeight="60px")
INVENTARIO.elt.style.height= "60px"
linkilhadeusas = "https://i.imgur.com/5UvVC5M.png"
linkOkami1 = "https://i.imgur.com/hr6DsqU.png"
linkWaka1 = "https://i.imgur.com/e641yTi.png"
linkArk1 = "https://i.imgur.com/DhV0DOD.png"
linkGruta1 = "https://4.bp.blogspot.com/-MplqVVRjFCo/VzYD90Cm5jI/AAAAAAAAX_Q/x2JbhgAwJwAi0cNTQq2l2j6hLCEX--gZgCLcB/s1600/Gruta%2Bde%2BBacaetava.jpg"
linkRat1 = "https://i.imgur.com/Mm8ebIk.png"
linkArk2 = "https://i.imgur.com/DhV0DOD.png"
linkEspada1 = "https://i.imgur.com/3oAUPu9.png"
linkInventario = "https://i.imgur.com/aVQK2Vk.png"
linkMapa = "https://i.imgur.com/7XkXmxS.png"
linkQuests = "https://i.imgur.com/ZmFyU4K.png"
linkBrush = "https://i.imgur.com/kLF2yfu.png"
linkEspadaicone = "https://i.imgur.com/5dS5fKX.png"
linkCenablockhead = "https://i.imgur.com/H7yYveG.png"
linkReturn1 = "https://i.imgur.com/pvJvcNs.png"
#site iconehttps://okami.fandom.com/wiki/Celestial_Plain?file=Spirit_Globe_icon.png
def jogo():

    INVENTARIO.inicia()
    invent = Elemento(img = linkInventario, tit = "Inventário", h = 200, w = 200)
    INVENTARIO.bota(invent)
    mapa = Elemento(img = linkMapa, tit = "Mapa", h = 200, w = 200)
    INVENTARIO.bota(mapa)
    quests = Elemento(img = linkQuests, tit = "Quests", h = 150, w = 150)
    INVENTARIO.bota(quests)
    espada = Elemento(img = linkEspadaicone, tit = "espada", h = 200, w = 200)
    INVENTARIO.bota(mapa)
    cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
    cena_gruta = Cena(img = linkGruta1)
    cena_blockhead = Cena(img = linkCenablockhead)
    cenaIlha.meio = cena_gruta
    okami1 = Elemento(img = linkOkami1, tit = "Okami",
                         y = 400, x = 170, h = 200, w = 200)
    okami1.entra(cenaIlha)
     
    
    waka1 = Elemento(img = linkWaka1, tit = "Waka",
                         y = 340, x = 305, h = 250, w = 200)
    waka1.entra(cenaIlha)
    txtwaka1 = Texto(cenaIlha, "Vamos para a ilha das deusas.")
    waka1.vai = txtwaka1.vai
    
    ark1 = Elemento(img = linkArk1, tit = "Ark",
                         y = 400, x = 40, h = 200, w = 500)
    ark1.entra(cenaIlha)
    
    rat1 = Elemento(img = linkRat1, tit = "Rat godess",
                         y = 150, x = 420, h = 400, w = 400)
    rat1.entra(cena_gruta)
    txtrat1 = Texto(cena_gruta, "afie minha espada mas por um porem prove sue valor completando ésa missão.")
    rat1.vai = txtrat1.vai
    ark2 = Elemento(img = linkArk2, tit = "Ark",
                         y = 350, x = 830, h = 100, w = 100)
    ark2.entra(cena_gruta) 
    ark2.vai = cenaIlha.vai
    okami1 = Elemento(img = linkOkami1, tit = "Okami",
                         y = 400, x = 170, h = 200, w = 200)
    okami1.entra(cena_gruta)
    waka1 = Elemento(img = linkWaka1, tit = "Waka",
                         y = 340, x = 890, h = 250, w = 200)
    waka1.entra(cena_gruta)
    txtwaka1 = Texto(cena_gruta, "Vamos fazer a missão.")
    waka1.vai = txtwaka1.vai
    espada1 = Elemento(img = linkEspada1, tit = "espada",
                         y = 340, x = 450, h = 200, w = 200)
    espada1.entra(cena_gruta)
    espada1.vai = cena_blockhead.vai
    
    return1 = Elemento(img = linkReturn1, tit = "Return",
                         y = 50, x = 170, h = 100, w = 100)
    return1.entra(cena_blockhead)
    return1.vai = cena_gruta.vai
    cena_gruta.vai()
jogo()