#!/bin/bash

# Removes all local branches other than master to start
# this prevents pushing unpublished work.

for branch in $(git branch); do
  if [[ branch == master ]]; then
    continue
  fi

  git branch -D "$branch"
done

