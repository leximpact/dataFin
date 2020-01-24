#!/bin/bash

.PHONY: install test

install:
	pip install -r requirements.txt

test:
	pytest tests/*py

