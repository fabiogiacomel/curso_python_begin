# Exercícios 03: Return

---

## Série A: Reprodução
**A1.** Crie `meu_retorno.py`.
**A2.** Copie e execute. Note que não aparece NADA na tela, porque não tem `print` fora da função.
```python
def quadrado(numero):
    return numero * numero

res = quadrado(5)
# Para ver, precisamos imprimir a variável 'res'
print(res)
```

---

## Série B: Modificação (Conversor)
**B1.** Crie uma função `converter_dolar(reais)`.
**B2.** Considere que o dólar está R$ 5.00.
**B3.** A função deve retornar quantos dólares a pessoa tem. `reais / 5`.
**B4.** Teste com R$ 50.00 (deve retornar 10) e R$ 100.00 (deve retornar 20).

---

## Série C: Criação (Maior de 2)
**C1.** Crie uma função `maior(a, b)`.
**C2.** Use `if/else` para retornar o maior número entre os dois.
**C3.** Teste: `print(maior(10, 50))` -> Deve aparecer 50.

---

## Série D: Desafio (Validação de Texto)
**D1.** Crie uma função `limpar_nome(texto)`.
**D2.** A função deve:
    1.  Remover espaços do começo e fim (`.strip()`).
    2.  Deixar tudo maiúsculo (`.upper()`).
    3.  RETORNAR o texto limpo.
**D3.** Teste com: `nome = limpar_nome("   ana maria   ")`. O resultado deve ser `"ANA MARIA"`.
