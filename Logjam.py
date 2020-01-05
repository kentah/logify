import config
import database

x = database.Database()
x.create_database()
#x.destroy_database()
x.create_tables()
x.populate_dummy_data()
