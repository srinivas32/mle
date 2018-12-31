#!/bin/bash

deb_version=$(git show debian:debian/changelog | awk 'NR==1{print $2}' | tr -d '()')

git log "debian-${deb_version}..HEAD" master --pretty=tformat:%H \
    | tac \
    | xargs -rn1 git cherry-pick
