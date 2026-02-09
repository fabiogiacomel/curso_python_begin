# Exercícios 14 e 15: Condicionais (if/else)

**Foco:** Indentação e Decisão.

---

## Série A: Reprodução
**A1.** Crie `meu_if.py`.
**A2.** Copie e execute. Teste digitando números positivos e negativos.

```python
numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
else:
    print("O número não é positivo (zero ou negativo).")
```

---

## Série B: Modificação (Senha)
**B1.** Crie um sistema de senha.
O código abaixo só diz "Seja bem-vindo" se acertar.
Modifique para usar o `else` e dizer "Senha Incorreta" se errar.

```python
senha = input("Senha: ")
if senha == "1234":
    print("Seja bem-vindo!")
# Sua vez: Adicione o else aqui
```

---

## Série C: Criação (Radar de Velocidade)
**C1.** Crie um programa `radar.py`.
1.  Pergunte a velocidade do carro (`int`).
2.  Se for maior que 80 (`> 80`), diga "MULTADO!".
3.  Se não (`else`), diga "Velocidade OK".

---

## Série D: Desafio (Par ou Ímpar + Positivo ou Negativo)
**D1.** Usando o conhecimento de módulo `%`.
Crie um programa que pede um número e diz:
1.  Se é Par ou Ímpar.
2.  Se é Positivo ou Negativo.

Exemplo de uso:
```text
Digite: -4
Resultado: Par
Resultado: Negativo
```

**Dica:** Você vai precisar de dois blocos de `if/else` separados. Um para o par/ímpar, outro para o positivo/negativo. Não coloque um dentro do outro ainda!
