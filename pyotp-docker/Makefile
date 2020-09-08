SHA := $(shell git rev-parse HEAD)

.PHONY: build all

build:
	docker build -t pysprings/pyotp:latest -f ./Dockerfile .
	docker tag pysprings/pyotp:latest pysprings/pyotp:$(SHA)

all : build
