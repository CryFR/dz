import string
with open('moby.txt', 'r') as file:
    with open('moby_clean.txt', 'w') as f:
        lines = file.read().replace('\n', ' ')
        reg_lines = lines.upper()
        rep_lines = reg_lines.replace("--", " ")
        out_lines = "".join(x for x in rep_lines if x not in string.punctuation)
        f.write(out_lines.replace(" ", "\n"))
