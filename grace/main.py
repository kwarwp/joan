#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Epydemic
# Copyright Â© 2020  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

""" Jogo do Pedra Papel tesoura.

    Pedra amassa tesoura, tesoura corta papel e papel embrulha pedra.

No Classes in this module.

Changelog
---------
    20.06
        * NEW: Use alert.
    20.04.1
        * NEW: Classe JoKenPo.

"""
from browser import alert
__version__ = "20.04.01"
# joan.grace.main.py


class JoKenPo:
    def amassa(self):
        self.perde()

    def corta(self):
        self.perde()

    def embrulha(self):
        self.perde()
        
    def perde(self):
        alert("perdeu") 
        
    def ganha(self):
        alert("ganhou")

class Rocha(JoKenPo):
    def __init__(self):
        alert("você escolheu Rocha")

class Papel(JoKenPo):
    def __init__(self):
        alert("você escolheu Papel")

class Tesoura(JoKenPo):
    def __init__(self):
        alert("você escolheu Rocha")
def main():
    escolhe = dict(r=Rocha, p=Papel, t=Tesoura)
    escolha = input("Digite r,p ou t para rocha, papel ou tesoura")
    escolheu = escolhe[escolha]()


if __name__ == "__main__":
    main()