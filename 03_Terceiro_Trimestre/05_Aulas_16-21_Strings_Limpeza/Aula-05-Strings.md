# Aula 05: Manipulando Textos (Strings)

**Objetivo:** O usuário sempre digita errado. Nosso trabalho é corrigir.

---

## Strings são Listas de Letras!
Tudo o que você aprendeu com Listas (`lista[0]`, `lista[0:3]`) funciona com textos.
```python
nome = "Python"
print(nome[0]) # "P"
```

## Métodos de Limpeza

### 1. Maiúsculas e Minúsculas
Para padronizar (comparar sem erros).
*   `texto.upper()`: TUDO MAIÚSCULO.
*   `texto.lower()`: tudo minúsculo.
*   `texto.capitalize()`: Só a primeira maiúscula.

### 2. Remover Espaços (`strip`)
Tira os espaços "fantasmas" do começo e do fim (muito comum em formulários).
*   `"  abc  ".strip()` -> Vir "abc".

### 3. Substituir (`replace`)
Troca uma coisa por outra.
*   `texto.replace("velho", "novo")`

### Exemplo Prático
O usuário digita: "  sim  "
O programa espera: "SIM"
```python
resp = input("Deseja sair? ")
if resp.strip().upper() == "SIM":
    print("Saindo...")
```
Não importa se ele digitou "sim", "SIM", "  Sim  "... vai funcionar!
