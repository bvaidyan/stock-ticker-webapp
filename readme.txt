server deployment
-----------------
if adding/changing any files
git add fname
git commit -m "commit-num"
heroku config:add BUILDPACK_URL=https://github.com/thedataincubator/conda-buildpack.git#py3
git push heroku master

goto http://bvaidyan-ticker.herokuapp.com/index to view the app

Local testing
-------------
export QUANDLKEY=XjC3DuFeDAERUVmQfscL
export GOOGLE_ANALYTICS_CODE=UA-125413559-1
python app.py
goto http://localhost:33507/index

Websites followed
-----------------
https://github.com/thedataincubator/flask-framework
https://github.com/samuelgthorpe/hello-flask/blob/master/app.py
https://www.thedataincubator.com/12day.html, Day 10

STEPS to build the app
----------------------
1. clone the https://github.com/thedataincubator/flask-framework
2. Added my templates,static,app.py and corresponding dependencies in conda-req files
3. git add fname_that_are_added_or_changed
4. git commit -m "commit-num"
5. heroku config:add BUILDPACK_URL=https://github.com/thedataincubator/conda-buildpack.git#py3
6. git push heroku master
7. Once the app is pushed to heroku, go into app setting and add QUANDLKEY/GOOGLE_ANALYTICS_CODE and its value here https://dashboard.heroku.com/apps/bvaidyan-ticker/settings under Config Vars section
8. Pick the quandl key (XjC3DuFeDAERUVmQfscL) from my login usr: gmail email, pwd: cse pwd
9. Get the GOOGLE_ANALYTICS_CODE = UA-125413559-1 from https://analytics.google.com/
