# Sofia Marques 
from _spy.vitollino.main import Cena, Elemento, Texto
 
linkdofundo="https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/07/03/16/van-gogh-sunflowers-3.jpg"
linkdodetetive="https://www.alunira.com/IMG/arton77.png?1472829267"

# Acaba de acontecer um roubo aqui no museu do Van Gogh!

def Historia():
    cena1 = Cena(img = linkdofundo)
    detetive = Elemento(img=linkdodetetive,
                       tit="Detetive",
                       style=dict(left=150, top=60, width=150, height=200))
    detetive.entra(cena1)
    txtdetetive= Texto (cena1,
                        "Acaba de acontecer um roubo aqui no museu do Van Gogh!")
    detetive.vai=txtdetetive.vai                    
    cena1.vai()
    
Historia()