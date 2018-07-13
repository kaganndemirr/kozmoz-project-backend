# Celery


## Installation of RabbitMQ

**For Fedora**
```bash
su root
dnf update
dnf install rabbitmq-server
/sbin/service rabbitmq-server start
```
**For Debian and Derivatives**
```bash
sudo su
apt update
apt install rabbitmq-server
```

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

For further information of installation and running Celery: [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
