high = 0
low = 0
avg = 0
unique = 0
with open('temper.stat', 'r') as file:
    lines = [float(x) for x in [line.strip() for line in file]]
high = max(lines)
low = min(lines)
avg = sum(lines) / len(lines)
unique = len(set(lines))

print(f" Максимальное значение: {high}\nМинимальное значение: {low}\nСредняя температура: {avg}\nКол-во уникальных температур: {unique}")
