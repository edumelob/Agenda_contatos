import json
import os

FILE_NAME = "contacts.json"

# Cria o arquivo se não existir
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


class ContactManager:
    def __init__(self, filename):
        self.filename = filename

    def load_contacts(self):
        """Carrega contatos do arquivo JSON"""
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_contacts(self, contacts):
        """Salva contatos no arquivo JSON"""
        with open(self.filename, "w") as f:
            json.dump(contacts, f, indent=4)

    def add_contact(self, name, phone, email):
        contacts = self.load_contacts()
        contacts.append({"name": name, "phone": phone, "email": email})
        self.save_contacts(contacts)
        print(f"Contato {name} adicionado com sucesso!")

    def list_contacts(self):
        contacts = self.load_contacts()
        if not contacts:
            print("Nenhum contato encontrado.")
            return
        print("\n--- Lista de Contatos ---")
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

    def delete_contact(self, index):
        contacts = self.load_contacts()
        try:
            removed = contacts.pop(index - 1)
            self.save_contacts(contacts)
            print(f"Contato removido: {removed['name']}")
        except IndexError:
            print("Contato não encontrado.")


def menu():
    manager = ContactManager(FILE_NAME)

    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Remover contato")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome: ")
            phone = input("Telefone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)
        elif choice == "2":
            manager.list_contacts()
        elif choice == "3":
            index = int(input("Número do contato: "))
            manager.delete_contact(index)
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
