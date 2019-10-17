class DataBase:
    def consultar():
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="uejn_servER8",
          database="uejn_afigestion"
        )

        return mydb.cursor()