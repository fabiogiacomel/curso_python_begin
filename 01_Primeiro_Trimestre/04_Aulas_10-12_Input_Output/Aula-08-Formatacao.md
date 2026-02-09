# Aula 08: Formatação de Texto (f-strings)

**Objetivo:** Criar frases que misturam texto fixo e variáveis sem ficar "colando" pedacinhos com `+`.

---

## O Jeito Antigo (Chato)
Usar o `+` para juntar textos (concatenação) é trabalhoso e dá erro se colar número.
```python
nome = "Ana"
idade = 15
print("O nome é " + nome + " e ela tem " + str(idade) + " anos.")
```

## O Jeito Novo (f-strings)
Colocamos uma letra `f` antes das aspas e usamos chaves `{}` para colocar as variáveis direto no texto.

### Exemplo
Abra `src/exemplo_08_formatacao.py`.

```python
nome = "Ana"
idade = 15
salario = 1500.50

print(f"O nome é {nome} e ela tem {idade} anos.")
```

### Por que é melhor?
1.  Funciona com qualquer tipo (str, int, float, bool).
2.  É mais fácil de ler.
3.  Permite formatar números (ex: casas decimais).

### Formatando Decimais
Para mostrar só 2 casas depois da vírgula: `:.2f`

```python
print(f"O salário é R$ {salario:.2f}")
# Vai mostrar: R$ 1500.50
```
