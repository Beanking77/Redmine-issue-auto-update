#!/usr/bin/env python
import json,sys,os

if __name__ == "__main__":
#    try:
        redmine_api_key={KEY}
        redmine_project_issue_url={issue_url}
        issue_status_id={status_id}
        assign_to_id={assignee_id}
        obj=json.load(sys.stdin)
        for i in range(obj['total_count']):
            issue_id=obj['issues'][i]['id']
            version_id=sys.argv[1]
            os.system('curl -L -k -v -H \"Content-Type: application/json\" -X PUT -d \'{ \"issue\": { \"status_id\": \"%s\", \"assigned_to_id\": \"%s\", \"fixed_version_id\": \"%s\"} }\' -H \"X-Redmine-API-Key: %s\" %s/%s.json' % (issue_status_id, assign_to_id, version_id, redmine_api_key, redmine_project_issue_url, issue_id))
