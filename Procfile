web: gunicorn birdview.wsgi --log-file -
migrate: python manage.py migrate --settings=birdview.settings.production
seed: python manage.py loaddata products/fixtures/products-data.json
seed: python manage.py loaddata products/fixtures/ingredients-data.json