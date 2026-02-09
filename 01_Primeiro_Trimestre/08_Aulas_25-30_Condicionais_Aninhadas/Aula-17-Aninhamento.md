# Aula 17: Condicionais Aninhadas (Nested If)

**Objetivo:** Fazer perguntas sub-sequentes. "Se isso for verdade, então verifique aquilo."

---

## If dentro de If
Podemos colocar qualquer código dentro de um bloco indentado. Inclusive *outro* `if`.

### Exemplo: Login Seguro
Para entrar, preciso acertar o USUÁRIO **E** a SENHA.
Mas quero dar mensagens de erro diferentes para cada um.

```python
usuario = input("User: ")
senha = input("Pass: ")

if usuario == "admin":
    # Entrou no primeiro nível
    if senha == "1234":
        print("Acesso Total!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário desconhecido!")
```

### Atenção à Indentação!
Repare que o segundo `if` tem **DUAS** indentações (2 TABs).
Ele está dentro do primeiro.
