# IS211 Assignment11 - Flask To-Do List Application

This repository hosts a simple Flask web application for managing a To-Do list. It allows users to add tasks, specify the email of the person responsible, and set a priority level (Low, Medium, High). Users can also clear the entire list with a single click.

## Features

- **Add To-Do Items**: Add tasks with descriptions, assign them to an email, and set a priority level.
- **View To-Do List**: All current tasks are displayed in a simple table format.
- **Clear To-Do List**: A single button to clear all entries from the list.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have Python installed on your system. You can download Python [here](https://www.python.org/downloads/). You will also need Flask, which can be installed using pip:

```bash
pip install Flask

1. Installation
Follow these steps to get your development environment running:

Clone the repository:
git clone https://github.com/Katt27/IS211_Assignment11.git
cd IS211_Assignment11

2. Set up the directory structure:
Ensure that index.html is located in a templates folder within the same directory as todoapp.py. If this folder does not exist, create it and move the file:

mkdir templates
mv index.html templates/index.html

3. Running the Application:
To run the application, use the following command in the project root directory:
python todoapp.py

The application will be accessible via http://localhost:5000 in your web browser.

Usage:
Adding a To-Do Item: Complete the form on the homepage with the task's details, the responsible person's email, and the task's priority. Submit by clicking "Add To-Do Item".
Clearing the List: Click the "Clear" button to remove all tasks from the display.



