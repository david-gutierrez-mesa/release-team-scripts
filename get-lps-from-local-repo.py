#!/usr/bin/env python
import sys
import git


def main(repo_path, start_hash, end_hash):
    liferay_portal_ee_repo = git.Repo(repo_path)

    print("Retrieving git info ...")

    of_interest = liferay_portal_ee_repo.git.log(start_hash + ".." + end_hash, "--pretty=format:%H")

    individual_commit_hashes = of_interest.split('\n')
    lps_list = []
    revered_list = []

    for commit_hash in individual_commit_hashes:
        message = liferay_portal_ee_repo.commit(commit_hash).message
        lps = message.split(' ')[0].split('\n')[0]
        if message.lower().find('revert') != -1:
            revered_list.append('https://github.com/liferay/liferay-portal-ee/commit/' + commit_hash)
        elif (lps not in lps_list) and (lps.startswith('LPS-')):
            lps_list.append(lps)

    print(" List of LPS:")
    print(*lps_list, sep="\n")
    print("\n\n List of reverted LPS:")
    print(*revered_list, sep="\n")


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
