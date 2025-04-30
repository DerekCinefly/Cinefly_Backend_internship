from utils.handler import handlerPath
from resources.network import cineflyVpcConfigs

httpEventProps = {
  'path': '/search/{searchIndex}',
  'authorizer': {
    'name': 'cognitoAuthorizer',
  },
}

search = {
    'handler': f'{handlerPath(__dirname)}/projects.defaultHandler',
    'vpc': cineflyVpcConfigs,
    'environment': {
        'CINEFLY_CUSTOMER_POOL_ID': { 'Ref': 'CineflyCustomerPool' },
    },
    'events': [
    {
      'httpApi': {
        'method': 'GET',
        'path': '/search/{searchIndex}',
        'authorizer': {
            'name': 'cognitoAuthorizer',
            },
      },
    },
  ],
}


lambdaFunctions = {
    'search': search,
}