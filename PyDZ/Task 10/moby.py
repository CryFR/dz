import string
with open('moby.txt', 'r') as file:
    lines = file.read().replace('\n', '')
    reg_lines = lines.upper()
    out_lines = "".join(x for x in reg_lines if x not in string.punctuation)
with open('moby_clean.txt', 'w') as f:
    f.write(out_lines.replace(" ", "\n"))
