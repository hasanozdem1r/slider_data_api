from flask import request, jsonify


# CALL PARAMETERS RELATED GETTER METHODS

def get_application_id() -> str:
    """
    This method is used to retrieve application id from form input values.
    :return: <str> application name

    """
    app_id: str = str(request.args.get('app-id'))
    return app_id


def get_application_name() -> str:
    """
    This method is used to retrieve application name from form input values.
    :return: <str> application name
    """
    app_name: str = str(request.args.get('app-name'))
    return app_name


def get_add_image_params():
    app_id = request.args.get('app-id')
    image_path = request.args.get('image-path')
    return app_id, image_path


# DB OR QUERY RELATED ISSUE RESPONSE METHODS

def prepare_db_related_exception_500(error):
    """
    This method used to prepare json message if database related issue caught
    :param error: error message
    :return: <json> response
    """
    # response preparation
    query_data = {'Message': f'Process error caught : {str(error)}. Please control database related issues'}
    response = jsonify(query_data)
    # 500 Internal Server Error
    response.status_code = 500
    return response


def prepare_query_related_error_400():
    """
    This method used to prepare json message if query params related issue caught
    :return: <json> response
    """
    # response preparation
    query_data = {'Message': f'Process error caught. Please control query parameters'}
    response = jsonify(query_data)
    # 400 Bad Request
    response.status_code = 400
    return response

# SUCCESSFUL RESPONSE METHODS

def prepare_response_200(query_data):
    response = jsonify(query_data)
    response.status_code = 200
    return response

def prepare_response_201(informative_msg):
    response = jsonify(informative_msg)
    # HTTP 201 -> Created
    response.status_code = 201
    return response