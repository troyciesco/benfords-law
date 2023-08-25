# NOTE: This isn't perfect, because I only have one db service.
# So it'd be kind of tricky to use all of the shorthand commands to run both the dev server
# and the local build at the same time, since you'd be bringing the db up and down.
# I think the commands are simple enough that this file can be referenced
# if you need to do that, though.


# Dev commands: spins up dev servers
boot-db-dev:
	docker-compose build db
	docker-compose up db

boot-api-dev:
	docker-compose build api
	docker-compose up api

boot-web-dev:
	docker-compose build web
	docker-compose up web
	
boot-dev:
		docker-compose build db api web
		docker-compose up db api web
dev: boot-dev

stop-dev:
		docker-compose stop db api web
sd: stop-dev

down-dev:
		docker-compose down db api web
dd: down-dev

restart-dev: stop-dev
restart-dev: boot-dev
rd: restart-dev

quit-dev: stop-dev
quit-dev: down-dev
qd: quit-dev

fresh-dev: stop-dev
fresh-dev: down-dev
fresh-dev: boot-dev
fd: fresh-dev

# Local Build commands: This is a prod-like environment to make sure
# builds look the same as dev. So you won't get HMR and such
boot-db-local-build:
	docker-compose build db
	docker-compose up db

boot-api-local-build:
	docker-compose build api-local-build
	docker-compose up api-local-build

boot-web-local-build:
	docker-compose build web-local-build
	docker-compose up web-local-build
	
boot-local-build:
		docker-compose build db api-local-build web-local-build
		docker-compose up db api-local-build web-local-build
blb: boot-local-build

stop-local-build:
		docker-compose stop db api-local-build web-local-build
slb: stop-local-build

down-local-build:
		docker-compose down db api-local-build web-local-build
dlb: down-local-build

restart-local-build: stop-local-build
restart-local-build: boot-local-build
rlb: restart-local-build

quit-local-build: stop-local-build
quit-local-build: down-local-build
qlb: quit-local-build

fresh-local-build: stop-local-build
fresh-local-build: down-local-build
fresh-local-build: boot-local-build
flb: fresh-local-build

# DANGER ZONE: This tries to remove everything in docker AND all data
# to simulate a fresh install. If you have images etc. that you care about
# on your local machine, don't run this.
danger-nuke:
	docker-compose stop
	docker-compose down
	docker-compose down --volumes
	docker system prune -a
	rm -rf web/.nuxt web/.output db_data