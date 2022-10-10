# Lab Manager

small django project to manage laboratory equipment reservations, Hardware configurations, etc...


# Deploy Prod

## Initial setup
- create a local-setup branch
- edit .env.prod file:
    * setup a local SECRET_KEY (random string)
    * setup DJANGO_ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS
    * setup database login/password

- edit .env.prod.db file:
    * setup database login/password

- eventually copy/modify docker-compose.prod file to tune up a local
  specific config (web port for instance)
```
sudo podman-compose -d -f docker-compose.prod.yml up
sudo podman exec labmanager_web_1 python manage.py collectstatic
sudo podman exec labmanager_web_1 python manage.py migrate
sudo podman exec -ti labmanager_web_1 python manage.py createsuperuser
```

