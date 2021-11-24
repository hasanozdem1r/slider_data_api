from app import app
from flask import Flask, jsonify, request,abort
from model import mysql_obj,fetch_data,close_connection


# This method will be used to retrieve all applications name for drag and drop
# GET request to ->  http://localhost:80/apps_api/v1/apps
@app.route('/apps-api/v1/apps') # collection
def retrieve_app_names():
    try:
        #SELECT app_name FROM apps_case_study.apps;
        sql_query="SELECT app_id,app_name FROM apps_case_study.apps"
        query_data=()
        db_cursor,connection,query_data=fetch_data(sql_query,query_data)
        close_connection(connection,db_cursor)
        response=jsonify(query_data)
        response.status_code=200
        print(type(response))
        return response
    except Exception as error:
        return f'{error}'


if __name__ == '__main__':
    # Root http://localhost:80
    app.run(host='localhost', port=80)
