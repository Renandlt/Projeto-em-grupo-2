import csv
import datetime

class Pergunta:
    def __init__(self, texto, opcoes):
        self.texto = texto
        self.opcoes = opcoes

class Resposta:
    def __init__(self, idade, genero, respostas):
        self.idade = idade
        self.genero = genero
        self.respostas = respostas
        self.data = datetime.date.today().strftime('%d/%m/%Y')
        self.hora = datetime.datetime.now().strftime('%H:%M:%S')

class Pesquisa:
    def __init__(self):
        self.perguntas = []
        self.respostas = []

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def realizar_pesquisa(self):
        print("Bem-vindo à nossa pesquisa!")

        idade = input("Qual é a sua idade? (Digite 00 para sair) ")

        if idade == '00':
            print('Obrigado por participar da pesquisa!')
            return

        genero = input('Qual é o seu gênero? (M/F/NB) ').upper()

        if genero not in ['M', 'F', 'NB']:
            print('Gênero inválido. Digite M, F ou NB.')
            return

        respostas = []

        for pergunta in self.perguntas:
            print(pergunta.texto)
            for i, opcao in enumerate(pergunta.opcoes, 1):
                print(f"{i}. {opcao}")
            resposta = input(f'Escolha uma opção (1-{len(pergunta.opcoes)}): ')
            if resposta.isdigit():
                resposta = int(resposta)
                if 1 <= resposta <= len(pergunta.opcoes):
                    respostas.append(resposta)
                else:
                    print('Resposta inválida. Escolha uma opção válida.')
            else:
                print('Resposta inválida. Digite um número.')

        if len(respostas) == len(self.perguntas):
            resposta = Resposta(idade, genero, respostas)
            self.respostas.append(resposta)
            print('Resposta registrada com sucesso!')
        else:
            print('Resposta não registrada devido a respostas inválidas.')

    def salvar_respostas(self, arquivo):
        with open(arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ['idade', 'genero'] + [f'pergunta_{i}' for i in range(1, len(self.perguntas) + 1)] + ['data', 'hora']
            writer.writerow(header)
            for resposta in self.respostas:
                # Usando strip() para remover espaços em branco do início e do final dos valores
                writer.writerow([resposta.idade.strip(), resposta.genero.strip()] + [str(r).strip() for r in resposta.respostas] + [resposta.data.strip(), resposta.hora.strip()])
            print(f"Respostas salvas no arquivo {arquivo}")

    def salvar_respostas(self, arquivo):
        with open(arquivo, mode='a', newline='') as file:  # Mude 'w' para 'a' para modo de anexação
            writer = csv.writer(file)
            # Verifique se o arquivo já existe para evitar escrever o cabeçalho repetidamente
            if file.tell() == 0:
                header = ['idade', 'genero'] + [f'pergunta_{i}' for i in range(1, len(self.perguntas) + 1)] + ['data', 'hora']
                writer.writerow(header)
            for resposta in self.respostas:
                # Usando strip() para remover espaços em branco do início e do final dos valores
                writer.writerow([resposta.idade.strip(), resposta.genero.strip()] + [str(r).strip() for r in resposta.respostas] + [resposta.data.strip(), resposta.hora.strip()])
            print(f"Respostas salvas no arquivo {arquivo}")

def main():
    pesquisa = Pesquisa()
    pergunta1 = Pergunta("Você tem acesso à internet?", ["S", "N", "NS"])
    pergunta2 = Pergunta("Você usa a internet para ter acesso às informações ou como meio de pesquisa?", ["S", "N", "NS"])
    pergunta3 = Pergunta("Você confia nas informações fornecidas?", ["S", "N", "NS"])
    pergunta4 = Pergunta("Você usa a internet para lazer?", ["S", "N", "NS"])

    pesquisa.adicionar_pergunta(pergunta1)
    pesquisa.adicionar_pergunta(pergunta2)
    pesquisa.adicionar_pergunta(pergunta3)
    pesquisa.adicionar_pergunta(pergunta4)

    while True:
        pesquisa.realizar_pesquisa()
        arquivo = 'pesquisa.csv'
        pesquisa.salvar_respostas(arquivo)  # Salvar as respostas a cada iteração
        if input("Deseja encerrar a pesquisa? (Digite 's' para sair) ").lower() == 's':
            break

if __name__ == "__main__":
    main()
