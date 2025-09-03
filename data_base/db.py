import sqlite3

class DataBase:
	def __init__(self, dbName):
		self.dbName = dbName

	def get_data(self, table, columns='*', condition='', col_group_by='', order_cond='', desc=False):
		processed_columns = ','.join(columns)
		command = f"SELECT {processed_columns} FROM {table}"
		command += f"\nWHERE {condition}" if condition else ""
		command += f"\nGROUP BY {col_group_by}" if col_group_by else ""
		command += f"\nORDER BY {order_cond}" if order_cond else ""
		command += f" DESC" if desc else ""
		command += ";"
		#print(command)
		return self.complete_command(command, ret=1)

	def create_table(self, name, columns):
		"""
			columns - [[name1, dataType1, additional_settings1], [...]]
		"""
		processed_columns = ','.join([f"{column[0]} {column[1].upper()} {column[2]}" for column in columns]) 
		command = f"CREATE TABLE IF NOT EXISTS {name} (\
				id INTEGER PRIMARY KEY,\
				{processed_columns}\
			);"
		self.complete_command(command)


	def insert_data(self, table, columns, values):
		""" 
			values - [[val1.1, val1.2], [val2.1, val2.2] ...]
			columns - [col1, col2, ...]
		"""
		processed_columns = ','.join(columns)
		processed_values = []
		for val in values:
			processed_values.append([f'"{i}"' if isinstance(i, str) else str(i) for i in val])
		processed_values = [f"({','.join(val)})" for val in processed_values]
		processed_values = ','.join(processed_values)
		#print(processed_values)
		command = f"INSERT INTO {table} ({processed_columns}) VALUES {processed_values};"
		#print(command)
		self.complete_command(command)

	def update_data(self, table, columns, values, condition=''):
		""" 
			columns - [col1, col2, ...]
			values - [val1, val2, ...]
		"""
		processed_text = ",".join([f"{column}={value}" for column, value in zip(columns, values)])
		command = f"UPDATE {table} SET {processed_text}"
		command += f" WHERE {condition}" if condition else ""
		command += ";"
		self.complete_command(command)

	def delete_table(self, table):
		command = f"DROP TABLE {table};"
		self.complete_command(command)

	def delete_data(self, table, condition=""):
		command = f"DELETE FROM {table}"
		command += f" WHERE {condition}" if condition else ""
		command += ";"
		self.complete_command(command)

	@staticmethod
	def save_db(conn):
		conn.commit()

	def complete_command(self, command, ret=0):
		conn = sqlite3.connect(self.dbName)
		cur = conn.cursor()
		cur.execute(command)
		res = cur.execute(command).fetchall() if ret else None
		if not ret: self.save_db(conn)
		conn.close()
		return res