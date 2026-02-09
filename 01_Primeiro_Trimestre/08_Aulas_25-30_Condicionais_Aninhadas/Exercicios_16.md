# Exercícios 16 e 17: Condicionais Complexas

---

## Série A: Reprodução
**A1.** Crie `meu_elif.py`.
**A2.** Faça um semáforo:
```python
cor = input("Cor do semáforo (verde/amarelo/vermelho): ")

if cor == "verde":
    print("Siga")
elif cor == "amarelo":
    print("Atenção")
elif cor == "vermelho":
    print("Pare")
else:
    print("Cor inválida! O semáforo quebrou.")
```

---

## Série B: Modificação (IMC Simples)
**B1.** Crie um calculador de IMC. `imc = peso / (altura * altura)`.
**B2.** Use `if/elif/else` para classificar:
-   Abaixo de 18.5: "Abaixo do peso"
-   Entre 18.5 e 24.9: "Peso normal" (Dica: `elif imc < 25:`)
-   Acima disso: "Sobrepeso"

---

## Série C: Criação (Calculadora com Menu)
**C1.** Crie uma calculadora que pergunta a operação.
1.  Peça dois números (`n1`, `n2`).
2.  Mostre um menu:
    *   1 - Somar
    *   2 - Subtrair
    *   3 - Multiplicar
3.  Peça a opção (`opcao = input()`).
4.  Use `if/elif/elif` para fazer a conta certa baseada na opção.

---

## Série D: Desafio (Triângulos)
**D1.** Peça 3 lados de um triângulo (`a`, `b`, `c`).
**D2.** Verifique se é um triângulo válido (A soma de dois lados tem que ser maior que o terceiro).
*   Se NÃO for triângulo, avise.
*   Se FOR triângulo (Aninhamento!), diga qual o tipo:
    -   Equilátero (3 lados iguais)
    -   Isósceles (2 lados iguais)
    -   Escaleno (3 lados diferentes)
