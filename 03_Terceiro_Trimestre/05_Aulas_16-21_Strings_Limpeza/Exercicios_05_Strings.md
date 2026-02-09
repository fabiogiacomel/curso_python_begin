# Exercícios 05: Strings

---

## Série A: Reprodução
**A1.** Crie `meu_texto.py`.
**A2.** Copie e execute:
```python
frase = "  Aprendendo Python  "
print(frase.strip())
print(frase.upper())
print(frase.replace("Python", "Lógica"))
```

---

## Série B: Modificação (Cadastro)
**B1.** Crie um programa que pede o nome completo.
**B2.** Mostre o nome todo em maiúsculo.
**B3.** Mostre o nome todo em minúsculo.
**B4.** Mostre quantas letras tem o nome (use `len`).
*   **Atenção:** Se tiver espaços, o `len` conta. Tente usar `strip()` antes de contar, ou não se preocupe com isso por enquanto.

---

## Série C: Criação (Detector de Palavrão)
**C1.** Peça uma frase para o usuário.
**C2.** Se a frase contiver a palavra "chato" (use `if "chato" in frase:`), substitua por "legal".
**C3.** Imprima a frase final (censurada).

---

## Série D: Desafio (Login Perfeito)
**D1.** Crie uma variável `senha_correta = "SECRET123"`.
**D2.** Peça a senha para o usuário.
**D3.** Antes de comparar, limpe os espaços (`strip`) e transforme em maiúscula (`upper`).
**D4.** Assim, se o usuário digitar "  secret123 ", o login deve ser aprovado.
