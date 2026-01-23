nome_User = input("Digite seu nome (usuário): ")
idade_User = input("Digite sua idade: ")
user_texto = lambda: f"O {nome_User} possui {idade_User} anos."
mensagem = user_texto()
print(mensagem)