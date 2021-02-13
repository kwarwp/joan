# Miguel Roman-Okami Shiranui
from _spy.vitollino.main import Cena, Elemento, Texto

linkilhadeusas = "https://i.imgur.com/5UvVC5M.png"
linkOkami1 = "https://i.imgur.com/hr6DsqU.png"

def jogo():
    cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
    okami1 = Elemento(img = linkOkami1, tit = "Okami 1",
                         style = dict (top = 200, left = 60, height = 100, width = 60))
    okami1.entra(cenaIlha)
    txtokami1 = Texto(cenaIlha, "vamos para a ilha das deusas")
    okami1.vai = txtokami1.vai
    cenaIlha.vai()
jogo()