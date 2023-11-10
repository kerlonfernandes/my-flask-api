from app.config import *
from app.models.database import *
import json

class ReturnData(Database):
    def __init__(self) -> None:
        super().__init__(DATABASE_HOST, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE, True)
        
    def getUsers(self):
        # Inicialize as listas para armazenar os dados
        self.user_ids = []
        self.emails = []
        self.names = []
        self.addresses = []
        self.telefones = []
        self.ufs = []
        self.passwords = []
        self.user_keys = []
        self.recover_key = []
        self.accessed_at = []
        self.date_access = []

        self.executeQuery("SELECT * FROM usuarios")

        for res in self.results:
            self.user_ids.append(res[0])
            self.emails.append(res[1])
            self.names.append(res[2])
            self.addresses.append(res[3])
            self.telefones.append(res[4])
            self.ufs.append(res[5])
            self.passwords.append(res[6])
            self.user_keys.append(res[7])
            self.recover_key.append(res[8])
            self.accessed_at.append(res[9])
            self.date_access.append(res[10])

        user_dicts = []

        for i in range(len(self.names)):
            user_data = {
                "user_id": self.user_ids[i],
                "email": self.emails[i],
                "nome": self.names[i],
                "endereco": self.addresses[i],
                "telefone": self.telefones[i],
                "uf": self.ufs[i],
                "password": self.passwords[i],
                "user_key": self.user_keys[i],
                "recover_key": self.recover_key[i],
                "accessed_at": str(self.accessed_at[i]),
                "date_access": str(self.date_access[i])
            }
            user_dicts.append(user_data)

        user_data = user_dicts
        return user_data



    def getEspecificUser(self, id):
        user_dicts = []
        if(id): 
            try:
                self.executeQuery(f"SELECT * FROM usuarios WHERE id = {id}")
                for res in self.results:
                    user_data = {
                        "user_id": res[0],
                        "email": res[1],
                        "nome": res[2],
                        "endereco": res[3],
                        "telefone": res[4],
                        "uf": res[5],
                        "password": res[6],
                        "user_key": res[7],
                        "recover_key": res[8],
                        "accessed_at": str(res[9]),
                        "date_access": str(res[10])
                    }
                    user_dicts.append(user_data)
                    return user_dicts
            except Exception as e:
                print("Ocorreu um erro! -> ", e)
    
    def deleteUser(self, id: int):
        if(id):
            self.executeNonQuery(f"DELETE FROM usuarios WHERE id = {id}")
            return self.info