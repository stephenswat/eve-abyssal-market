#!/bin/bash

mkdir /dev
npm cache clean --force
npm install
npm run dev-host
