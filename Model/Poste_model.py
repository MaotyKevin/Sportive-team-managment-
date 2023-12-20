import sys , os , sqlite3
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from bd_model import Bd_manage

class Poste_model:
    def __init__(self):
        self.databaseConnect = Bd_manage()

    def Poste_list(self):
        conn  , cursor= self.databaseConnect.bd_connect()
        query = """
            SELECT * FROM Poste
        """
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()

        return data
    
    def Poste_delete(self , poste_id):
        conn , cursor = self.databaseConnect.bd_connect()
        delete_query = """
            DELETE FROM Poste WHERE poste_id = ?
        """
        cursor.execute(delete_query , (poste_id,))
        conn.commit()
        conn.close()

    def Poste_add(self , poste_nom):
        conn , cursor = self.databaseConnect.bd_connect()
        insert_query = """
            INSERT INTO Poste (poste_nom) VALUES (?)
        """
        cursor.execute(insert_query , (poste_nom,))
        conn.commit()
        conn.close()

    def Poste_update(self , poste_id , poste_nom):
        try:
            conn , cursor = self.databaseConnect.bd_connect()
            update_query = "UPDATE Poste SET poste_nom = ? WHERE poste_id = ?"
            cursor.execute(update_query, (poste_nom, poste_id))
            conn.commit()
            return True 
        
        except sqlite3.Error as e:
            print(f"Error updating Poste: {e}")
            return False
    
if __name__ == '__main__':
    poste = Poste_model()
    
    coach  = "Coach"
    poste.Poste_add(coach)
        