def filtrar_livros(livros, categoria=None, autor=None, preco_maximo=None):
    def corresponde(livro):
        if categoria and livro.get("categoria") != categoria:
            return False
        if autor and livro.get("autor") != autor:
            return False
        if preco_maximo is not None and livro.get("preco") > preco_maximo:
            return False
        return True
    return [livro for livro in livros if corresponde(livro)]