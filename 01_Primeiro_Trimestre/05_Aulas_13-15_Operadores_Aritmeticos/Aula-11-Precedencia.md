# Aula 11: Precedência (Ordem das Contas)

**Objetivo:** Não errar contas por fazer na ordem errada.

---

## A Regra
O Python segue a matemática rígida. A ordem de quem é resolvido primeiro é:

1.  **Parênteses `()`**: O que está dentro ganha prioridade total.
2.  **Potência `**`**: Exponenciação.
3.  **Multiplicação e Divisão `* / // %`**: Quem vier primeiro na linha.
4.  **Soma e Subtração `+ -`**: Os últimos.

### Exemplo Clássico
Quanto é `2 + 3 * 4`?

*   Se fizer na ordem de leitura: 2+3 = 5, depois 5*4 = **20**. (ERRADO)
*   Pela regra matemática: 3*4 = 12, depois 2+12 = **14**. (CERTO)

Para forçar a soma primeiro, USE PARÊNTESES:
`(2 + 3) * 4` = `5 * 4` = **20**.

**Dica de Ouro:** Na dúvida, use parênteses. Mal não faz.
