#! /usr/bin/env python
# -*- coding: UTF8 -*-
# joan.danae.main.py
# This file is part of  program Epydemic
# Copyright Â© 2020  Carlo Oliveira <carlo@nce.ufrj.br>,
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
def grep(substr):
    while True:
        line = yield
        if substr in line:
            print(f"found {substr}")
            
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fgen = fib()
#[print(next(fgen)) for _ in range(10)]
g = grep("users/created")
next(g)
g.send("users/created api took 3 ms.")