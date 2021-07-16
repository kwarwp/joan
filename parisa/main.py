# Nara de Faria e Sousa Cardenuto
from _spy.vitollino.main import Cena, Elemento, Texto
linkFlorestasemnada = "https://image.freepik.com/vetores-gratis/paisagem-de-floresta-dos-desenhos-animados-com-plantas-e-arvores_43633-5886.jpg"
linkMulher = "https://i.imgur.com/5M7D5s5.png"
# Hi! Today i'm doing a trail in this forest.
def Historia():
    cenaFloresta = Cena(img = linkFlorestasemnada)
    mulher = Elemento(img = linkMulher,
                    tit = "Lara",
                    style = dict(left=150, top=150, width=70, height=200))
    mulher.entra(cenaFloresta)
    cenaFloresta.vai()
Historia()
