# Shubhanshu Mishra's Technical blog

[![build blog](https://github.com/napsternxg/blog/actions/workflows/github_actions.yml/badge.svg?branch=master)](https://github.com/napsternxg/blog/actions/workflows/github_actions.yml)

Technical blog on data science, python, machine learning etc.


## Installation

```bash
mkdir -p ../pelican-themes
pushd ../pelican-themes
git clone https://github.com/napsternxg/pelican-bootswatch
popd
sudo apt-get install make
conda env create -f environment.yml
source activate pelican
DEBUG=1 make publish serve
```

### Local Testing

```
make html serve
```
