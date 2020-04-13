
import os
import zipfile
import json

from werkzeug.datastructures import FileStorage


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def test_login(test_client):
    """
    GIVEN POST /api/v1/update/offline
    WHEN a zip file is attached
    THEN status shoud be 200
    """
    token_request = test_client.post(
        'api/v1/user/login/',
        data=json.dumps({'username':'example', 'password':'123456'}),
        headers={'Content-Type': 'application/json'}
    )
#    token = 'JWT '+ token_request.get_json()['access_token']
#    file_data_location = os.path.join("tests/assets/f.zip")
#
#    my_file = FileStorage(
#        stream=open(file_data_location, "rb"),
#        filename="f.zip",
#        content_type="application/zip",
#    )
#
#    response = test_client.post(
#        "/api/v1/update/offline",
#        data={
#        "update_file": my_file,
#        },
#        headers={
#            'Content-Type': "multipart/form-data",
#            'Authorization': token
#        }
#
#    )
#    assert response.status_code == 200
#
#    """
#    WHEN update_file is not sent in request
#    THEN status is 400
#    """
#    my_file = FileStorage(
#        stream=open(file_data_location, "rb"),
#        filename="f.zip",
#        content_type="application/zip",
#    )
#    response = test_client.post(
#        "/api/v1/update/offline",
#        data={
#        "wrong_field": my_file,
#        },
#        headers={
#            'Content-Type': "multipart/form-data",
#            'Authorization': token
#        }
#    )
#    assert response.status_code == 400
#    """
#    WHEN file format is not zip
#    THEN status is 400
#    """
#    my_file = FileStorage(
#        stream=open(file_data_location, "rb"),
#        filename="f.jpg",
#        content_type="application/zip",
#    )
#    response = test_client.post(
#        "/api/v1/update/offline",
#        data={
#        "wrong_field": my_file,
#        },
#        headers={
#            'Content-Type': "multipart/form-data",
#            'Authorization': token
#        }
#    )
#    assert response.status == '400 BAD REQUEST'
#
