pessoa = {
    "nome": "Henrique",
    "idade": 20,
    "cidade": "Jaraguá do Sul"
}
print (pessoa)

print (f'Nome: {pessoa["nome"]}\nCidade: {pessoa["cidade"]}')

#Adicionar uma nova chave e seu respectivo valor
pessoa["email"] = "henrique@gmail.com"
print(pessoa)

#remover uma chave
del pessoa["idade"]
print(pessoa)