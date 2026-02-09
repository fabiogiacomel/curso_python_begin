# Exercícios 04: Listas e Índices

---

## Série A: Reprodução
**A1.** Crie `minha_lista.py`.
**A2.** Copie e execute:
```python
herois = ["Batman", "Aranha", "Thor", "Hulk"]
print(herois[0]) # Primeiro
print(herois[3]) # Quarto
print(herois[-1]) # Último
```

---

## Série B: Modificação (Troca)
**B1.** No código acima, o Hulk ficou bravo e foi embora. O "Homem de Ferro" entrou no lugar dele.
Mude o valor do índice 3 para "Homem de Ferro".
`herois[3] = "..."`
Imprima a lista inteira depois para conferir.

---

## Série C: Criação (Dias da Semana)
**C1.** Crie uma lista com os 7 dias da semana (começando em Domingo).
**C2.** Peça para o usuário digitar um número de 1 a 7.
**C3.** Imprima o dia correspondente.
**Atenção:** Se ele digitar 1, ele quer o Domingo (índice 0). Você precisa subtrair 1!
`print(dias[numero - 1])`

---

## Série D: Desafio (Média da Lista)
**D1.** Dada a lista: `valores = [10, 20, 30, 40, 50]`
1.  Faça a soma manual: `soma = valores[0] + valores[1] ...`
2.  Calcule a média (soma dividida por 5).
3.  Imprima a média.
