# Aula 04: Break e Continue

**Objetivo:** Quebrar regras. Parar antes da hora ou pular quem não interessa.

---

## 1. O comando `break` (Quebrar/Parar)
O `break` funciona como um freio de emergência.
Quando o Python encontra um `break`, ele **SAI** do loop na hora e continua o programa depois dele.

### Exemplo: Procurando um número
```python
for n in range(100):
    if n == 5:
        print("Achei o 5! Parando...")
        break # Não precisa ir até o 99.
    print(n)
```

## 2. O comando `continue` (Continuar/Pular)
O `continue` diz: "Pare tudo o que está fazendo AQUI e vá para a PRÓXIMA volta".
Ele não sai do loop, só pula o resto do código daquela volta específica.

### Exemplo: Pular números Pares
```python
for n in range(5):
    if n % 2 == 0:
        continue # É par? Pula o print e vai pro próximo!
    print(f"O número {n} é ímpar")
```

---

## 3. O Truque do `while True`
Muitos programadores usam um loop infinito proposital (`while True`) e usam o `break` para sair quando o usuário quiser.

```python
while True:
    msg = input("Digite 'sair' para parar: ")
    if msg == "sair":
        break
    print("Você digitou:", msg)
```
Isso é muito comum em menus de jogos e sistemas!
