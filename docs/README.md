# {{ config.title }}

> A Collection of custom pygments styles for python

## Installation

#### PyPi

```bash
$ (sudo) pip install pygments-style-extras
```

#### Easy Install

```bash
$ (sudo) easy_install pygments-style-extras
```

#### Manually

```bash
$ git clone https://github.com/thecodechef/pygments-style-extras.git
$ cd pygments-style-extras
$ (sudo) python setup.py install
```

## Usage

### Converting to CSS

```bash
$ pygmentize -f html -S [style] -a .parent-class > css/[style].css
```

### Examples

#### Github Example

```bash
$ pygmentize -f html -S github -a .parent-class > css/github.css
```

#### MonokaiLight Example

```bash
$ pygmentize -f html -S monokai_light -a .highlight > css/monokai_light.css
```

#### Railscasts Example

```bash
$ pygmentize -f html -S railscasts -a .highlight > css/railscasts.css
```


## Bug Reporting

if you find any bugs/issues report it at [github](https://github.com/) and create a new [issue](https://github.com/thecodechef/pygments-style-extras/issues/new)

## Thanks

Thank You to all these people:

* [Pygments](http://www.pygments.org)
* [Python](http://www.python.org)
* Your Name Here
