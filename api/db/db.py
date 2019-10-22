import mysql.connector

cnx = mysql.connector.connect(
    host="db-server-evergreen-luis.mysql.database.azure.com",
    port=3306,
    user="evergreenadmin@db-server-evergreen-luis",
    password="Susy0926",
    database="evergreen",
)