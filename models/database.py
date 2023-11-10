import mysql.connector

#ESTA CLASSE DE CONSULTAS ESTÁ EM DESENVOLVIMENTO, PODE NÃO TER TODOS OS TRATAMENTOS DE ERROS NECESSÁRIOS PARA RETORNAR AS DEVIDAS MENSAGENS PARA IDENTIFICAR OS ERROS

class Database:
    def __init__(self, host, user, password, database, messages=False) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.messages = messages
        self.results = []
        self.info = {
            "status": "",
            "connection": "",
            "query": "",
            "affected_rows": "",
            "errors": "",
            "has_changed": ""
        }
        

    def executeQuery(self, query):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                self.cursor.execute(query)
                self.results = self.cursor.fetchall()
                self.info['affected_rows'] = self.cursor.rowcount
                self.info['query'] = query
                self.info['connection'] = str(self.conn)
                self.info['status'] = "success"
                self.info['errors'] = None
                self.info['has_changed'] = "not"
                if self.messages == True:
                    print(self.info)
                return self.results

            else:
                self.info['affected_rows'] = self.cursor.rowcount
                self.info['query'] = query
                self.info['connection'] = str(self.conn)
                self.info['status'] = "error"
                self.info['errors'] = "Connection not active"

                if self.messages:
                    print(self.info)
                    
                return None

        except Exception as e:
            if self.messages:
                self.info['status'] = "error"
                self.info['errors'] = str(e)
                print(self.info)
            return None


    def executeNonQuery(self, query):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                self.cursor.execute(query)
                self.info['affected_rows'] = self.cursor.rowcount
                self.info['query'] = query
                self.info['connection'] = str(self.conn)
                self.info['status'] = "success"
                self.info['errors'] = None
                self.info['has_changed'] = "yes"
                self.conn.commit()
                if self.messages == True:
                    print(self.info)


            else:
                self.info['affected_rows'] = self.cursor.rowcount
                self.info['query'] = query
                self.info['connection'] = str(self.conn)
                self.info['status'] = "error"
                self.info['errors'] = "Connection not active"

                if self.messages:
                    print(self.info)
                    
                return None

        except Exception as e:
            if self.messages:
                self.info['status'] = "error"
                self.info['errors'] = str(e)
                print(self.info)
            return None
        


    def closeConnection(self):
        if self.conn.is_connected():
            self.conn.close()

