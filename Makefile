# GDG on Campus Kastamonu — haftalık bölüm üretimi
# Kullanım: make episode WEEK=2026-W44 → onay sayfası → make approve WEEK=2026-W44 → make episode WEEK=2026-W44
# make yoksa aynı komutlar: python -m pipeline <adım> --week <hafta>   (README'ye bakın)

ifeq ($(OS),Windows_NT)
PY ?= .venv/Scripts/python
else
PY ?= .venv/bin/python
endif
WEEK ?=
W := $(if $(WEEK),--week $(WEEK),)
F := $(if $(FORCE),--force,)

.PHONY: episode approve revise collect write normalize verify review tts assets render package setup

episode:
	$(PY) -m pipeline episode $(W) $(F)

approve:
	$(PY) -m pipeline approve $(W) $(if $(FLAGS),--accept-flags,)

revise:
	$(PY) -m pipeline revise $(W) --feedback "$(FEEDBACK)"

collect write normalize verify review tts assets render package:
	$(PY) -m pipeline $@ $(W) $(F)

setup:
	uv venv .venv --python 3.12
	uv pip install -p .venv -r requirements.txt
	uv pip install -p .venv torch torchaudio --index-url https://download.pytorch.org/whl/cu128 --reinstall-package torch --reinstall-package torchaudio
	$(PY) -m playwright install chromium
	cd video && npm ci
