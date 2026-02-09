# Exercícios 12: Lógica e Decisão (Booleana)

---

## Série A: Reprodução
**A1.** Crie `meu_teste_logico.py`.
**A2.** Copie e execute:

```python
print(10 > 5)
print(10 == 10)
print(5 != 5)
print("Ana" == "ana") # Cuidado com maiúsculas
```
Anote no caderno o resultado de cada linha (True ou False).

---

## Série B: Modificação
**B1.** Mude os números para que todos os resultados sejam `False`.
Exemplo: Mude `10 > 5` para `10 < 5`.

---

## Série C: Criação (Verificador de Idade)
**C1.** Crie um programa que:
1.  Peça a idade do usuário.
2.  Crie uma variável `maior_de_idade` que recebe a comparação `idade >= 18`.
3.  Imprima: `É maior de idade? [True/False]`

---

## Série D: Desafio (Login Simples)
**D1.** Crie um sistema de login.
1.  Defina uma senha correta no código: `senha_mestra = "1234"`
2.  Peça para o usuário digitar a senha.
3.  Imprima `Acesso permitido: True` ou `Acesso permitido: False` dependendo se a senha for igual.

**D2.** (Extra) Adicione um usuário correto também. O acesso só é permitido se `usuario == "admin"` **E** `senha == "1234"`.

```python
usuario = input("User: ")
senha = input("Pass: ")
acesso = (usuario == "admin") and (senha == "1234")
print(f"Acesso: {acesso}")
```
