
def get_html(text, img, filename = 'file_poem'):
    '''
    Функция для генерации html-документа.
    text: файл с текстом
    img: файл с изображением
    '''
    import urllib.request
    from my_url import url_open
    filename += '.html'
    try:
        with open(filename, encoding='utf-8', mode='w') as new_file:

            new_file.write("""
<html>
    <head>
        <meta charset='utf-8'>
        <title>Стихи</title>
    </head>
    <body>""")

            for line in url_open(text):
                new_file.write(f"{line}<br>")



            new_file.write(
f"""
  <p><img src="{img}" alt="Тютчев"></p>
    </body>
</html>""")

    except Exception as error:
        print(error)
    else:
        print("Файл создан!")

if __name__ == "__main__":
    file_ = "http://dfedorov.spb.ru/python/files/tutchev.txt"
    pic = "http://dfedorov.spb.ru/python/files/tutchev.jpg"
    get_html(file_, pic)

