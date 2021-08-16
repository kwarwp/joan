#Alice
from _spy.vitollino.main import Cena, Elemento, Texto
linkoftheboatandgirl="https://static.vecteezy.com/ti/vetor-gratis/p1/2141093-personagem-de-desenho-animado-rowing-the-boat-isolated-gr%C3%A1tis-vetor.jpg"
linkoftheoceanstorm="https://ike.io/content/images/2018/08/the_sea-1.jpg" 
def Historia():
    stormCena=Cena(img=linkoftheoceanstorm)
#Mary is salling for a long time. At the morning, she was just on a trip, but she went too far, and now, 4:00pm, Mary is fighting agains a big storm.
    mary=Elemento(img=linkoftheboatandgirl,
                 tit="Mary",
                 style=dict(left=110, top=60, width=200, height=100))
    mary.entra(stormCena)
    stormCena.vai()
    
Historia()