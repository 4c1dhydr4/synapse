@echo off
set COMMIT_MESSAGE=Synapse v0.0.2: Landing page init * website app init * Synapse logos update

echo Deploying: %COMMIT_MESSAGE%
echo Collecting static files
python manage.py collectstatic --no-input

echo Running database migrations
python manage.py makemigrations
python manage.py migrate

echo Commit changes to Git
git add .
git commit -m "%COMMIT_MESSAGE%
git push

echo No server. Finished
