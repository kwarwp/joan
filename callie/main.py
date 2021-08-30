#Alice
from _spy.vitollino.main import Cena, Elemento, Texto
linkoftheboatandgirl="https://i.imgur.com/bLZMF23.png"
linkoftheoceanstorm="https://ike.io/content/images/2018/08/the_sea-1.jpg" 
def Historia():
    stormCena=Cena(img=linkoftheoceanstorm)
#Mary is salling for a long time. At the morning, she was just on a trip, but she went too far, and now, 4:00pm, Mary is fighting agains a big storm.
    mary=Elemento(img=linkoftheboatandgirl,
                 tit="Mary",
                 style=dict(left=90, top=60, width=230, height=200))
    mary.entra(stormCena)
    txtmary= Texto(stormcena,
                         "Mary is salling for a long time. At the morning, she was just on a trip, but she went too far, and now, 4:00pm, Mary is fighting agains a big storm.")
    mary.vai = txtMary.vai
    stormCena.vai()
    
Historia()
