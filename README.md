This repo contains a bunch of tools cooked up to fix firebase-js-sdk on May 24,
2019.

damage.txt contains the output of a git push --force that overwrite nearly all
refs in the repository.

orig-commits.txt is extracted from damage.txt and contains all the original commit ids.

test.sh can be run against a repo to determine how many commits from the golden
set are missing.

feiyangc@ had a copy with all the commits.

unpack.sh unpacks that copy and applies some fixes to it. See source.

`cd firebase-js-sdk`. The rest of the work was done from within the copy, where
all commands are now in the parent directory.

`../prune-locals.sh` removes any local branches that shouldn't be published

`../fix.py ../damage.txt fix` fixes the refs based on contents of damage.txt

`../fix.py ../damage.txt check` verifies that the refs match with git rev-parse

Result was checked with `git push --force --dry-run --tags origin 'refs/heads/*'`. 

The fix was a applied. Output in `fixed.txt`

