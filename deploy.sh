heroku create attdbtest

heroku addons:create heroku-postgresql:hobby-dev -a attdbtest

heroku git:remote -a attdbtest

git subtree push --prefix server heroku master