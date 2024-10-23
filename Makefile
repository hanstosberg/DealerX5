# Переменные
PYTHON := python3
APP_NAME := main.py
VENV := venv

# Цель по умолчанию
all: run

# Цель для запуска приложения
run:
	$(PYTHON) $(APP_NAME)

# Очистка
clean:
	rm -rf __pycache__ $(VENV)

.PHONY: all run clean