def create_html(lang, title, css=False, headline="", content=""):
    if lang == "" or lang is None:
        raise ValueError("You have to assign a language")

    if title == "" or lang is None:
        raise ValueError("You have to assign a title")

    try:
        with open(content, mode="r", encoding="UTF-8") as file:
            content = file.read()
            file.close()
    except FileNotFoundError:
        pass

    with open("index.html", mode="w", encoding="UTF-8") as file:
        file.write(
            '<!DOCTYPE html>\n\n'
            f'<html lang="{lang}">\n'
            '<head>\n'
            '<meta charset="utf-8" />\n'
            f'<title>{title}</title>\n'
        )
        file.mode = "a"
        if css:
            file.write('<link rel="stylesheet" href=index.css>\n')

        file.write(
            '</head>\n'
            '<body>\n'
        )

        if headline != "" and not None:
            file.write(f'<h1>{headline}</h1>\n')

        if content != "" and not None:
            file.write(f'<p>{content}</p>\n')

        file.write(
            '</body>\n'
            '</html>\n'
        )
        file.close()


def create_css(headline_align="", headline_color=""):
    with open("index.css", mode="w", encoding="UTF-8") as file:
        file.write("")
        file.mode = "a"
        temp = css_section("h1", {"text-align: ": headline_align, "color: ": headline_color})
        file.write(f"{temp}\n\n")
        temp = css_section("p", {})
        file.write(f"{temp}\n\n")
        file.close()


def css_section(section, arguments: {}):
    return_string = f"{section} " + "{\n"
    for i in arguments:
        return_string += i + arguments[i] + ";\n"
    return return_string + "}"


def cut_lang(lang: str):
    return lang[-2::]
