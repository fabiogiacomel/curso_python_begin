# Exercícios 04: Bibliotecas

---

## Série A: Reprodução
**A1.** Crie `meus_imports.py`.
**A2.** Copie e execute o "Jogo do Dado":
```python
import random
dado = random.randint(1, 20) # Dado de RPG
print(f"Rolagem: {dado}")
```

---

## Série B: Modificação (Sorteio de Nomes)
**B1.** Crie uma lista com o nome de 3 amigos.
**B2.** Use `random.choice(lista)` para escolher quem vai pagar o lanche.
**B3.** Imprima "O escolhido foi: [nome]".

---

## Série C: Criação (Raiz Quadrada)
**C1.** Importe `math`.
**C2.** Peça um número para o usuário (`input` + `float`).
**C3.** Calcule a raiz quadrada dele (`math.sqrt`).
**C4.** Mostre o resultado bonitinho.

---

## Série D: Desafio (Adivinhe o Número)
**D1.** O computador vai "pensar" em um número.
1.  Importe `random`.
2.  Sorteie um número secreto entre 1 e 5: `secreto = random.randint(1, 5)`.
3.  Peça para o usuário tentar adivinhar (`input`).
4.  Se acertar, parabéns. Se errar, diga qual era o número secreto.
    *   Dica: Não esqueça de converter o `input` para `int`.
