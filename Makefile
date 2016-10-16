
all: clean build

build:
	python setup.py bdist_egg upload --identity="Jeremy Bolding"
	python setup.py sdist upload --identity="Jeremy Bolding"

clean:
	rm -rf *.egg-info
	rm -rf *.zip
	rm -rf *.tar.gz
	rm -rf *.7z
	rm -rf *.rar
	rm -rf *.exe
