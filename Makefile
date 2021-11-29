### Variables ###

containers-tool = docker-compose
dev-dockerfile = -f docker-compose.yml -f docker-compose.dev.yml
prod-dockerfile = -f docker-compose.yml -f docker-compose.prod.yml

### Development ###

.PHONY: build-dev
build-dev:
	$(containers-tool) $(dev-dockerfile) build
	make dev

.PHONY: rebuild-dev
rebuild-dev:
	$(containers-tool) $(dev-dockerfile) build --no-cache
	make dev

.PHONY: dev
dev:
	$(containers-tool) $(dev-dockerfile) up --remove-orphans

### Prod ###

.PHONY: build-prod
build-prod:
	$(containers-tool) $(prod-dockerfile) build
	make prod

.PHONY: prod
prod:
	$(containers-tool) $(prod-dockerfile) up -d
