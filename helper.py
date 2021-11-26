from flask import request


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