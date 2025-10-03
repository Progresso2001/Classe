<p align="center">
  <img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>


Classe Pessoa em Python
Este projeto contém uma classe Pessoa que representa uma pessoa com atributos como nome, idade, cidade e país. A classe permite criar objetos com essas informações e fornecer uma descrição do endereço e um método para retornar um valor que simula um email.

Descrição da Classe
__init__(self, nome, idade, cidade, pais): Construtor que inicializa os atributos da pessoa.

endereco(self): Método que retorna uma string formatada com as informações da pessoa (nome, idade, cidade e país).

email(self): Método que retorna uma string concatenando os atributos (não retorna um email real, mas uma junção dos dados).

Observações
O método email atualmente concatena os atributos e não retorna um email válido.

É possível melhorar o método endereco para corrigir pequenos erros na string (exemplo: espaçamento e correção da palavra "cide" para "cidade").

O código de exemplo inclui instâncias da classe e imprime os resultados do método endereco.
