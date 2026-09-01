print("Bem-vindo ao verificador de senha!") 
print("Para criar uma senha segura ela dever ter pelo menos um caractere especial e um número")
def cadastro_senha():
    inserir_senha = input("Digite sua senha:")
    print("Ok, vamos verificar se sua senha é válida.")
    
    tamanho_senha = len(inserir_senha)
    caracteres_especiais = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    numeros = "0123456789"
    tem_especial = '1' in inserir_senha or '2' in inserir_senha or '3' in inserir_senha or '4' in inserir_senha or '5' in inserir_senha or '6' in inserir_senha or '7' in inserir_senha or '8' in inserir_senha or '9' in inserir_senha or '0' in inserir_senha
    tem_especial = '!' in inserir_senha or '@' in inserir_senha or '#' in inserir_senha
    tem_numero = any(c.isdigit() for c in inserir_senha)
    
    if tamanho_senha <= 8:
        print("Senha inválida! A senha deve ter no mínimo 8 caracteres.")
        return inserir_senha
    else:
        print("Senha válida! Sua senha atende um dos requisitos de segurança.")
    
    verificar_senha = input("Digite sua senha novamente para verificação:")
    while verificar_senha != inserir_senha:
        print("Senha incorreta! Tente novamente.")
        verificar_senha = input("Digite sua senha novamente para verificação:")
    print("Senha verificada com sucesso!")

def senha_valida(tem_especial,tem_numero):
    if tem_especial and tem_numero:
        print("Senha válida! Sua senha atende aos requisitos de segurança.")
def senha_media(tem_especial, tem_numero):
    if tem_especial != tem_numero:   
        print("Senha média! Sua senha atende a alguns requisitos de segurança.")

def senha_fraca(tem_especial, tem_numero):
    if not tem_especial and not tem_numero:   
        print("Senha fraca! Sua senha não atende aos requisitos de segurança.")


inserir_senha, tem_especial, tem_numero = cadastro_senha()
senha_valida(tem_especial, tem_numero)     
senha_media(tem_especial, tem_numero)
senha_fraca(tem_especial, tem_numero)