# Cibele Ribeiro
from _spy.vitollino.main import Cena, Elemento, Texto
linkFloresta = "https://a-static.mlcdn.com.br/618x463/painel-de-festa-em-tecido-sublimado-3d-caminho-na-floresta-sublime-sonhos/sublimesonhos/614357441/6a02b48244ffbcef0bf683dd4997e275.jpg"
linkFairy = "https://thefairyprincess.net/wp-content/uploads/2020/03/1_rev-min-724x1024.png"
# I love my forest!
def Historia():
    cenaFloresta = Cena(img = linkFloresta)
    fairy = Elemento(img = linkFairy,
                     tit = "Trixy",
                     style = dict(left=150, top=150, width=60, height=100))
    fairy.entra(cenaFloresta)
    txt1 = Texto(cenaFloresta,
                 "I love my forest!")
    fairy.vai = txt1.vai             
    cenaFloresta.vai()
Historia()
