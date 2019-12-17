# photo_html_blank.py
def get_html_from_dir_photo(mydir, filename='file_photo'):
    '''
    Функция генерирует html-файл, содержащий изображения,
    находящиеся в указанной директории mydir.
    '''
    from os import listdir
    filename += '.html'
    try:

        with open(filename, encoding='utf-8', mode='w') as new_file:

            new_file.write("""
<html>
    <head>
        <meta charset='utf-8'>
        <title>Фотогалерея</title>
    </head>
    <body>
""")

            for img in listdir('./photo'):
                new_file.write(f"       <p><img src='./photo/{img}' width='500' height='255' alt='Картинка'></p>\n")

            new_file.write(
f"""
    </body>
</html>""")
        
    except Exception as e:
        print(e)        
    else:
        print("Файл создан!")

if __name__ == '__main__':
    get_html_from_dir_photo('photo')  

    
