from pydriller import Repository
import csv
from tqdm import tqdm
import sys

project = sys.argv[1]
print(project)
csv_path = './pydrillerData/' + project + '.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    fields = ['hash', 'msg', 'files', 'lines', 'committer_date', 'modified_files', 'merge', 'branches']
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writerow(
        {'hash': 'hash', 'msg': 'msg', 'files': 'files', 'lines': 'lines', 'committer_date': 'committer_date',
         'modified_files': 'modified_file', 'merge': 'merge', 'branches': 'branches'})

    repo_url = 'https://github.com/apache/' + project
    for commit in tqdm(Repository(repo_url).traverse_commits()):
        modified_file = []
        branches = []
        for file in commit.modified_files:
            modified_file.append([file.filename, file.change_type.name, file.old_path, file.new_path])
        for branch in commit.branches:
            branches.append(branch)
        writer.writerow({'hash': commit.hash, 'msg': commit.msg, 'files': commit.files, 'lines': commit.lines,
                         'committer_date': commit.committer_date, 'modified_files': modified_file,
                         'merge': commit.merge, 'branches': branches})
