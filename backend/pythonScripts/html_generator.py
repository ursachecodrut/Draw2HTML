def div_generator(divs):
    return "".join(f"""<div class="div{index}"></div>"""
                   for index, div in enumerate(divs))


def p_generator(paragraphs):
    return "".join(f"""<p class="p{index}"></p>"""
                   for index, p in enumerate(paragraphs))


def img_generator(images):
    return "".join(f"""<img class="img{index}" />"""
                   for index, img in enumerate(images))


def div_style_generator(divs):
    return "".join(
        f""".div{index} {{
    position: absolute;
    left: {div[0]}px;
    top: {div[1]}px;
    width: {div[2]}px;
    height: {div[3]}px;
    border: 3px solid blue;}}\n"""
        for index, div in enumerate(divs))


def p_style_generator(paragraphs):
    return "".join(
        f""".p{index} {{
    position: absolute;
    left: {p[0]}px;
    top: {p[1]}px;
    width: {p[2]}px;
    height: {p[3]}px;
    border: 3px solid green;}}\n"""
        for index, p in enumerate(paragraphs))


def img_style_generator(images):
    return "".join(
        f""".img{index} {{
    position: absolute;
    left: {img[0]}px;
    top: {img[1]}px;
    width: {img[2]}px;
    height: {img[3]}px;
    border: 3px solid red;}}\n"""
        for index, img in enumerate(images))


def generate_css_string(div_style, p_style, img_style):
    return f"""* {{
        margin: 0;
        padding: 0;
    }}

    {div_style}
    {p_style}
    {img_style}
    """


def generate_html_string(divs, paragraphs, images):
    div_tags = div_generator(divs)
    p_tags = p_generator(paragraphs)
    img_tags = img_generator(images)

    div_style = div_style_generator(divs)
    p_style = p_style_generator(paragraphs)
    img_style = img_style_generator(images)

    css = generate_css_string(div_style, p_style, img_style)

    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Draw2HTML</title>
        <style>
            {css}
        </style>
    </head>
    <body>
        {div_tags}
        {p_tags}
        {img_tags}
    </body>
    </html>\n
    """
