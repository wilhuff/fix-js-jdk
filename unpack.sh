#!/bin/bash

# Unpacks Fei's JS repo and prepares for fixing

tar xzf js-sdk.tar.gz
cd firebase-js-sdk

# These remotes were present but create ambiguity when checking out branches
# from origin. Removing them removes ambiguity
git remote remove fei
git remote remove samstern

# Remove hooks to prevent day-to-day automation from getting in the way
rm .git/hooks/*
