class Personagem:
    def __init__(self, nome, vida, ataque):
        self._nome = nome
        self._vida = vida
        self._ataque = ataque
        
    def atacar(self, alvo):
        if self._vida > 0:
            print(f"{self._nome} atacou {alvo._nome}!")
            alvo.tomar_dano(self._ataque)
        else:
            print(f"{self._nome} está derrotado e não pode atacar!")     
    
    def tomar_dano(self, dano):
        self._vida -= dano
        
        if self._vida < 0:
            self._vida = 0
            print(f"{self._nome} foi derrotado!")
            
        print(f"{self._nome} recebeu {dano} de dano!")
        print(f"Vida atual de {self._nome}: {self._vida}")
        print("\n ================================\n")
    
    def mostrar_status(self):
        print(f"Nome: {self._nome}")
        print(f"Vida: {self._vida}")
        print(f"Ataque: {self._ataque}")
        print("\n================================\n")
    
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 150, 20)

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 120, 40)

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 100, 50)

guerreiro = Guerreiro("Thorin")

mago = Mago("Merlin")

arqueiro = Arqueiro("Legolas")

print("===== INÍCIO DA BATALHA =====\n")

while (
    guerreiro._vida > 0 or
    mago._vida > 0 or
    arqueiro._vida > 0
):
    
    if guerreiro._vida > 0:
        guerreiro.atacar(mago)

    if mago._vida > 0:
        mago.atacar(arqueiro)

    if arqueiro._vida > 0:
        arqueiro.atacar(guerreiro)

    
    vivos = 0

    if guerreiro._vida > 0:
        vivos += 1

    if mago._vida > 0:
        vivos += 1

    if arqueiro._vida > 0:
        vivos += 1

    
    if vivos == 1:
        break

print("===== FIM DA BATALHA =====\n")

guerreiro.mostrar_status()
mago.mostrar_status()
arqueiro.mostrar_status()