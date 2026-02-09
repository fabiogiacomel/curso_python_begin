# Exercícios 06: Iteração em Listas

---

## Série A: Reprodução
**A1.** Crie `meu_iterador.py`.
**A2.** Copie e execute:
```python
amigos = ["Ana", "Bia", "Caio"]
for a in amigos:
    print(f"Bom dia, {a}!")
```

---

## Série B: Modificação (Contador de Letras)
**B1.** Use a lista de amigos acima.
**B2.** Dentro do loop, mude o print para mostrar o tamanho do nome (`len(a)`).
Exemplo: "Ana tem 3 letras".

---

## Série C: Criação (O Maior Número)
**C1.** Crie uma lista com 5 números aleatórios: `lista = [10, 50, 2, 80, 5]`.
**C2.** Crie uma variável `maior = 0`.
**C3.** Faça um loop para percorrer a lista.
**C4.** Dentro do loop, use um `if`: se o número atual for maior que a variável `maior`, atualize ela (`maior = numero_atual`).
**C5.** No final, imprima o maior número encontrado.

---

## Série D: Desafio (Busca de Nome)
**D1.** Crie uma lista com 5 nomes.
**D2.** Pergunte ao usuário: "Qual nome você procura?".
**D3.** Faça um loop para procurar.
*   Se achar: Mostre "Encontrado!" e use o `break`.
*   (Opcional) Se terminar o loop e não achar, mostre "Não encontrado" (Dica: use uma variável `achei = False` antes do loop).
