from typing import Dict
from aws_lambda import APIGatewayProxyEventV2
from model.transport import LegacyServerResponse
from dal.project import project_by_project_code
from utils.handler import CineflyHttpError, promise_handler, json_api_response


# Checks whether a project exists by project code.

async def get_project_by_project_code(event: APIGatewayProxyEventV2) -> Dict:
    code = event.get('queryStringParameters', {}).get('code')

    if code is None:
        raise CineflyHttpError(400, 'Missing query param [code].')

    project = await project_by_project_code(code)

    if project is None:
        raise CineflyHttpError(404, f'Project with code [{code}] does not exist.')

    return json_api_response(True, [
        {
            'level': 'Info',
            'message': f'Found project by code [{code}].'
        }
    ])

defaultHandler = promise_handler(LegacyServerResponse(get_project_by_project_code))
