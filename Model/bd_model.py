import sqlite3

class Bd_manage:
    def __init__(self):
        self.database_name = 'Data\Foot_data.sqlite'
    
    def bd_connect(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        return conn , cursor