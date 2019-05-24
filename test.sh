#!/bin/bash

top_dir=$(dirname ${BASH_SOURCE[0]})

for c in $(cat $top_dir/orig-commits.txt); do
  if ! git rev-parse $c >& /dev/null; then
    echo missing
  fi
done | wc -l
