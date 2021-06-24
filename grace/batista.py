# joan.grace.batista.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" História de São João Batista.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    21.06
        Profeta Isaías.

"""
from _spy.vitollino.main import STYLE, JOGO as J
STYLE.update(width=1250, height="650px")


class Isaias:
    ISAIAS = "https://i.imgur.com/acDFUaT.jpg"
    def __init__(self):
        self.isaias = J.c(self.ISAIAS)
    def vai(self):
        self.isaias.vai()


if __name__ == "__main__":
    Isaias().vai()