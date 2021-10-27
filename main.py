# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333

import sys
import requests
import re
import os
from bs4 import BeautifulSoup

username = os.environ["USERNAME"]
hw_index = int(re.findall(r'homework([0-9]+)', os.environ["ISSUE_TITLE"])[0])


def test(condition, message):
    print(("[ok] " if condition else "[wrong] ") + message)
    if not condition: sys.exit(-1)


def get_raw(url):
    return requests.get(url).text.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')


def hw1():
    soup = BeautifulSoup(requests.get('https://github.com/{}/hw-gitMergeAndRebase/commits/master-1'.format(username)).text, features='lxml')
    sha = [cc.get('value') for cc in soup.find_all("clipboard-copy") if cc.get('value')]
    test(len(sha) == 9, "commit_number=9")
    test(sha[1:] == [
        "07ad66a71ff56e2205ab495f1f871838ee5d09d2",
        "b0db239a6e6b8e2031fcd009237081bf3d6e1b31",
        "0a44654d64e16bfc24f96405dd8751307d87c59c",
        "1d21f4ccff3693b7646a913b69066ccbae611a17",
        "6ac0dad640dff27625f075c7bf3f7efb8240dec8",
        "4ed609c7e3969315580c47d78b3edb9b62d3386c",
        "3f211abfd8889f3d29d7e5ffad6315692f837386",
        "9b8530d8da65928ddabed2bb429f7c043b142267"
    ], "commit sha-1 check")
    A = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/master-1/A.c'.format(username))
    test('printf("A:agoodfeature");//A' in A, 'checking file A (want: \'printf("A: a good feature"); // A\')')
    B = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/master-1/B.c'.format(username))
    test('printf("B:agoodfeature");//B' in B, 'checking file B (want: \'printf("B: a good feature"); // B\')')
    C = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/master-1/C.c'.format(username))
    test('printf("C:agoodfeature");//C' in C, 'checking file C (want: \'printf("C: a good feature"); // C\')')


def hw2():
    soup = BeautifulSoup(requests.get('https://github.com/{}/hw-gitMergeAndRebase/commits/my-feature-2'.format(username)).text, features='lxml')
    sha = [cc.get('value') for cc in soup.find_all("clipboard-copy") if cc.get('value')]
    test(len(sha) == 8, "commit_number=8")
    test(sha[3:] == [
        "1d21f4ccff3693b7646a913b69066ccbae611a17",
        "6ac0dad640dff27625f075c7bf3f7efb8240dec8",
        "4ed609c7e3969315580c47d78b3edb9b62d3386c",
        "3f211abfd8889f3d29d7e5ffad6315692f837386",
        "9b8530d8da65928ddabed2bb429f7c043b142267"
    ], "commit sha-1 check")
    A = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/my-feature-2/A.c'.format(username))
    test('printf("A:agoodfeature");//A' in A, 'checking file A (want: \'printf("A: a good feature"); // A\')')
    B = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/my-feature-2/B.c'.format(username))
    test('printf("B:agoodfeature");//B' in B, 'checking file B (want: \'printf("B: a good feature"); // B\')')
    C = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/my-feature-2/C.c'.format(username))
    test('printf("C:agoodfeature");//C' in C, 'checking file C (want: \'printf("C: a good feature"); // C\')')


def hw3():
    soup = BeautifulSoup(requests.get('https://github.com/{}/hw-gitMergeAndRebase/commits/master-3'.format(username)).text, features='lxml')
    sha = [cc.get('value') for cc in soup.find_all("clipboard-copy") if cc.get('value')]
    test(len(sha) == 6, "commit_number=6")
    test(sha[1:] == [
        "1d21f4ccff3693b7646a913b69066ccbae611a17",
        "6ac0dad640dff27625f075c7bf3f7efb8240dec8",
        "4ed609c7e3969315580c47d78b3edb9b62d3386c",
        "3f211abfd8889f3d29d7e5ffad6315692f837386",
        "9b8530d8da65928ddabed2bb429f7c043b142267"
    ], "commit sha-1 check")
    A = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/master-3/A.c'.format(username))
    test('printf("A:agoodfeature");//A' in A, 'checking file A (want: \'printf("A: a good feature"); // A\')')
    B = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/master-3/B.c'.format(username))
    test('printf("B:agoodfeature");//B' in B, 'checking file B (want: \'printf("B: a good feature"); // B\')')
    C = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/master-3/C.c'.format(username))
    test('printf("C:agoodfeature");//C' in C, 'checking file C (want: \'printf("C: a good feature"); // C\')')


def hw4():
    soup = BeautifulSoup(requests.get('https://github.com/{}/hw-gitMergeAndRebase/commits/my-feature'.format(username)).text, features='lxml')
    sha = [cc.get('value') for cc in soup.find_all("clipboard-copy") if cc.get('value')]
    test(len(sha) == 4, "commit_number=4")
    test(sha[1:] == [
        "4ed609c7e3969315580c47d78b3edb9b62d3386c",
        "3f211abfd8889f3d29d7e5ffad6315692f837386",
        "9b8530d8da65928ddabed2bb429f7c043b142267"
    ], "commit sha-1 check")
    A = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/my-feature/A.c'.format(username))
    test('printf("A:agoodfeature");//A' in A, 'checking file A (want: \'printf("A: a good feature"); // A\')')
    B = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/my-feature/B.c'.format(username))
    test('printf("B:agoodfeature");//B' in B, 'checking file B (want: \'printf("B: a good feature"); // B\')')
    C = get_raw('https://raw.githubusercontent.com/{}/hw-gitMergeAndRebase/my-feature/C.c'.format(username))
    test('printf("C:agoodfeature");//C' in C, 'checking file C (want: \'printf("C: a good feature"); // C\')')


methods = [hw1, hw2, hw3, hw4]
if __name__ == '__main__':
    methods[hw_index - 1]()