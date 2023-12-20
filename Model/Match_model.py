import sys , os , sqlite3
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from bd_model import Bd_manage

class Match_model:
    def __init__(self):
        self.databaseConnect = Bd_manage()

    def adversaire_nom(self , adversaire_id):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT team_name from Equipe WHERE team_id = ?
        """
        cursor.execute(query , (adversaire_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        else:
            return None


    def Match_list(self):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT m.match_adversaire , m.match_date , m.match_lieu , e.team_name
            FROM Match m
            LEFT JOIN EquipeMatch em ON m.match_id = em.match_id
            LEFT JOIN Equipe e ON em.team_id = e.team_id
            
        """
        cursor.execute(query)
        data = cursor.fetchall()
        results = []
        for datas in data :
            adversaire_id , date_match , lieu_match , equipe_match = datas 
            adversaire_nom=self.adversaire_nom(adversaire_id)
            results.append((adversaire_nom, date_match, lieu_match, equipe_match))

        conn.close()
        return results

        


    def Match_add(self , match_adversaire , match_date , match_lieu):
        conn , cursor = self.databaseConnect.bd_connect()
        insert_query = """
            INSERT INTO Match (match_adversaire ,match_date, match_lieu ) VALUES (? , ? , ?)
        """
        cursor.execute(insert_query , (match_adversaire , match_date , match_lieu,))
        conn.commit()
        conn.close()

    def match_de_equipe(self , team_id):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT m.match_adversaire , m.match_date , m.match_lieu
            FROM EquipeMatch em
            LEFT JOIN Match m ON em.match_id = m.match_id
            WHERE em.team_id = ?
        """

        cursor.execute(query , (team_id,))
        data = cursor.fetchall()
        results = []
        for datas in data :
            adversaire_id , date_match , lieu_match = datas 
            adversaire_nom=self.adversaire_nom(adversaire_id)
            results.append((adversaire_nom, date_match, lieu_match))
        conn.close()
        return results 
    
    def Nombre_match_une_equipe(self , team_id):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT
                COUNT(em.match_id)
            FROM
                Equipe e
            JOIN EquipeMatch em ON e.team_id = em.team_id
            WHERE
                e.team_id = ?
        """

        cursor.execute(query , (team_id,))
        data = cursor.fetchall()
        conn.close()
        return data
    
if __name__ == '__main__':
    matchs = Match_model()
    teamID = 1
    

    results = matchs.Nombre_match_une_equipe(teamID)

    print(results)
        