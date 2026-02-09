# Exercícios 07: Visualização

---

## Série A: Reprodução
**A1.** Crie `meu_grafico.py`.
**A2.** Copie e execute:
```python
notas = [2, 5, 8, 10]
for n in notas:
    print("*" * n)
```

---

## Série B: Modificação (Alinhamento)
**B1.** Mude o código acima para mostrar o número antes da barra.
Exemplo: `5 | *****`
**B2.** Use a formatação `f"{n:02d}"` para que os números fiquem sempre com 2 dígitos (02, 05, 10).

---

## Série C: Criação (Votação)
**C1.** Crie duas listas:
    `candidatos = ["A", "B", "C"]`
    `votos = [15, 32, 8]`
**C2.** Faça um loop para percorrer as duas (pode usar `range(len(candidatos))`).
**C3.** Imprima um gráfico onde cada voto vale um quadrado `■` (pode copiar esse caractere).

---

## Série D: Desafio (Escala Reduzida)
**D1.** Imagine que os votos são: `[150, 320, 80]`.
**D2.** Se você imprimir 320 quadrados, vai quebrar a tela.
**D3.** Faça cada quadrado valer 10 votos. (Divida o valor por 10 antes de multiplicar o texto).
**D4.** Imprima o gráfico ajustado.
