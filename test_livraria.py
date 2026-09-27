import unittest
from livraria import filtrar_livros
class TestFiltroLivros(unittest.TestCase):
    def setUp(self):
    # Dados de teste
           self.livros = [
               {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "categoria": "Romance", "preco": 30.0},
               {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "categoria": "Fantasia", "preco": 50.0},
               {"titulo": "1984", "autor": "George Orwell", "categoria": "Ficção Científica", "preco": 40.0},
               {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "categoria": "Romance", "preco": 35.0}
           ]
    def test_filtrar_por_categoria(self):
        resultado = filtrar_livros(self.livros, categoria="Romance")
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado["titulo"], "Dom Casmurro")

    def test_filtrar_por_autor(self):
        resultado = filtrar_livros(self.livros, autor="George Orwell")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado["titulo"], "1984")

    def test_filtrar_por_preco_maximo(self):
        resultado = filtrar_livros(self.livros, preco_maximo=35.0)
        self.assertEqual(len(resultado), 2)

if __name__ == "__main__":
    unittest.main()