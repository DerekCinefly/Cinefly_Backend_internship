from utils.handler import handlerPath
from resources.network import cineflyVpcConfigs


getProjectByProjectCode = {  
  'handler': f'{handlerPath(__dirname)}/projects.defaultHandler',
  'vpc' : cineflyVpcConfigs,
  'events': [
    {
      'httpApi': {
        'method': 'GET',
        'path' : '/v1/projects',
      },
    },
  ],
}

lambdaFunctions = {
    'getProjectByProjectCode': getProjectByProjectCode,
}
