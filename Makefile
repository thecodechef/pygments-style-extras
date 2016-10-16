
all: clean build

build:
	python setup.py bdist_egg upload
	python setup.py sdist upload

install:
	python setup.py install

clean:
	rm -rf *.egg-info
	rm -rf *.zip
	rm -rf *.tar.gz
	rm -rf *.7z
	rm -rf *.rar
	rm -rf *.exe
	rm -rf build/
	rm -rf dist/
