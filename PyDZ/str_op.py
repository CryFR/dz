s = "У лукоморья 123 дуб зеленый 456"
if 'я' in s:
    print(s.index('я', 1))
print(s.count('у'))
if s.isdigit():
    print(s.upper())
if len(s) > 4:
    print(s.lower())
print(s.replace(s[0], 'О'))