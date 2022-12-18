import math

ângulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, seno, ângulo, cosseno, ângulo, tangente))
