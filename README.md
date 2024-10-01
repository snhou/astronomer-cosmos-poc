# astronomer-cosmos-poc

## Prerequisites
1. git
2. Python 3.9 or higher
3. Docker Desktop or Docker Compose

## Environment Setup
1. Clone this repository
```shell
git clone  https://github.com/snhou/astronomer-cosmos-poc.git
```
2. Build Docker Image

```shell
docker compose build
```
> if you modify your Dockerfile, you should add `--no-cache` argument to ignore previos cache

3. Create Docker Container

```shell
docker compose up -d
```

## Check dbt run properly
1. enter into docker container

```shell
docker exec -it astronomer-cosmos-poc-airflow-webserver-1 bash
```

2. Change into the `dbt/jaffle_shop` directory

```shell
cd /opt/airflow/dbt/jaffle_shop/
```

3. As usual, run all dbt steps
```shell
dbt debug
```
![alt text](./doc/image.png)
```shell
dbt seed
```
![alt text](./doc/image1.png)
```shell
dbt run
```
![alt text](./doc/image2.png)
```shell
dbt test
```
![alt text](./doc/image3.png)
```shell
dbt clean
```
![alt text](./doc/image4.png)


## Run Airflow DAG
![alt text](./doc/image5.png)