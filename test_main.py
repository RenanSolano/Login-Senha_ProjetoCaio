import unittest
from unittest.mock import patch
from cadastro import *
from login import *

class MainTest(unittest.TestCase):
    @patch('builtins.input', lambda *args: '')

    def test_cad_usuario(self):
        inputs = iter('ettore','senha','cachorro','gato')

        with patch('builtins.input', lambda *_: next(inputs)):
            usuario = cad_usuario()
            self.assertEqual(usuario.login, 'ettore')
            self.assertEqual(usuario.senha, hashlib.sha256('senha'.encode()).hexdigest())


    def test_login_usuario(self):
        inputs = iter('ettore','senha','cachorro','gato')
        with patch('builtins.input', lambda *_: next(inputs)):
            usuario = login_usuario()
            self.assertEqual(usuario.login, 'ettore')
            self.assertEqual(usuario.senha, hashlib.sha256('senha'.encode()).hexdigest())
            usuario = login_usuario()
            self.assertIsNone(usuario)
            
