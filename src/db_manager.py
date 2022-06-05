#  Copyright (c) 2022/6/4 By Alireza Soltani Jazi

import file_handler as fh
import db_handler as dbh

if __name__ == "__main__":
	# Connect to the MySQL
	db = dbh.MySQLConnector(host='localhost', username='root', password='', database='test_db')
	connector = db.connect_to_mysql()
	db_action = dbh.DatabaseHandler(connector)

	# Create new database
	# db_action.create_database(new_database_name='test_db')

	# Display all databases
	db_action.display_all_databases()

	# Create new table
	# columns = \
	# 	'(id INT AUTO_INCREMENT PRIMARY KEY,tweet_id int, date VARCHAR(255), text LONGTEXT, ' \
	# 	'code_one VARCHAR(255), code_two VARCHAR(255))'
	# db_action.create_table("my_table_8", columns)

	# Display all tables
	db_action.display_all_tables()

	# Insert row(s) in a table with a file
	# fh = fh.FileHandler(src_file=r'../resource/file_1.csv')
	# file_values = fh.read_csv_file()
	# columns = '(tweet_id, date, text, code_one, code_two)'
	# db_action.insert_data(table_name='my_table_8', values=file_values, columns=columns)

	# Select data of a table
	db_action.select_table(table_name='my_table_8', limit=1, offset=0)
