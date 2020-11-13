heroku create attdb

heroku addons:create heroku-postgresql:hobby-dev -a attdb

heroku git:remote -a attdb