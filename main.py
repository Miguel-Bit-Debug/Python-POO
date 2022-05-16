from pessoa import Pessoa

p1 = Pessoa('Miguel', 21)
p2 = Pessoa('João', 32)

print(p1._idade)

p1.get_idade(2001)

p1 = Pessoa.por_ano_nascimento('Miguel', 2001)
print(p1)
print(p1._nome, p1._idade)

print(p1.gera_id())

