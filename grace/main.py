#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Epydemic
# Copyright © 2020  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

""" Jogo do Pedra Papel tesoura.

    Pedra amassa tesoura, tesoura corta papel e papel embrulha pedra.

No Classes in this module.

Changelog
---------
    20.04.1
        * NEW: Classe JoKenPo.

"""
__version__ = "20.04.01"
# joan.grace.main.py


class JoKenPo:
    def amassa(self):
        pass

    def corta(self):
        pass

    def embrulha(self):
        pass
        
    def perde(self):
        print("perdeu") 
        
    def ganha(self):
        print("ganhou")

class Rocha(JoKenPo):
    def __init__(self):
        print("você escolheu Rocha")
def main():
    escolhe = dict(r=Rocha, p=Papel, t=Tesoura)
    escolha = input("Digite r,p ou t para rocha, papel ou tesoura)
    escolheu = escolhe[escolha]


if __name__ == "__main__":
    main()