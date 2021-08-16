# Leonardo Sassone 
from _spy.vitollino.main import Cena, Elemento, Texto
linkdoNagato = "http://images2.wikia.nocookie.net/__cb20120802150510/naruto/images/8/85/Hanzo_wielding_Kusarigama.png"
linkKonohagurake = "https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/03/Konohagakure.jpg"
linkHanzo = "http://images2.wikia.nocookie.net/__cb20120802150510/naruto/images/8/85/Hanzo_wielding_Kusarigama.png"
# I need to practice to defeat Hanzõ! 
def Historia(): 
    cenaKonohagurake=Cena(img=linkKonohagurake) 
    
    nagato=Elemento(img=linkdoNagato,
                    tit="Nagato",
                    style=dict(left=150, top=60, width=60, height=200))
    nagato.entra(cenaKonohagurake)
    cenaKonohagurake.vai()
    
Historia() 