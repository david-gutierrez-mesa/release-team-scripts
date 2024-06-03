class FileName:
    Parent_task_file_name = "PARENT_TASK.txt"


class Filter:
    QA_Analysis_for_release = ('project = "PUBLIC - Liferay Product Delivery" AND summary ~ "{release_version} QA '
                               'Analysis"')


class Roles:
    Release_lead = 'david.gutierrez'


class URLs:
    Liferay_repo_URL = 'https://github.com/liferay/liferay-portal-ee/'
