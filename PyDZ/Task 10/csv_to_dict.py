def read_csv(file_name):
    '''return list of dictionaries from csv file

    [{"key1":value,"key2":value,...},...]
    '''
    try:
        with open(file_name, encoding="cp1251", mode='r') as csvfile:
            result = []
            keys = [x.strip() for x in csvfile.readline().split(',')]
            while True:
                entry = [x.strip() for x in csvfile.readline().split(',')]
                if entry == ['']:
                    break
                result.append(dict(zip(keys, entry)))
        return result
    except Exception as err:
        print("!!!!Error!!!!\n", err)


if __name__ == "__main__":
    print(read_csv("newfile.csv"))
