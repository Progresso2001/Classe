class Pessoa():
    def __init__(self, nome, idade, cidade, pais):
        self.nome=nome
        self.idade=idade
        self.cidade=cidade
        self.pais=pais
    def endereco(self):
        localidade= 'Chamo-me,' + self.nome.title() + ' ' + 'tenho' + str(self.idade) + ' ' + 'de idade ' + 'sou da cide de ' + self.cidade + 'nasci em ' + self.pais
        return localidade
    def email(self): #como chamar o outro metodo
        post=self.nome + self.idade + self.cidade + self.pais
        return post
    
pessoa=Pessoa('joaquim', 43, 'Luanda', 'Angola')
pessoa1=Pessoa('manuel', 53, 'cabinda', 'Portugal')
pessoa2=Pessoa('carlos', 33, 'uige', 'Brazil')
# gmail=Pessoa("joaquim", "99@", ".com", "post")
print(pessoa.endereco())
print(pessoa1.endereco())
print(pessoa2.endereco())
# print(gmail.email())   