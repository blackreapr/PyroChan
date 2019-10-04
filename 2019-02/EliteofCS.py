"""
This code parses an XML file (that was exported from a PDF which our university published)
to output a list of students, sorted by their grades.
"""
from xml.etree.ElementTree import parse
from operator import itemgetter


def scrape_xml(document):
    admis = []

    for tr in document.iterfind('page/table/tr'):
        tds = list(tr)
        if len(tds) is 40 and str(tds[39].text) == "Admis(e)":
            last = str(tds[1].text)
            first = str(tds[2].text)
            fullname = normalize_name(first, last)
            moy = str(tds[37].text).replace(",", ".")
            student = [fullname, moy]
            admis.append(student)

    return admis


def normalize_name(first_name, last_name):
    """
    The names in our data are stored all in uppercase, so we "normalize" it
    Examples:
    normalize_name("NIKOLA", "TESLA") == "Nikola Tesla"
    normalize_name("FELIX ARVID ULF", "KJELLBERG") == "Felix Arvid Ulf Kjellberg"
    """
    name_parts = " ".join([first_name, last_name]).split(" ")
    full_name = " ".join(map(capitalize, name_parts))
    return full_name


def capitalize(word):
    return word[0].upper() + word[1:].lower()


def sort_students(unsorted_students):
    return sorted(unsorted_students, key=itemgetter(1), reverse=True)


def convert_html(majors):
    contents = []
    for student in majors:
        div = "<tr><td>#{i}</td><td>{fullname}</td><td><i>{moy}</i></td></tr>".format(
           i=len(contents)+1, fullname=student[0], moy=student[1])
        contents.append(div)
    contents = "\n".join(contents)

    html_code = """<!DOCTYPE html>
    <html>
    <head>
        <title>Elite of NTIC — L2 (2018-2019)</title>
    </head>
    <body>
         <h1 align="center">Elite of NTIC — L2 (2018-2019)</h1>
         <content>
         <table>
         {content}
         </table>
         </content>
    </body>
    </html>""".format(content=contents)
    return html_code


def export_html(html):
    with open("EliteOfCs.html", "wt") as ntic:
        ntic.write(html)
    ntic.close()


def main():
    doc = parse('Grades.xml')
    students = scrape_xml(doc)
    elites = sort_students(students)
    html_content = convert_html(elites)
    export_html(html_content)


if __name__ == '__main__':
    main()