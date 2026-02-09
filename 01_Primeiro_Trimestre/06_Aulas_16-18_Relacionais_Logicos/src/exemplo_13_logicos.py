# Exemplo 13: Lógica Booleana

nota = 7.5
frequencia = 80 # %

# Regra: Passa se nota >= 7 E frequencia >= 75
aprovado = nota >= 7 and frequencia >= 75

print(f"Nota: {nota}")
print(f"Frequência: {frequencia}%")
print(f"Aluno aprovado? {aprovado}")

# Exemplo de OU (or)
tem_ingresso = False
e_amigo_do_dono = True

pode_entrar = tem_ingresso or e_amigo_do_dono
print(f"Pode entrar na festa? {pode_entrar}")
