from user_interface import name_view
from user_interface import num_view
from user_interface import text_view

def new_create(info, device = 1):
    n, nu, t = info
    # t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '    <name units = "1">{}</name>\n'\
        .format(t)
    xml += '    <num_view units = "2">{}</num_view>\n'\
        .format(nu)
    xml += '    <text units = "3">{}</text>\n'\
        .format(t)
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return info
