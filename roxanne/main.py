# Miguel Roman-Okami Shiranui
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE.update(width=1150, height="600px")

linkilhadeusas = "https://i.imgur.com/5UvVC5M.png"
linkOkami1 = "https://i.imgur.com/hr6DsqU.png"
linkWaka1 = "https://i.imgur.com/e641yTi.png"
def jogo():
    cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
    okami1 = Elemento(img = linkOkami1, tit = "Okami 1",
                         y = 400, x = 60, h = 200, w = 200)
    okami1.entra(cenaIlha)
    
    
    waka1 = Elemento(img = linkWaka1, tit = "Waka 1",
                         style = dict (y = 380, x = 340, h = 200, w = 200))
    waka1.entra(cenaIlha)
    txtwaka1 = Texto(cenaIlha, "vamos para a ilha das deusas")
    waka1.vai = txtwaka1.vai
    
    cenaIlha.vai()
jogo()