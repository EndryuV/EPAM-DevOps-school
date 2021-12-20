import psycopg2
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
    row = cursor.fetchone()
    info = []
    while row is not None:
        info.append(row)        
        row = cursor.fetchone()        
finally:
    conn.close()
contents = """<table class="table">
	<thead>
		<tr>
            <th>magazines_id</th>
            <th>article_type_id</th>
            <th>author_id</th>
        </tr>
    </thead>
    <tbody>
    """
contents2 = """</tbody>
</table>
<style type="text/css">
.table {
	width: 100%;
	margin-bottom: 20px;
	border: 15px solid #F2F8F8;
	border-top: 5px solid #F2F8F8;
	border-collapse: collapse; 
}
.table th {
	font-weight: bold;
	padding: 5px;
	background: #F2F8F8;
	border: none;
	border-bottom: 5px solid #F2F8F8;
}
.table td {
	padding: 5px;
	border: none;
	border-bottom: 5px solid #F2F8F8;
}
</style>"""
with open('/usr/share/nginx/html/index2.html', 'w') as news:
    news.write(contents)
    for tup in info:
        news.write("<tr>")
        news.write("\n")
        for x in tup:
            text = "<td><center>"+str(x)+"</center></td>"+"\n"
            news.write(text)
        news.write("</tr>")
        news.write("\n")
    news.write(contents2)
