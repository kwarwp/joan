
{'date': 'Mon May 04 2020 13:27:23.684 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: innermost.C.tree[0].args.indexOf is not a function>
'''},
{'date': 'Mon May 04 2020 13:29:21.648 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: innermost.C.tree[0].args.indexOf is not a function>
'''},
{'date': 'Mon May 04 2020 13:47:00.137 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 91
    gameg()        
  module <module> line 43
    pergaminho = Cena (img = PERGAMINHO)
NameError: name 'PERGAMINHO' is not defined
'''},