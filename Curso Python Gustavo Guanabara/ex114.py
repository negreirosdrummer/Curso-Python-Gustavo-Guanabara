# CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO
# nota: o site pudim.com.br estava fora do ar, por isso decidi usar o site www.google.com

# MINHA RESOLUÇÃO
"""import urllib.request


def verifica_conexao(site):
    try:
        with urllib.request.urlopen(site) as response:
            if 200 <= response.status < 300:
                return True
            else:
                return False
    except urllib.error.URLError:
        return False


site = "https://www.google.com"
if verifica_conexao(site):
    print(f'\033[32mConsegui acessar o site Google com sucesso!')
else:
    print(f'\033[31mO site Google não está acessível no momento...')"""


# RESOLUÇÃO GUANABARA
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print(f'\033[31mO site Google não está acessível no momento...')
else:
    print(f'\033[32mConsegui acessar o site Google com sucesso!')
    # print(site.read())  # lê o arquivo html do site
