# flask related imports
from app import app
from flask import jsonify, request
# api params related helper methods
from helper import get_application_name, get_application_id, get_add_image_params
# database related imports
from model import fetch_data, close_connection, create_record
from datetime import datetime


# This method will be used to retrieve all applications name for drag and drop
# GET request to ->  http://localhost:80/apps_api/v1/apps OR http://localhost/apps-api/v1/apps
@app.route('/apps-api/v1/apps')  # collection
def retrieve_app_names():
    """
    This method will be used to retrieve all applications name for drag and drop
    :return: <json> Query answer
    """
    try:
        # query and data preparation
        sql_query = "SELECT app_name FROM apps_case_study.apps"
        query_data = ()
        # database crud operations
        db_cursor, connection, query_data = fetch_data(sql_query, query_data)
        close_connection(connection, db_cursor)
        response = jsonify(query_data)
        response.status_code = 200
        return response
    except Exception as error:
        return f'{error}'



# This method will be used to retrieve all images path for slider menu
# GET request to ->  http://localhost:80/apps-api/v1/images?app-id=1
# http://localhost/apps-api/v1/images?app-id=51
@app.route('/apps-api/v1/images')
def retrieve_images():
    """
    This method will be used to retrieve all images path via application id
    :return: <json> Query answer
    """
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


# TODO method documentation
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


# http://localhost:80//apps-api/v1/images/post?app-id=41?image-path=asda
@app.route('/apps-api/v1/images/post', methods=['POST'])
def add_image():
    """
    This method used to add new image to the database
    :return: result JSON
    """
    if request.method == 'POST':
        try:
            # Are the parameters valid?
            if 'app-id' in request.args and 'image-path' in request.args:
                app_id, image_path = get_add_image_params()
                current_date = datetime.now()
                # query and data preparation to check app_id is already in db or not
                sql_query = "SELECT COUNT(app_id) FROM apps_case_study.images WHERE app_id=%s and image_path=%s;"
                query_data: tuple = (app_id, image_path,)
                # database crud operations
                db_cursor, connection, query_data = fetch_data(sql_query, query_data)
                close_connection(connection, db_cursor)
                query_data: int = int(query_data[0][0])
                # Is this given photo in database?
                # The data is not in database
                if query_data == 0:
                    # query and data preparation
                    sql_query: str = "INSERT INTO apps_case_study.images (app_id,image_path,created_date,updated_date) \
                                VALUES(%s,%s,%s,%s);"
                    current_date = datetime.now()
                    query_data: tuple = (app_id, image_path, str(current_date.strftime('%Y-%m-%d %H:%M:%S')),
                                         str(current_date.strftime('%Y-%m-%d %H:%M:%S')),)
                    # database crud operations
                    db_cursor, connection = create_record(sql_query, query_data)
                    close_connection(connection, db_cursor)
                    # prepare informative json reply
                    informative_msg: dict = {'message': "The image successfully added to database"}
                    response = jsonify(informative_msg)
                    # HTTP 201 -> Created
                    response.status_code = 201
                    return response

                # The data is in database
                else:
                    # query and data preparation to update image path in database
                    sql_query = "UPDATE apps_case_study.images SET image_path = %s, updated_date=%s  WHERE app_id = %s;"
                    query_data: tuple = (image_path, str(current_date.strftime('%Y-%m-%d %H:%M:%S')), app_id)
                    # database crud operations
                    db_cursor, connection = create_record(sql_query, query_data)
                    close_connection(connection, db_cursor)
                    informative_msg: dict = {'message': "The image successfully updated to database"}
                    response = jsonify(informative_msg)
                    # HTTP 201 -> Created
                    response.status_code = 201
                    return response

            # Parameters are invalid
            else:
                return 'Parameters are not valid'
        except Exception as error:
            return f'{error}'


if __name__ == '__main__':
    # Root http://localhost:80
    app.run(host='localhost', port=80)
