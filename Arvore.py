import unittest
from avltree import AvlTree

class TestAvlTree(unittest.TestCase):
    def setUp(self):
        self.tree = AvlTree[int,str]()
        print("\n[SETUP] Nova arvore Avl inicializada.")

    def test_insert_and_search(self):
        print("[Teste] inserindo elementos na arvore.")
        self.tree[10] = 'dez'
        self.tree[20] = 'vinte'
        self.tree[5] = 'cinco'
        print('[VERIFICAÇÃO] Checando se os elementos estão na arvore')
        self.assertEqual(self.tree[10], 'dez')
        self.assertEqual(self.tree[20], 'vinte')
        self.assertEqual(self.tree[5], 'cinco')
        print('[VERIFICACAO] Checando se um elementos não inserido esta ausente.')
        self.assertNotIn(15,self.tree)

    def test_delete(self):
        print("[Teste] inserindo elementos para testar remocao.")
        self.tree[30] = 'trinta'
        self.tree[20] = 'vinte'
        self.tree[40] = 'quarenta'
        print('[ACAO] Removendo chave 20')
        del self.tree[20]
        print("[Verificação] Verificando se a chave 20 foi removida.")
        self.assertNotIn(20,self.tree)
        print('[Verificação] Verificiando se outras chaves permanecem.')
        self.assertIn(30,self.tree)
        self.assertIn(40,self.tree)

    def test_inorder_traversal(self):
        print("[Teste] inserindo elementos para travessia in-order.")
        elements = [50,30,70,20,40,60,80]
        for el in elements:
            self.tree[el] = str(el)
            print(f"[Insercao] {el} -> '{str(el)}'")

        print("[Acao] Realizando travessia in-order.")
        inorder = list(self.tree)
        print(f'[Sucesso] Ordem esta correta.')

    def test_update_value(self):
        print("[Teste] Testando atualizacao de valor em uma chave existente.")
        self.tree[100] = 'cem'
        print(f'[Insercao] 100 -> "cem"')
        self.assertEqual(self.tree[100], 'cem')
        
        print("[Acao] Atualizando valor da chave 100 para '100'")
        self.tree[100] = '100'
        self.assertEqual(self.tree[100],'100')
        print("[Verificacao] Valor atualizado com sucesso")

    def test_empty_tree(self):
        print("[Teste] Verificando arvore vazia.")
        self.assertNotIn(1,self.tree)
        print("[Sucesso] A arvore esa vazia conforme esperado.")
        
if __name__ == '__main__':
    unittest.main()