from user_interface import name_view
from user_interface import num_view
from user_interface import text_view

def new_create(info, device = 1):
    n, nu, t = info
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Name: {} c</p>\n'\
        .format(style, n)
    html += '    <p {}>Num: {} m/s</p>\n'\
        .format(style, nu)
    html += '    <p {}>Text: {} mmHg</p>\n'\
        .format(style, t)
    html += '  </body>\n</html>'
    
    with open('new_index.html', 'w') as page:
        page.write(html)

    return info
