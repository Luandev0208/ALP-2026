import random
import time

n = random.randint(2, 10)

print("Prepare-se...")
time.sleep(n)

print("AGORA!")

tempo0 = time.time()

input()

tempo1 = time.time()

print(f"Você levou {tempo1 - tempo0:.3f} segundos.")
