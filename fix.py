#!/usr/bin/env python

import subprocess
import re
import sys

def read_damage(filename):
    with open(filename) as fd:
        return [line.rstrip() for line in fd.readlines()]

def find_commit_name_pairs(lines):
    pattern = re.compile(r'^ \+ ([^.]*)\.\.\.[^ ]* ([^ ]*) -> .*')
    result = []
    for line in lines:
        if not line:
            continue
        m = pattern.match(line)
        if not m:
            raise Exception("Failed to match line: '" + line + "'")

        result.append((m.group(1), m.group(2)))

    return result

def find_branches():
    pattern = re.compile(r'remotes/origin/(.*)')
    output = subprocess.check_output(['git', 'branch', '-a'])

    branches = []
    for line in output.splitlines():
        m = pattern.search(line)
        if m:
            branches.append(m.group(1))

    return set(branches)


def find_tags():
    output = subprocess.check_output(['git', 'tag', '-l'])

    tags = [line.rstrip() for line in output.splitlines()]
    return set(tags)


def fix_branch(commit, ref):
    subprocess.check_call(['git', 'checkout', ref])
    subprocess.check_call(['git', 'reset', '--hard', commit])


def fix_tag(commit, ref):
    subprocess.check_call(['git', 'tag', '-f', ref, commit])


def run_fix(pairs, branches, tags):
    for commit, ref in pairs:
        if ref in branches:
            fix_branch(commit, ref)
        elif ref in tags:
            fix_tag(commit, ref)
        else:
            raise Exception("Unknown ref " + ref)

def rev_parse(ref):
    output = subprocess.check_output(['git', 'rev-parse', '--short', ref])
    return output.rstrip()

def run_check(pairs):
    for commit, ref in pairs:
        actual = rev_parse(ref)
        if actual != commit:
            raise Exception("actual didn't match: %s vs %s" % (actual, commit))


def main(args):
    command = args[2]
    lines = read_damage(args[1])
    pairs = find_commit_name_pairs(lines)
    branches = find_branches()
    tags = find_tags()

    if command == 'fix':
        run_fix(pairs, branches, tags)
    elif command == 'check':
        run_check(pairs)



main(sys.argv)
