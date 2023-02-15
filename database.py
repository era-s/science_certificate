import sqlite3


class DataBase:
    def __init__(self):
        # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('earth_middle.db')
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS EarthMiddle (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    unit INTEGER,
                    difficulty INTEGER, 
                    try_count INTEGER,
                    wrong_count INTEGER,
                    last_solve INTEGER,
                    tag TEXT,
                    body TEXT,
                    choices TEXT,
                    answer INTEGER,
                    solution TEXT
                    )""")

    def add_database(self, unit, difficulty, tag, body, choices, solution):
        self.cursor.execute("""INSERT INTO problems (unit, difficulty, tag, body, choices, solution) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, (unit, difficulty, tag, body, choices, solution))
        self.conn.commit()

    def get_problems_by_unit(self, unit):
        self.cursor.execute("""
                SELECT * FROM EarthMiddle WHERE unit=?
                """, (unit,))
        return self.cursor.fetchall()

    def get_problems_by_difficulty(self, difficulty):
        self.cursor.execute("""
                SELECT * FROM EarthScience WHERE difficulty=?
                """, (difficulty,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
