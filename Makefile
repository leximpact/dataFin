#!/bin/bash

.PHONY: install test

install:
	pip install -r back/requirements.txt

test:
	pytest back/tests/*py

# python -m http.server
# python app.py pour runner l'index.html sur http://localhost:5000
