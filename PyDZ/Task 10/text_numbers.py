def numeration(first_file, updated_file):
    with open(first_file) as file:
        data = "".join([x for x in file.readlines()])
        content = data.splitlines()
        with open(updated_file, 'w') as upd_file:
            for i in range(len(content)):
                content[i] = "%s " % (i + 1) + content[i]
            data = "\n".join([x for x in content])
            upd_file.write(data)


numeration('text.txt', 'update_text.txt')
