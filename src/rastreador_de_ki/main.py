
"""
O script deve:

1. Pedir ao usuário o **nome** do guerreiro.
2. Pedir o **nível de Ki base** (convertendo de `str` para `int`).
3. Pedir a **raça** do guerreiro.
4. Calcular:
   - Ki em Super Saiyajin (multiplicador x50).
   - Ki em Super Saiyajin 2 (multiplicador x100).
5. Avaliar, com operadores lógicos e de comparação:
   - Se o Ki base é considerado alto (>= 1000).
   - Se o guerreiro é Saiyajin.
   - Se o guerreiro pode se tornar Super Saiyajin (Ki alto **e** é Saiyajin).
   - Se o guerreiro é considerado lendário (Ki base > 9000 **ou** é Saiyajin).
6. Exibir todos os resultados formatados no terminal,
"""

nome_do_guerreiro: str = str(input("Digite o nome do Guerreiro: ")).lower()
ki_base: int = int(input("Digite o nível do KI base do guerreiro: "))
raca: str = str(input("Digite a raça do guerreiro: ")).lower()

ki_base_alto = ki_base >= 1000
e_saiyajin = raca == "saiyajin"
e_lendario = ki_base > 9000 or e_saiyajin
pode_virar_super_saiyajin = ki_base_alto and e_saiyajin
ki_super_saiyajin = ki_base * 50
ki_super_saiyajin_2 = ki_base * 100

print("\n\n###### FIXA DO GUERREIRO ######\n")
print(f"Guerreiro: {nome_do_guerreiro}")
print(f"Raça: {raca}")
print(f"Ki base: {ki_base}")
print(f"ki Super Saiyajin: {ki_super_saiyajin}")
print(f"ki Super Saiyajin 2: {ki_super_saiyajin_2}")
print(f"O ki base é alto?: {ki_base_alto}")
print(f"O guerreiro pode virar super saiyajin? {pode_virar_super_saiyajin}")    
print(f"O guerreiro pode ser considerado um ser lendário? {e_lendario}")
print("\n###############################")

print("Fim da execução")
