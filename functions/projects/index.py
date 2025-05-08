from utils.handler import handler_path
from resources.network import cineflyVpcConfigs


getProjectByProjectCode = {  
  'handler': f'{handler_path(__dirname)}/projects.defaultHandler',
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
