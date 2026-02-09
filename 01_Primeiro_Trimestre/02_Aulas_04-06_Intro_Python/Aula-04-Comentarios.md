# Aula 04: Comentários

**Objetivo:** Aprender a deixar notas no código que o computador ignora.

---

## O Símbolo `#` (Cerquilha / Hashtag)
Tudo que você escreve depois de um `#` na mesma linha é **invisível** para o computador. Serve apenas para humanos lerem.

### Exemplo
Abra `src/exemplo_04_comentarios.py`.

```python
# Este comando escreve um oi
print("Oi")

print("Tchau") # Este comando escreve tchau
```

### Por que usar?
1.  **Explicar:** Dizer o que um bloco complexo faz.
2.  **Desativar:** "Desligar" uma linha de código sem apagar ela (útil para testar).

---

## Comentários de Múltiplas Linhas
Podemos usar três aspas `"""` para escrever textos longos.

```python
"""
Este é um comentário
que ocupa várias
linhas. O Python ignora tudo isso.
"""
print("Agora o código volta a funcionar")
```
