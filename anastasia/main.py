# joan.anastasia.main.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Jogo do Mistério do Castelo.

    Descubra o mistério deste castelo.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Cena
from adda.main import Fazenda
__version__ = "20.07"
CASTELO = "https://i.imgur.com/zOxshRh.jpg"

class Castelo:
    def __init__(self):
        castelo = Cena(CASTELO, direita=Fazenda())
        castelo.vai()
        
        
Castelo()
