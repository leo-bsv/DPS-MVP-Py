start:
	docker compose up --build -d && sleep 5 && docker compose logs

run:
	docker compose up -d

run_logs:
	docker compose up

logs_web:
	docker compose logs web

logs_psql:
	docker compose logs db

logs_nginx:
	docker compose logs nginx

stop:
	docker compose stop

migrate:
	docker compose exec web python /code/DAAS/manage.py migrate

makemigrations:
	docker compose exec web python /code/DAAS/manage.py makemigrations

logs:
	docker compose logs

input:
	docker compose exec web python /code/DAAS/manage.py $(command)

