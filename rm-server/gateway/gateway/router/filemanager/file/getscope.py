from flask import request

from gateway.app import app
from gateway.http_client import filemanager_http_client
from gateway.utils.handle_api import  (
    get_client_username, handle_request_response
)

@app.route('/file/getscope', methods=['GET'])
@handle_request_response
@get_client_username
def file_getscope(client_username: str):
    args=request.args.to_dict()
    status_code, resp_body = filemanager_http_client.get(
        'file/getscope', client_username, params=args
    )
    return status_code, resp_body