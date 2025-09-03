from db import DataBase

testDB = DataBase(dbName="test.db")
testDB.create_table(name='shop',\
	columns=[['product', 'varchar(100)', ''], ['price', 'int', '']])
print(testDB.get_data(table='shop'))
testDB.insert_data(table='shop', columns=['product', 'price'],\
	values=[['orange', 5], ['gloves', 20]])
print(testDB.get_data(table='shop'))
testDB.update_data(table='shop', columns=['price'], values=[3], condition='product=="orange"')
print(testDB.get_data(table='shop'))
testDB.delete_data(table='shop', condition='product=="gloves"')
print(testDB.get_data(table='shop'))
testDB.delete_data(table='shop')
print(testDB.get_data(table='shop'))