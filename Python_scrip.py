import psycopg2

#from prettytable import from_db_cursor
from config import host, database, user, password

try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    cursor = conn.cursor()
    cursor.execute('select magazines.name, article_types.type, author.author from magazines, article_types, author, articles where articles.magazines_id = magazines.id and articles.article_types_id = article_types.id and articles.author_id = author.id;')
    #print(cursor.rowcount)
    row = cursor.fetchone()
    articles = []

    while row is not None:
        articles.append(row)
        print(row)
        row = cursor.fetchone()
    #print(articles)
    conn.commit() 
finally:
    conn.close()
contents = """<html>
<head>
        <meta charset="UTF-8">
        <title>My table</title>
</head>
<style>table, th, td {border:1px solid black;}</style>
<body>
    <h2 align="center">Articles</h2>
    <table style="width: 100%;"
        <tr>
            <th>magazines_id</th>
            <th>article_type_id</th>
            <th>author_id</th>
        </tr>"""

contents2 = """</table>
</body>
</html>"""

with open('index_.html', 'w') as news:
    news.write(contents)
    for tup in articles:
        news.write("<tr>")
        news.write("\n")
        for x in tup:
            text = "<th><center>"+str(x)+"</center></th>"+"\n"
            news.write(text)
        news.write("</tr>")
        news.write("\n")
    news.write(contents2)
