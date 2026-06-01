# Playwright Python Framework

## Overview

This project is a UI test automation framework built using Python, Playwright, and Pytest. The framework follows the Page Object Model (POM) design pattern to improve maintainability, reusability, and scalability of test scripts.

## Tech Stack

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* HTML Test Reports

## Project Structure

playwright-python-framework/
├── pages/
├── tests/
├── utils/
├── reports/
├── requirements.txt
└── pytest.ini

## Test Coverage

### Login Tests

* Valid login
* Invalid login
* Error message validation

### Inventory Tests

* Product count validation
* Product name verification
* Add-to-cart functionality
* Cart item verification

## Setup Instructions

1. Clone the repository

git clone https://github.com/SeemaC0507/playwright-python-framework.git

2. Install dependencies

pip install -r requirements.txt

3. Install Playwright browsers

playwright install

## Execute Tests

Run all tests:

pytest -v

Generate HTML report:

pytest --html=reports/report.html --self-contained-html

## Key Features

* Page Object Model framework design
* Reusable test components
* Data-driven test support
* HTML reporting
* Easy maintenance and scalability

## Future Enhancements

* Cross-browser execution
* CI/CD integration with GitHub Actions
* Data-driven testing using external files
* Parallel test execution
