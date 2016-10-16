
all: clean build

build:
	@sudo python setup.py sdist upload

py_install: build
	@sudo python setup.py install

book-install:
	@gitbook install

book-build: book-install
	@gitbook build

book-serve: book-build
	@gitbook serve

clean:
	@rm -rf *.zip
	@rm -rf *.tar.gz
	@rm -rf *.7z
	@rm -rf *.rar
	@rm -rf *.exe
	@rm -rf build/
	@rm -rf dist/
	@rm -rf _book/
	@sudo rm -rf *.egg-info
