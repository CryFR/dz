import csv


def to_csv(file_name, lst_tpl):
    try:

        with open(file_name, 'w') as csv_file:
            csv_file.write('name,address,age\n')
            writer = csv.writer(csv_file)
            for line in lst_tpl:
                writer.writerow(line)
    except Exception as err:
        print("!!!!Error!!!!\n", err)


a = [("Георгрий", "Невский Проспект", "21"),
     ("Иван", "пр. Ветеранов", "21"),
     ]

to_csv('create_csv_from_list.csv', a)
