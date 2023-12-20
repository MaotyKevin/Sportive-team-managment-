import sys , os , sqlite3
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from bd_model import Bd_manage

class Ligue_model:
    def __init__(self):
        self.databaseConnect = Bd_manage()

    def Ligue_list(self):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT * FROM Ligue
        """
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()

        return data
    
    def Ligue_delete(self , ligue_id):
        conn , cursor = self.databaseConnect.bd_connect()
        delete_query = """
            DELETE FROM Ligue WHERE ligue_id = ?
        """
        cursor.execute(delete_query , (ligue_id,))
        conn.commit()
        conn.close()

    def Ligue_add(self , ligue_nom):
        conn , cursor = self.databaseConnect.bd_connect()
        insert_query = """
            INSERT INTO Ligue (ligue_nom) VALUES (?)
        """
        cursor.execute(insert_query , (ligue_nom,))
        conn.commit()
        conn.close()

    def Ligue_update(self , ligue_id , ligue_nom):
        try:
            conn , cursor = self.databaseConnect.bd_connect()
            update_query = "UPDATE Ligue SET ligue_nom = ? WHERE ligue_id = ?"
            cursor.execute(update_query, (ligue_nom, ligue_id))
            conn.commit()
            return True 
        
        except sqlite3.Error as e:
            print(f"Error updating Ligue: {e}")
            return False
    
if __name__ == '__main__':
    ligue = Ligue_model()
    id = 4
    nom = "Ligue bresiliennes"
    ligue.Ligue_update(id , nom)
        