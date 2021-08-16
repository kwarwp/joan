
# Leonardo Sassone 
from _spy.vitollino.main import Cena, Elemento, Texto
linkDoNaruto = "https://i.imgur.com/aHGM7mE.png"
linkKonohagurake = "https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/03/Konohagakure.jpg"
linkHanzo = "http://images2.wikia.nocookie.net/__cb20120802150510/naruto/images/8/85/Hanzo_wielding_Kusarigama.png"
# I need to practice to defeat Hanzõ! 
def Historia(): 
    cenaKonohagurake=Cena(img=linkKonohagurake) 
    
    naruto = Elemento(img=linkDoNaruto,
                     tit="naruto",
                     style=dict(left=75, top=60, width=150, height=200))
    naruto.entra(cenaKonohagurake)
    cenaKonohagurake.vai()
    
Historia() 

# No canto da dobra da perna esquerda, se eu botar a seta do mouse ali vai aparecer Naruto pequeno, mas aparece