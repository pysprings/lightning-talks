.PHONY: build clean

build: clean
	mkdir -p build
	cp -R myapp build
	python -m pip install -r requirements.txt --target build
	find ./build -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +
	mkdir -p dist
	python -m zipapp build -o dist/myapp.pyz -p "/usr/bin/env python3" -m "myapp.app:main" -c


clean:
	rm -rf build
