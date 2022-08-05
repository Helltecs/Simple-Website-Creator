def create_html(title, headline, content):
    try:
        with open(content, mode="r", encoding="UTF-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        pass

    with open("index.html", mode="w", encoding="UTF-8") as file:
        file.write(
                    '<!DOCTYPE html>\n\n'
                    '<html lang="en">\n'
                    '<head>\n'
                    '<meta charset="utf-8" />\n'
                    f'<title>{title}</title>\n'
                    '</head>\n'
                    '<body>\n'
                    f'<h1>{headline}</h1>\n'
                    f'<p>{content}</p>\n'
                    '</body>\n'
                    '</html>\n'
                    '\n'
                    )
        file.close()
