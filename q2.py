import datetime

class Clinica:
    def __init__(self, endereco):
        self._nome = "Pata Certa"
        self.__endereco = endereco
        self.__atend = []
        self.__tabela_preco = {
    "1": {
        "categoria": "Consulta",
        "servico": "Consulta Geral de Rotina",
        "preco": 150.00,
        "tempo_estimado_min": 30
    },
    "2": {
        "categoria": "Consulta",
        "servico": "Consulta de Emergência",
        "preco": 280.00,
        "tempo_estimado_min": 45
    },
    "3": {
        "categoria": "Vacinação",
        "servico": "Vacina Múltipla V10",
        "preco": 130.00,
        "tempo_estimado_min": 15
    },
    "4": {
        "categoria": "Vacinação",
        "servico": "Vacina Antirrábica",
        "preco": 90.00,
        "tempo_estimado_min": 15
    },
    "5": {
        "categoria": "Exame",
        "servico": "Hemograma Completo",
        "preco": 85.00,
        "tempo_estimado_min": 720
    },
    "6": {
        "categoria": "Exame",
        "servico": "Ultrassonografia Abdominal",
        "preco": 220.00,
        "tempo_estimado_min": 40
    },
    "7": {
        "categoria": "Procedimento",
        "servico": "Castração Canino",
        "preco": 450.00,
        "tempo_estimado_min": 120
    },
    "8": {
        "categoria": "Procedimento",
        "servico": "Castração Felino",
        "preco": 350.00,
        "tempo_estimado_min": 90
    },
    "9": {
        "categoria": "Estética",
        "servico": "Banho e Tosa",
        "preco": 80.00,
        "tempo_estimado_min": 60
    }
}

    def nova_consulta(self, servico, pet):
        data = datetime.date.today()

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def tabela_preco(self):
        return self.__tabela_preco
        
        

class Pet:
    def __init__(self,nome, especie, raca, peso, idade):
        self.__info = []
        self.__info.append(nome)
        self.__info.append(especie)
        self.__info.append(raca)
        
        if peso <= 0 or idade <= 0:
            raise ValueError("digite valores acima de de 0")
        
        else:
            self.__info.append(peso)
            self.__info.append(idade)

        @property
        def info (self):
            return {'nome': info[0],
                    'espécie': info[1],
                    'raça': info[2]
                    }
        
        def levar_clinica(self, servico,motivo, agendar = None):
            if agendar == None:
                clinica.nova_consulta(servico, motivo, agendar)
            else:

                clinica.nova_consulta(servico, motivo)

clinica = Clinica("Rua dos Bobos, 0 - Bairro Imaginário - São Paulo - SP - CEP: 00000-000")
print(clinica.endereco)
#batata