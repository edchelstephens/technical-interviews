# technical-interviews
Repository For Technical Inteviews

# Python Version
## 3.13.5


# Run Unit tests

1. Install test requirements
    `pip install -r _requirements.txt`

2. Run coverage
    `coverage run -m pytest -sv && coverage report && coverage html && open -a 'Google Chrome' htmlcov/index.html`