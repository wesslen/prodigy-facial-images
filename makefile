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

download:
	git clone https://github.com/alireza116/visualstudy.git
	mkdir data
	mv visualstudy/public/* data
	rm -rf visualstudy

binary_anger:
	python -m prodigy mark binary_anger ./data/rq1 --loader images --label ANGER --view-id classification

classify_images:
	python -m prodigy classify-images image_categories ./data/rq1 -F scripts/classify_images.py

ab_captcha_preprocess:
	python scripts/convert.py data/rq2data.csv data/ab_captcha.jsonl

ab_captcha:
	python -m prodigy ab_captcha images data/ab_captcha.jsonl -F scripts/ab_captcha.py