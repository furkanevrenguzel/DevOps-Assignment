from files import jira, bitbucket


jira_projects = jira.getProjects()
bitbucket_projects = bitbucket.getProjects()

updated_projects_count = 0

for jira_project in jira_projects:
    p_name = jira_project["name"]
    p_key = jira_project["key"]
    p_desc = jira_project["description"]

    if bitbucket.isPorjectExist(p_key, p_name, bitbucket_projects["values"]) == False:
        bitbucket.addProject(p_key, p_name, p_desc)
        updated_projects_count += 1

results = """ 

 """.format(len(jira_projects), updated_projects_count)

print(results)
