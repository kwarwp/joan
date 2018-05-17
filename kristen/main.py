from _spy.vitollino.main import Cena

B_NORTE = "https://i.imgur.com/DHfcJaf.jpg"
B_LESTE = "https://i.imgur.com/DKp1uPB.jpg"
B_OESTE = "https://i.imgur.com/doUqtLz.jpg"
B_SUL = "https://i.imgur.com/8DbF9Nc.jpg "

def criarsalag():
 b_norte = Cena(img=B_NORTE)
 b_sul = Cena(img=B_SUL)
 b_leste = Cena(img=B_LESTE)
 b_oeste = Cena(img=B_OESTE)
 
 b_norte.direita = b_leste
 b_norte.esquerda = b_oeste
 b_leste.esquerda = b_norte
 b_leste.direita = b_sul
 b_oeste.direita = b_norte
 b_oeste.esquerda = b_sul
 b_sul.direita = b_oeste
 b_sul.esquerda = b_leste
 b_norte.vai()
 
criarsalag()