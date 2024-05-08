#!/usr/bin/env python
import os
import sys

from getLpsFromLocalRepo import get_lps_from_local_repo
from utils.liferay_utils.jira_utils.jira_helpers import get_all_issues
from utils.liferay_utils.jira_utils.jira_liferay import get_jira_connection


def fill_qa_analysis_jira_task(jira, repo_path, start_hash, end_hash, release_version=''):
    lpd_ticket = ''
    if release_version:
        print("Get task from " + release_version)
        jql = 'project = "PUBLIC - Liferay Product Delivery" AND summary ~ "' + release_version + ' QA Analysis"'
        qa_analysis_tasks = get_all_issues(jira, jql, ["key"])
        if len(qa_analysis_tasks) == 1:
            parent_task = qa_analysis_tasks[0].key
            get_lps_from_local_repo(jira, repo_path, start_hash, end_hash, release_version, parent_task)
            os.environ["PARENT_TASK"] = parent_task


if __name__ == '__main__':
    path = ''
    first_hash = ''
    final_hash = ''
    try:
        path = sys.argv[1]
    except IndexError:
        print("Please provide a local path to the report")
        exit()

    try:
        first_hash = sys.argv[2]
    except IndexError:
        print("Please provide a hash to start")
        exit()

    try:
        final_hash = sys.argv[3]
    except IndexError:
        print("Please provide a hash to finish")
        exit()

    try:
        release = sys.argv[4]
    except IndexError:
        release = ""
    jira_connection = get_jira_connection()
    fill_qa_analysis_jira_task(jira_connection, path, first_hash, final_hash, release)
