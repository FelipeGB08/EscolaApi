def cpf_invalido(numero_cpf):
    # Verifica se o tamanho é diferente de 11 OU se tem algo que não seja número
    return len(numero_cpf) != 11 or not numero_cpf.isdigit()

def rg_invalido(numero_rg):
    return len(numero_rg) != 9 or not numero_rg.isdigit()

def nome_invalido(nome):
    return not all(letra.isalpha() or letra.isspace() for letra in nome)