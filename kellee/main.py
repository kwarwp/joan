from _spy.vitollino.main import Cena

A_NORTE = "https://i.imgur.com/lLB3EFx.jpg"
A_LESTE = "https://i.imgur.com/ymN6qmh.jpg"
A_OESTE = "https://i.imgur.com/72Z207w.jpg"
A_SUL = "https://i.imgur.com/jHB3DgA.jpg"

B_NORTE = "https://i.imgur.com/5gsI06u.jpg"
B_LESTE = "https://i.imgur.com/Ud9wEDw.jpg"
B_OESTE = "https://i.imgur.com/JNIjEgd.jpg"
B_SUL = "https://i.imgur.com/8uZrXeI.jpg"

C_NORTE = "https://i.imgur.com/2dRpuCl.jpg"
C_LESTE = "https://i.imgur.com/OkZfcEx.jpg"
C_OESTE = "https://i.imgur.com/ETxjNen.jpg"
C_SUL = "https://i.imgur.com/G7OLtjm.jpg"

D_NORTE = "https://i.imgur.com/26okh3m.jpg"
D_LESTE = "https://i.imgur.com/igzQXZu.jpg"
D_OESTE = "https://i.imgur.com/8kCDuf5.jpg"
D_SUL = "https://i.imgur.com/vwtKnJa.jpg"

E_NORTE = "https://i.imgur.com/T3XToj0.jpg"
E_LESTE = "https://i.imgur.com/u9rZIOG.jpg"
E_LESTEA = "https://i.imgur.com/E2oUQwa.jpg"
E_SUL = "https://i.imgur.com/ZBsXQk7.jpg"

F_NORTE = "https://i.imgur.com/2mrITem.jpg"
F_OESTE = "https://i.imgur.com/CPc3fGM.jpg"
F_SUL = "https://i.imgur.com/VGmsnAq.jpg"

G_NORTE = "https://i.imgur.com/DKp1uPB.jpg"
G_LESTE = "https://i.imgur.com/DHfcJaf.jpg"
G_SECRETO = "https://i.imgur.com/doUqtLz.jpg"
G_SUL = "https://i.imgur.com/8DbF9Nc.jpg"

ED = "https://i.imgur.com/FWKz9Ol.png"
EDI = "https://i.imgur.com/hIcRUrM.png"
GUARDA = "https://i.imgur.com/WReBA4R.png"

def criarsalas():
 
 a_norte = Cena(img=A_NORTE)
 a_sul = Cena(img=A_SUL)
 a_leste = Cena(img=A_LESTE)
 a_oeste = Cena(img=A_OESTE)
 
 b_norte = Cena(img=B_NORTE)
 b_sul = Cena(img=B_SUL)
 b_leste = Cena(img=B_LESTE)
 b_oeste = Cena(img=B_OESTE)
 
 c_norte = Cena(img=C_NORTE)
 c_sul = Cena(img=C_SUL)
 c_leste = Cena(img=C_LESTE)
 c_oeste = Cena(img=C_OESTE)
 
 d_norte = Cena(img=D_NORTE)
 d_sul = Cena(img=D_SUL)
 d_leste = Cena(img=D_LESTE)
 d_oeste = Cena(img=D_OESTE)
 
 e_norte = Cena(img=E_NORTE)
 e_sul = Cena(img=E_SUL)
 e_leste = Cena(img=E_LESTE)
 e_lestea = Cena(img=E_LESTEA)
 
 f_norte = Cena(img=F_NORTE)
 f_sul = Cena(img=F_SUL)
 f_oeste = Cena(img=F_OESTE)
 
 g_norte = Cena(img=G_NORTE)
 g_sul = Cena(img=G_SUL)
 g_leste = Cena(img=G_LESTE)
 g_secreto = Cena(img=G_SECRETO)
 
 a_norte.direita = a_leste
 a_norte.esquerda = a_oeste
 a_norte.meio = b_norte
 a_leste.esquerda = a_norte
 a_leste.direita = a_sul
 a_oeste.direita = a_norte
 a_oeste.esquerda = a_sul
 a_sul.direita = a_oeste
 a_sul.esquerda = a_leste
 
 b_norte.direita = b_leste
 b_norte.esquerda = b_oeste
 b_norte.meio = c_norte
 b_leste.esquerda = b_norte
 b_leste.direita = b_sul
 b_oeste.direita = b_norte
 b_oeste.esquerda = b_sul
 b_sul.direita = b_oeste
 b_sul.esquerda = b_leste
 b_sul.meio = a_norte
 
 c_norte.direita = c_leste
 c_norte.esquerda = c_oeste
 c_norte.meio = d_norte
 c_leste.esquerda = c_norte
 c_leste.direita = c_sul
 c_oeste.direita = c_norte
 c_oeste.esquerda = c_sul
 c_sul.direita = c_oeste
 c_sul.esquerda = c_leste
 c_sul.meio = b_norte
 
 d_norte.direita = d_leste
 d_norte.esquerda = d_oeste
 d_leste.esquerda = d_norte
 d_leste.direita = d_sul
 d_oeste.direita = d_norte
 d_oeste.esquerda = d_sul
 d_oeste.meio = e_norte
 d_sul.direita = d_oeste
 d_sul.esquerda = d_leste
 d_sul.meio = c_norte
 
 e_norte.direita = e_sul
 e_norte.esquerda = e_leste
 e_leste.esquerda = e_sul
 e_leste.direita = e_norte
 e_leste.meio = e_lestea
 e_lestea.esquerda = e_sul
 e_lestea.direita = e_norte
 e_lestea.meio = f_norte
 e_sul.direita = e_leste
 e_sul.esquerda = e_norte
 e_sul.meio = d_norte
 
 f_norte.direita = f_sul
 f_norte.esquerda = f_oeste
 f_oeste.direita = f_norte
 f_oeste.esquerda = f_sul
 f_oeste.meio = g_norte
 f_sul.direita = f_oeste
 f_sul.esquerda = f_norte
 f_sul.meio = e_norte
 
 g_norte.direita = g_leste
 g_norte.esquerda = g_sul
 g_norte.meio = g_secreto
 g_leste.esquerda = g_norte
 g_leste.direita = g_sul
 g_secreto.meio = g_norte
 g_sul.direita = g_norte
 g_sul.esquerda = g_leste
 
 a_norte.vai()
 
criarsalas()
