from typing import Dict
from dal import user_profile_by_id
import json

class CineflyHttpError(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code


def create_error_message(error: CineflyHttpError):
    return {
        'statusCode': error.status_code or 500,
        'body': json.dumps(
            json_api_response(None, [{'level': 'Error', 'message': str(error)}])
        ),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def create_response_message(value, status_code = 200):
    return {
        'statusCode': status_code,
        'body': json.dumps(value),
        'headers': {
            'Content-Type': 'application/json'
        }
    }


async def map_promise(promise, status_code = 200):
    try:
        response = await promise
        return create_response_message(response, status_code)
    except CineflyHttpError as error:
        print(json.dumps(error.__dict__, indent=2))
        return create_error_message(error)
    
    
def promise_handler(lambda_function, status_code = 200):
    async def handler(event, context):
        return await map_promise(lambda_function(event, context), status_code)
    return handler


def json_api_response(result, messages) -> Dict:
    return {
        "result": result,
        "messages": messages
    }

def extract_user_id_from_cognito(lambda_data):
    if not lambda_data:
        return None

    cognito_username = str(lambda_data.get("cognito:username")) if "cognito:username" in lambda_data else None

    identities = lambda_data.get("identities")
    federated_user_id = None

    if isinstance(identities, list) and len(identities) > 0:
        federated_user_id = identities[0].get("userId")

    return federated_user_id or cognito_username


def with_current_user(lambda_action):
    async def handler(event):
        authorizer = event.get("requestContext", {}).get("authorizer", {})
        lambda_auth = authorizer.get("lambda", {})

        user_id_in_profile = extract_user_id_from_cognito(lambda_auth)

        if not user_id_in_profile:
            raise CineflyHttpError(401, "Not authenticated")

        user_profile = await user_profile_by_id(user_id_in_profile)

        if not user_profile:
            raise CineflyHttpError(401, "Not authenticated")

        return await lambda_action(event, user_profile)

    return handler


