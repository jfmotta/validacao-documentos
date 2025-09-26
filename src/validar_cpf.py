def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    d1 = calc_digito(cpf, 10)
    d2 = calc_digito(cpf[:9] + d1, 11)
    return cpf[-2:] == d1 + d2

