with open('temper.stat', 'r') as file:
    lines = [float(x) for x in [line.strip() for line in file]]
print(f"Максимальное значение: {max(lines)}\nМинимальное значение: {min(lines)}\nСредняя температура: {sum(lines) / len(lines)}\nКол-во уникальных температур: {len(set(lines))}")
