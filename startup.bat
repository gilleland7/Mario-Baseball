@ECHO off
start cmd /k python src\backend\server.py

timeout 2

cd C:\Users\mattg\Documents\GitHub\Mario\src\frontend\mario_app\src
npm start

