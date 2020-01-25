#!/bin/bash

.PHONY: install test

install:
	pip install -r back/requirements.txt

test:
	pytest back/tests/*py

run:
	@echo "API web servie en http://localhost:5000..."
	python app.py
