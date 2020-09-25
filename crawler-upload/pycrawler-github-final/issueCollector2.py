'''
Exports Issues from a specified repository to a CSV file

Uses basic authentication (Github username + password) to retrieve Issues
from a repository that username has access to. Supports Github API v3.
'''
import csv
import requests
import re
import os
import commands
import datetime


GITHUB_USER = 'xxx'
GITHUB_PASSWORD = 'xxx'
AUTH = (GITHUB_USER, GITHUB_PASSWORD)

csvfile = './issues_body.csv'
csvout = csv.writer(open(csvfile, 'ab'))
fail_repo = './not_response.txt'

crash_issue = 0 # the number of issues with 'crash' or 'exception'

def more_pages(r, repo,pkg):
  if 'link' in r.headers:
    pages = dict(
      [(rel[6:-1], url[url.index('<') + 1:-1]) for url, rel in
       [link.split(';') for link in
        r.headers['link'].split(',')]])
    # print "***"
    print pages
    while 'last' in pages and 'next' in pages:
      print pages['next']
      r = requests.get(pages['next'], auth=AUTH)
      write_issues(r, repo, csvout, pkg)
      if pages['next'] == pages['last']:
        break
      pages = dict(
        [(rel[6:-1], url[url.index('<') + 1:-1]) for url, rel in
         [link.split(';') for link in
          r.headers['link'].split(',')]])

def write_issues(response,repo,csvout,pkg):
  global crash_issue
  print crash_issue
  '''output a list of issues to csv'''
  if not response.status_code == 200:
    #print repo
    #raise Exception(response.status_code)
    not_response = open(fail_repo,'a')
    not_response.write(repo+'\n')
    return
  for issue in response.json():
    if issue['body']:
        if 'crash' in issue['body'].lower()  or 'exception' in issue['body'].lower() \
                or 'crash' in issue['title'].lower() or 'exception' in issue['title'].lower():
            crash_issue = crash_issue + 1
            csvout.writerow([pkg, repo, issue['number'], issue['html_url'],issue['created_at'], issue['closed_at'],'1'])
def main():
  repo = open('./repos_github.txt','r')
  line = repo.readline()
  i =  1
  while line:
    REPO = line.strip('\n').split(';')[1]# REPO format is username/repo
    pkg = line.strip('\n').split(';')[0]
    print i, REPO
    i = i + 1

    ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues?state=all' % REPO
    r = requests.get(ISSUES_FOR_REPO_URL, auth=AUTH)
    write_issues(r, REPO, csvout,pkg)
    #more pages? examine the 'link' header returned
    more_pages(r, REPO,pkg)
    line = repo.readline()
if __name__ == '__main__':
  csvout.writerow(('pkg','repo', 'ID', 'issue_url', 'Created At', 'Closed At', 'crashes Description'))
  main()
