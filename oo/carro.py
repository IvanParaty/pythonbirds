
NORTE = "Norte"
LESTE = "Leste"
SUL = 'Sul'
OESTE = 'Oeste'

class Carro():
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

class Direcao():

    rotacao_a_direita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}
    def __init__(self):
        self.valor = NORTE

    def valor(self):
        pass

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda[self.valor]


class Motor():
    def __init__(self):
        self.velocidade = 0

    def velocidade(self):
        return self.velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)

    pass



tec=1
while tec != 'f':
    tec = input('entrada')
    if tec == 'w':
        Carro.acelerar
    if tec == 's':
        Carro.frear
    print(Carro.calcular_velocidade)
