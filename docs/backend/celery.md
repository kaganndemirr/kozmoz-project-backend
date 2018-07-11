# Celery


## Installation of RabbitMQ
```bash
# For Fedora and Debian
su root
# For Ubuntu and Linux Mint
sudo su

apt-get update
apt-get install rabbitmq-server
```
If you use another os: [RabbitMQ Installation for Other Distribution](https://www.rabbitmq.com/download.html)<br>


## Setting up RabbitMQ
```bash
rabbitmqctl add_vhost kozmoz_vhost
rabbitmqctl set_permissions -p kozmoz_vhost guest ".*" ".*" ".*"
```
For further information of setting up RabbitMQ: [Setting up RabbitMQ](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq)


## How to run Celery
```bash
celery -A kozmoz worker -n kozmoz_celery@%h --statedb=./kozmoz_worker.state
```

**If you want to see your tasks list or output status**:
```bash
celery -A kozmoz worker -l info -n kozmoz_celery@%h --statedb=./kozmoz_worker.state
```

**If you use Windows**:
```bash
celery -A kozmoz worker -n kozmoz_celery@%h --statedb=./kozmoz_worker.state -P eventlet
```

**If you want to see your tasks list or output status on Windows**:
```bash
celery -A kozmoz worker -l info -n kozmoz_celery@%h --statedb=./kozmoz_worker.state -P eventlet
```

For further information of installation and running Celery: [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
