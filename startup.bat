@ECHO off
start cmd /k python src\backend\server.py

timeout 2

cd src\frontend\mario_app\src
npm start

