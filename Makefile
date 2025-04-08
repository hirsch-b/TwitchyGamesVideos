format:
	black twitchybackend
	isort twitchybackend

docker-up:
	docker compose up -d

docker-down:
	docker compose down

collect-tests:
	pytest --collect-only tests

test:
	pytest tests

dev:
	fastapi dev twitchybackend/app.py

install-deps:
	pip install -r requirements.txt -r requirements.dev.txt
	cd ./twitchyfrontend; npm install

build:
	cd ./twitchyfrontend; npm install && npm run build
