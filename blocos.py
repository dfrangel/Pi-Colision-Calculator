class Bloco:
    def __init__(self, peso, vel, x):
        self.peso = peso
        self.vel = vel
        self.x = x
        self.tam = 80

    def update(self, largura):
        bateu_na_parede = False
        if (self.x + self.tam + self.vel > largura):
            self.x = largura - self.tam
            self.vel *= -1
            bateu_na_parede = True
        self.x += self.vel
        
        return bateu_na_parede


def colide_blocos(b1, b2):
    m1 = b1.peso
    m2 = b2.peso
    v1 = b1.vel
    v2 = b2.vel

    # Fórmula de colisão elástica perfeitamente aplicada
    v1f = (((m1 - m2) / (m1 + m2)) * v1) + (((2 * m2) / (m1 + m2)) * v2)
    v2f = (((m2 - m1) / (m2 + m1)) * v2) + (((2 * m1) / (m2 + m1)) * v1)

    b1.vel = v1f
    b2.vel = v2f