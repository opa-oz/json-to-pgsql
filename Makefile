.PHONY: help

#include .env
#export $(shell sed 's/=.*//' .env)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

clear:
	rm -rf build dist

build: clear ## https://mypyc.readthedocs.io/en/latest/getting_started.html#using-setup-py
	python3 setup.py bdist_wheel

run:
	python main.py

test:
	pytest