from faker import Faker
import random

fake = Faker('pt_BR')

def criar_persona():
    persona = {
        "nome": fake.name(),
        "idade": random.randint(18, 70),
        "cidade": fake.city()
    }
    return persona

persona = criar_persona()
print(persona)
