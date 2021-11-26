from app import app
from flask import jsonify, request
from helper import get_application_name, get_application_id
from model import fetch_data, close_connection


#TODO method documentation
# This method will be used to retrieve all applications name for drag and drop
# GET request to ->  http://localhost:80/apps_api/v1/apps OR http://localhost/apps-api/v1/apps
@app.route('/apps-api/v1/apps')  # collection
def retrieve_app_names():
    try:
        # query and data preparation
        sql_query = "SELECT app_name FROM apps_case_study.apps"
        query_data = ()
        # database crud operations
        db_cursor, connection, query_data = fetch_data(sql_query, query_data)
        close_connection(connection, db_cursor)
        response = jsonify(query_data)
        response.status_code = 200
        print(query_data, type(response))
        return response
    except Exception as error:
        return f'{error}'

#TODO method documentation
# This method will be used to retrieve all images path for slider menu
# GET request to ->  http://localhost:80/apps-api/v1/images?app-id=1
# http://localhost/apps-api/v1/images?app-id=51
@app.route('/apps-api/v1/images')
def retrieve_images():
    # database operations managed well.
    # authentication or query parameters passed well
    # FIXME exception part can be better
    try:
        # FIXME create else situation things to do
        if 'app-id' in request.args:
            app_id = get_application_id()
            # query and data preparation
            sql_query = "SELECT image_id,image_path FROM apps_case_study.images WHERE app_id=%s"
            query_data = (app_id,)
            # database crud operations
            db_cursor, connection, query_data = fetch_data(sql_query, query_data)
            close_connection(connection, db_cursor)
            response = jsonify(query_data)
            response.status_code = 200
            return response
    # database related error.
    # authentication or query based reasons
    except Exception as error:
        return f'{error}'

#TODO method documentation
# http://localhost/apps-api/v1/apps/?app-name=appasdas
# http://localhost:80/apps-api/v1/apps/?app-name=Rolly Legs
@app.route('/apps-api/v1/apps/')
def retrieve_app_id():
    # database operations managed well.
    # authentication or query parameters passed well
    # FIXME exception part can be better
    try:
        # FIXME create else situation things to do
        if 'app-name' in request.args:
            app_name = get_application_name()
            # query and data preparation
            sql_query = "SELECT app_id FROM apps_case_study.apps where app_name=%s"
            query_data = (app_name,)
            # database crud operations
            db_cursor, connection, query_data = fetch_data(sql_query, query_data)
            close_connection(connection, db_cursor)
            response = jsonify(query_data)
            response.status_code = 200
            return response
    # database related error.
    # authentication or query based reasons
    except Exception as error:
        return f'{error}'


if __name__ == '__main__':
    # Root http://localhost:80
    app.run(host='localhost', port=80)
