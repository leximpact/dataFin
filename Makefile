#!/bin/bash

.PHONY: install test

install:
	pip install -r back/requirements.txt

test:
	pytest back/tests/*py

