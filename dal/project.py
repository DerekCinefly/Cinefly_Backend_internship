from db import execDbQuery

async def project_by_project_code(code: str): 
    query = {
    'text': 'SELECT id, code, owner_user_id, title, description, project_type, last_updated, date_created FROM project WHERE code=$1 AND record_status=$2 LIMIT 1',
    'values': [code, 'Active'],
  }
    projects_result = await execDbQuery(query)
    
    return projects_result.rows[0]

async def project_by_user_id(id: int):
  query = {
    'text': 'SELECT id, code, owner_user_id, title, description, project_type, last_updated, date_created FROM project WHERE owner_user_id=$1 AND record_status=$2',
    'values': [str(id), 'Active']
  }
  projects_result = await execDbQuery(query)
  return projects_result.rows