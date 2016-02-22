# Redmine issue auto update 
##### Use redmine api to auto update redmine issues
## Usage
#### 1. Create versoin id in redmine:

```
=====================================
Give:
$bigVER.$VER="1.1.1.0001"
$release_date=`date --date="now" +"%Y-%m-%d"`
$project_id="test123"
Return:
$version_id=1234 {Version id in redmine}
=====================================

curl -L --silent -k -v -H "Content-Type: application/json" -X POST -d "{ \"version\": { \"name\": \"$bigVER.$VER\", \"status\": \"open\", \"sharing\": \"none\", \"due_date\": \"$release_date\", \"description\": \"\"} }" -H "X-Redmine-API-Key: {Put your redmine api key here}" {Put your redmine url}/projects/$project_id/versions.json |python -c 'import json,sys;obj=json.load(sys.stdin);print obj["version"]["id"]'

```

#### 2. Update redmine issue:
Redmine issue filter id number:

Create a issue filter in redmine and get filter id number.

{You redmine url}/projects/{redmine project}/issues?query_id={filter id}

```

=====================================
Give:
$project_id="{redmine project}"
$query_id={filter id}
$version_id=1234 (Get from step 1.)
=====================================
curl -L --silent -k -X GET "{Put your redmine url}/projects/$project_id/issues.json?query_id=$query_id&limit=100&key={Put your redmine api key here}" | ../update-issue.py $version_id

```
