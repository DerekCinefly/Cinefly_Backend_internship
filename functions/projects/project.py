from aws_lambda import APIGatewayProxyEventV2
from dal.project import projectByProjectCode
from model.transport import jsonApiResponse, LegacyServerResponse
from utils.handler import CineflyHttpError, promiseHandler


# Checks whether a project exists by project code.

async def getProjectByProjectCode(event: APIGatewayProxyEventV2) -> dict:
    code = event.get('queryStringParameters', {}).get('code')

    if code is None:
        raise CineflyHttpError(400, 'Missing query param [code].')

    project = await projectByProjectCode(code)

    if project is None:
        raise CineflyHttpError(404, f'Project with code [{code}] does not exist.')

    return jsonApiResponse(True, [
        {
            'level': 'Info',
            'message': f'Found project by code [{code}].'
        }
    ])

defaultHandler = promiseHandler(LegacyServerResponse(getProjectByProjectCode))
