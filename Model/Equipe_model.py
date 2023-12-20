import sys , os , sqlite3
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from bd_model import Bd_manage

class Equipe_model:
    def __init__(self):
        self.databaseConnect = Bd_manage()

    def ligue_nom(self , ligue_id):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT ligue_nom from Ligue WHERE ligue_id = ?
        """
        cursor.execute(query , (ligue_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        else:
            return None

    def Equipe_list(self):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT team_id , team_name , ligue_id FROM Equipe
        """
        cursor.execute(query)
        data = cursor.fetchall()

        results = []
        for datas in data :
            team_id , team_name , ligue_id  = datas 
            ligue_nom =self.ligue_nom(ligue_id)
            results.append((team_id , team_name, ligue_nom))


        conn.close()

        return results
    
    def Titulaires_dans_equipe(self , team_id):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT T.titulaire_nom
            FROM EquipeTitulaire et
            LEFT JOIN Titulaire T ON et.titulaire_id = T.titulaire_id
            WHERE et.team_id = ?
        """

        cursor.execute(query , (team_id,))
        data = cursor.fetchall()
        conn.close()
        return data 
    
    def Nombre_tiitulaires_dans_equipe(self , team_id):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT
                COUNT(et.titulaire_id)
            FROM
                Equipe e
            JOIN EquipeTitulaire et ON e.team_id = et.team_id
            WHERE
                e.team_id = ?
        """

        cursor.execute(query , (team_id,))
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Equipe_add(self , team_name , logo , ligue_id):
        conn , cursor = self.databaseConnect.bd_connect()
        insert_query = """
            INSERT INTO Equipe (team_name ,logo, ligue_id ) VALUES (? , ? , ?)
        """
        cursor.execute(insert_query , (team_name , logo , ligue_id,))
        conn.commit()
        conn.close()

        
    

    
if __name__ == '__main__':
    Equipe = Equipe_model()
    teamID = 1
    datas = Equipe.Nombre_tiitulaires_dans_equipe(teamID)
    print(datas)