from app import app
from configparser import ConfigParser
from flaskext.mysql import MySQL # version Flask-MySQL==1.5.2

# create a MySQL class instance
mysql_obj=MySQL()

# create a ConfigParser class instance
conf_obj=ConfigParser()

# read all information from config file
conf_obj.read('database_config.ini')
user_info=conf_obj["USERINFO"]
db_info=conf_obj["DB_CONFIG"]


# To configure access to your MySQL database server by using these settings
app.config['MYSQL_DATABASE_USER'] =str(user_info['user'])
app.config['MYSQL_DATABASE_PASSWORD'] = str(user_info['password'])
app.config['MYSQL_DATABASE_DB'] = str(db_info['database'])
app.config['MYSQL_DATABASE_HOST'] =str(db_info['host'])

# connect mysql_object with app
mysql_obj.init_app(app)

def create_record(sql_query:str,data:tuple):
    try:
        connection = mysql_obj.connect()
        db_cursor = connection.cursor()
        db_cursor.execute(sql_query, data)
        connection.commit()
        return db_cursor,connection
    except Exception as error:
        print(f'Connection failed error message: {error}')


def connect_db():
    connection = mysql_obj.connect()
    db_cursor = connection.cursor()
    return connection, db_cursor


def close_connection(connection, db_cursor):
    """
    This method used to close SQL server connection
    """
    db_cursor.close()
    connection.close()


def fetch_data(sql_query:str,data:tuple):
    connection = mysql_obj.connect()
    db_cursor = connection.cursor()
    db_cursor.execute(sql_query, data)
    query_data=db_cursor.fetchall()
    return db_cursor,connection,query_data



# this section has been created testing connection independently
if __name__=='__main__':
    try:
        mysql_obj.connect()
        connection = mysql_obj.connect()
        #create_record("INSERT INTO apps_case_study.users(username,email,password) VALUES(%s,%s,%s);",('apps1','apps1@gmail.com','apps1'))
        print('Connection Successful')
    except Exception as error:
        print(f'Connection failed error message: {error}')