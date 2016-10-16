
all: clean build clean

build:
	@sudo python setup.py sdist
	@sudo python setup.py bdist bdist_egg bdist_wheel
	@sudo twine upload --config-file ~/.pypirc dist/*
	@make clean

install: build
	@sudo python setup.py install

gb_install:
	@gitbook install

gb_build: gb_install
	@gitbook build

gb_serve: gb_build
	@gitbook serve

clean:
	@sudo rm -rf *.zip
	@sudo rm -rf *.tar.gz
	@sudo rm -rf *.7z
	@sudo rm -rf *.rar
	@sudo rm -rf *.exe
	@sudo rm -rf build/
	@sudo rm -rf dist/
	@sudo rm -rf _book/
	@sudo rm -rf *.egg-info
