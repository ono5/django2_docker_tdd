.PHONY: test release clean

test:
	docker-compose build --pull release
	docker-compose build
	docker-compose run test

release:
	docker-compose up --abort-on-container-exit migrate
	docker-compose run app python3 manage.py collectstatic --no-input
	docker-compose up

ft:
	docker-compose run --rm app pytest ${f1} ${f2} functional_tests.py

ut:
	docker-compose run --rm app pytest -v -s -l ${filename}

clean:
	docker-compose down -v
	docker images -q -f dangling=true -f label=application=todobackend | xargs -I ARGS docker rmi -f --no-prune ARGS

