from utils.handler import promiseHandler, withCurrentUser
from aws_lambda import APIGatewayProxyEventV2
from services.elasticsearch import searchScripts, scriptIndexName, searchListings, listingIndexName, userIndexName, searchUsers, assetIndexName, searchAssets, reusableAssetIndexName, searchReusableAssets
from model.cineflyuser import CineflyUserProfile


#  Searches the indexed scripts/listings from the Elasticsearch based on the provided index name in path.
 
#  Admin can see all data, normal Customer can only search their own data.

async def search(event: APIGatewayProxyEventV2, current_user_profile: CineflyUserProfile) -> dict:
    authorizer = event["requestContext"].get("authorizer", {}).get("lambda", {})
    user_groups = authorizer.get("cognito:groups", [])
    search_index = event.get("pathParameters", {}).get("searchIndex")
    query_params = event.get("queryStringParameters", {})

    is_admin = "Admin" in user_groups

    if search_index == scriptIndexName:
        search_result = await searchScripts({
            "isAdmin": is_admin,
            "queryParams": query_params,
            "currentUserProfile": current_user_profile,
        })
        return {"result": search_result}

    elif search_index == listingIndexName:
        search_result = await searchListings({
            "queryParams": query_params
        })
        return {"result": search_result}

    elif search_index == userIndexName:
        search_result = await searchUsers({
            "queryParams": query_params
        })
        return {"result": search_result}

    elif search_index == assetIndexName:
        search_result = await searchAssets({
            "queryParams": query_params,
            "currentUserProfile": current_user_profile
        })
        return {"result": search_result}

    elif search_index == reusableAssetIndexName:
        search_result = await searchReusableAssets({
            "queryParams": query_params
        })
        return {"result": search_result}

    return {"result": None}

defaultHandler = promiseHandler(withCurrentUser(search))