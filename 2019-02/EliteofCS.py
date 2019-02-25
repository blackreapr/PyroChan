"""
We all like to compare our grades with other and see if we are among top (Elites)
This script takes xml file(table) of all the student grades and sort it
And save the result in html file
"""
from xml.etree.ElementTree import parse
from operator import itemgetter


def scrape_xml(document):
    admis = []
    for tr in document.iterfind('page/table/tr'):
        tds = list(tr)
        if len(tds) is 25 and str(tds[24].text) == "Admis(e)":
            last = str(tds[0].text)
            first = str(tds[1].text)
            fullname = normalize_name(first, last)
            moy = str(tds[22].text).replace(",", ".")
            student = [fullname, moy]
            admis.append(student)
    return admis


def normalize_name(firstname, lastname):
    """
    The names in our data are stored all in uppercase, we only need the first letter to be upper
    Examples:
    normalize_name("NIKOLA", "TESLA") == "Nikola Tesla"
    normalize_name("FELIX ARVID ULF", "KJELLBERG") == "Felix Arvid Ulf Kjellberg"
    """
    name_parts = " ".join([firstname, lastname]).split(" ")
    fullnanme = " ".join(map(capitalize, name_parts))
    return fullnanme


def capitalize(word):
    return word[0].upper() + word[1:].lower()


def sort_students(unsorted_students):
    return sorted(unsorted_students, key=itemgetter(1), reverse=True)


def convert_html(majors):
    contents = []
    for student in majors:
        div = "<tr><td>#{i}</td> <td>{fullname}</td><td><i>{moy}</i></td></tr>".format(
           i=len(contents)+1, fullname=student[0], moy=student[1])
        contents.append(div)
    contents = "\n".join(contents)

    html_code = """<html>
    <head>
        <title>Elite of NTIC</title>
    </head>
    <body>
         <h1 align="center">Elite of NTIC</h1>
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