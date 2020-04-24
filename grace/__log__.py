
{'date': 'Fri Apr 24 2020 12:34:35.663 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 45
  escolha = input("Digite r,p ou t para rocha, papel ou tesoura)
                                                                ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Fri Apr 24 2020 12:34:53.639 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 50
    main()
  module <module> line 44
    escolhe = dict(r=Rocha, p=Papel, t=Tesoura)
NameError: name 'Papel' is not defined
'''},
{'date': 'Fri Apr 24 2020 12:37:54.465 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 58
    main()
  module <module> line 54
    escolheu = escolhe[escolha]()
  module <module> line 42
    output("você escolheu Rocha")
NameError: name 'output' is not defined
'''},