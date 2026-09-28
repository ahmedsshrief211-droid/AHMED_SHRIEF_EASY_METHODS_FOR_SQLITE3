import sqlite3

class database:
    def __init__(self,db="parking.db"):
        self.db=sqlite3.connect(db)
        self.cr=self.db.cursor()

    def new_table(self,table_name,columns):# new_table("users","fname,lname,gender")
        query=f"create table if not exists {table_name} ({columns} )"
        self.cr.execute(query)
        self.db.commit()

    def insert(self,table_name,columns,values):
        query=f"insert into {table_name}({columns}) values({values})"
        self.cr.execute(query)
        self.db.commit()

    def fetch_one(self,column,table):
        query=f"select {column} from {table}"
        self.cr.execute(query)
        return self.cr.fetchone()

    def fetch_all(self,column,table):
        query=f"select {column} from {table}"
        self.cr.execute(query)
        return self.cr.fetchall()

    def fetch_all_where(self,column,table,cell,value):
            query=f"select {column} from {table} where {cell}='{value}'"
            self.cr.execute(query)
            return self.cr.fetchall()
    
    def fetch_where(self,column,table,cell,value):
        query=f"select {column} from {table} where {cell}='{value}' "
        self.cr.execute(query)
        return self.cr.fetchone()

    def update(self,column,table,updated_value,key,key_value):
        query=f"update {table} set {column}={updated_value} where {key}='{key_value}' "
        self.cr.execute(query)
        self.db.commit()

    def delete(self,table,column,value):
        query=f"delete from {table} where {column} = {value}"
        self.cr.execute(query)
        self.db.commit()
    
db=database()
db.new_table("users_info",
                """user_id integer primary key autoincrement,
                user_name text not null,
                Email text not null,
                national_id integer not null,
                phone_number text not null,
                password text not null""")

db.new_table("car",
                """car_id integer primary key autoincrement,
                user_id integer foreign key,
                brand text not null,
                model text not null,
                year text not null,
                plate_number text not null
                """)

db.new_table("parking_spaces",
                """space_id integer primary key autoincrement,
                space_number text unique not null,
                section text not null, 
                status text not null
                """)

db.new_table("reservations",
                """reservation_id integer primary key autoincrement,
                car_id integer foreign key,
                space_id integer foreign key,
                reservation_time text not null,
                entry_time text not null,
                exit_time text,
                reservation_status text not null
                """)


db.new_table("parking_sessions",
                """session_id integer primary key autoincrement,
                car_id integer foreign key,
                space_id integer foreign key,
                reservation_id integer foreign key,
                entry_time text not null,
                exit_time text,
                cost real
                """)

db.new_table("payments",
                """payment_id integer primary key autoincrement,
                session_id integer foreign key,
                amount real,
                payment_method text not null,
                payment_status text not null
                """)