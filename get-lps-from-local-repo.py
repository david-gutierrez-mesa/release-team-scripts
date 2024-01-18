#!/usr/bin/env python
import sys
import git


def main(repo_path, start_hash, end_hash):
    liferay_portal_ee_repo = git.Repo(repo_path)

    print("Retrieving git info ...")

    of_interest = liferay_portal_ee_repo.git.log(start_hash + ".." + end_hash, "--pretty=format:%H")

    individual_commit_hashes = of_interest.split('\n')
    lps_list = []

    for commit_hash in individual_commit_hashes:
        message = liferay_portal_ee_repo.commit(commit_hash).message.split(' ')[0].split('\n')[0]
        if (message not in lps_list) and (message.startswith('LPS-')):
            lps_list.append(message)

    print(*lps_list, sep="\n")


if __name__ == '__main__':
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
        final_hash = "HEAD"

    main(path, first_hash, final_hash)
