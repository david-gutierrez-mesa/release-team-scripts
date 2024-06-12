# release-team-scripts

## Run getLpsFromLocalRepo script
### Prerequisites
* Python 3 installed
* pip installed

### Steps
1. Update your local liferay repo
2. Checkout the branch you want to use
3. From project root directory, install requirements
    ```
    pip install -r ./requirements.txt
    ```
4. Change script permissions
    ```
    chmod 755 getLpsFromLocalRepo.py
    ```
5. Run scrip
    ```
    ./getLpsFromLocalRepo.py ${PATH_TO_PORTAL} ${START_HASH} ${END_HASH} ${NEXT_VERSION} ${PARENT_TASK}
    ```

_**Note:** The first time you use the script it will ask you for your Jira user and token. For more information on Jira tokens refer to https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/_   

### Parameters
* _PATH_TO_PORTAL_: Mandatory. Local path to your liferay repo. Remember that it should be up-to-date 
* _START_HASH_: Mandatory. Hash to start the issues search. Be sure it exists on the branch you are on for liferay repo
* _END_HASH_: Mandatory. HEAD can be used. Hash to finish the issues search. Be sure it exists on the branch you are on for liferay repo
* _NEXT_VERSION_: Mandatory. You must set the next version in order to add it into tickets name.
* _PARENT_TASK_: Optional. Key of the Jira issue we want to create the subtask in. If it is set subtask are crated using NEXT_VERSION on the name. If it is not set, no sub-task is created.

### Example
```
    ./getLpsFromLocalRepo.py /path/to/portal/liferay-portal-ee 3003e37ca17273ce74c3f0213865b7b64ec7ad1f d6f2ba88aac686f9b64a7152082c5cb1d72065f7 2024.Q2.0 LPD-26288
```