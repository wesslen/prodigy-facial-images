create-venv:
	( \
		python -m venv venv; \
		source venv/bin/activate; \
	)

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	python -m pip install -r requirements-prodigy.txt

clean-cache:
	rm -rf */__pycache__/*
	rm -rf .ipynb_checkpoints

clean-files:
	rm -rf data/*

clean-venv:
	rm -rf venv