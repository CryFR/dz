s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
result = [i for i in s.split() if not i.startswith('м')]
print(' '.join(map(str, result)))
