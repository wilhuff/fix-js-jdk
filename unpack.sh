#!/bin/bash

# Unpacks Fei's JS repo and prepares for fixing

tar xzf js-sdk.tar.gz
cd firebase-js-sdk
git remote remove fei
git remote remove samstern
rm .git/hooks/*
