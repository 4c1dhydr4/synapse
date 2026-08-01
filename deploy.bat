@echo off
set COMMIT_MESSAGE=Synapse v0.0.3: CompressedStaticFilesStorage

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

echo Connecting Server
ssh root@178.128.4.226
