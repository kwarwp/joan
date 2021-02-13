# Miguel Roman-Okami Shiranui
from _spy.vitollino.main import Cena, Elemento, Texto

linkilhadeusas = "https://i.imgur.com/5UvVC5M.png"
linkOkami1 = "https://i.imgur.com/hr6DsqU.png"

def jogo():
    cenaIlha = Cena(img = "https://i.imgur.com/5UvVC5M.png")
    Okami1 = Elemento(img = linkOkami1, tit = "Okami 1",
                         style = dict (top = 200, left = 60, height = 100, width = 60))
    Okami1.entra(cenaIlha)
    cenaIlha.vai()
jogo()