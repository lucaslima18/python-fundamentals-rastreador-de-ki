nome_do_guerreiro: str = str(input("Digite o nome do Guerreiro: ")).lower()
ki_base: int = int(input("Digite o nível do KI base do guerreiro: "))
raca: str = str(input("Digite a raça do guerreiro: ")).lower()

ki_base_alto = ki_base >= 1000
e_saiyajin = raca == "saiyajin"
e_lendario = ki_base > 9000 or e_saiyajin
pode_virar_super_saiyajin = ki_base_alto and e_saiyajin
ki_super_saiyajin = ki_base * 50
ki_super_saiyajin_2 = ki_base * 100