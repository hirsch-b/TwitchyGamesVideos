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
