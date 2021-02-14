# Miguel Roman-Okami Shiranui
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE.update(width=1150, height="600px")

linkilhadeusas = "https://i.imgur.com/5UvVC5M.png"
linkOkami1 = "https://i.imgur.com/hr6DsqU.png"
linkWaka1 = "https://i.imgur.com/e641yTi.png"
linkArk1 = "https://i.imgur.com/DhV0DOD.png"
linkGruta1 = "https://4.bp.blogspot.com/-MplqVVRjFCo/VzYD90Cm5jI/AAAAAAAAX_Q/x2JbhgAwJwAi0cNTQq2l2j6hLCEX--gZgCLcB/s1600/Gruta%2Bde%2BBacaetava.jpg"
linkRat1 = "https://i.imgur.com/Mm8ebIk.png"
linkArk2 = "https://i.imgur.com/DhV0DOD.png"
def jogo():
    cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
    cena_gruta = Cena(img = linkGruta1)
    cenaIlha.meio = cena_gruta
    cena_gruta.meio = cenaIlha
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
    
    rat1 = Elemento(img = linkRat1, tit = "cena_gruta",
                         y = 300, x = 170, h = 400, w = 400)
    rat1.entra(cena_gruta)
    ark2 = Elemento(img = linkArk2, tit = "Ark",
                         y = 400, x = 170, h = 200, w = 200)
    ark2.entra(cena_gruta)  
    cena_gruta.vai()
jogo()