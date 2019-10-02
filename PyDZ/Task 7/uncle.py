s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
splitted_rythm = s.split()
result = [i for i in splitted_rythm if not i.startswith('м')]
print(result)
