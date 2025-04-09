format:
	black twitchybackend
	isort twitchybackend

docker-up:
	docker compose up -d

docker-down:
	docker compose down

collect-tests:
	python -m pytest --collect-only tests/

test:
	python -m pytest tests/

dev:
	python -m fastapi dev twitchybackend/app.py

install-deps:
	pip install -r requirements.txt -r requirements.dev.txt
	cd ./twitchyfrontend; npm install

build:
	cd ./twitchyfrontend; npm install && npm run build
