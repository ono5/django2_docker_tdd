.PHONY: test release clean

test:
	docker-compose build --pull release
	docker-compose build
	docker-compose run test

release:
	docker-compose up --abort-on-container-exit migrate
	docker-compose run app python3 manage.py collectstatic --no-input
	docker-compose up

all_tests:
	docker-compose run --rm app pytest

ft:
	docker-compose run --rm app pytest -v -s -l functional_tests/tests.py

ut:
	docker-compose run --rm app pytest -v -s -l ${dir}

mk:
	docker-compose run --rm app python3 manage.py makemigrations
	docker-compose run --rm app python3 manage.py migration ${app_name}

clean:
	docker-compose down -v
	docker images -q -f dangling=true -f label=application=todobackend | xargs -I ARGS docker rmi -f --no-prune ARGS


flash:
	docker-compose run --rm app python3 manage.py flush --database=default --noinput
	docker-compose run --rm app python3 manage.py createsuperuser

