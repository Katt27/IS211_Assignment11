# IS211_Assignment11
IS211_Assignment11

#This repository contains a simple Flask web application that serves as a To-Do list. Users can add tasks with descriptions, assign them to an email address, and categorize them by priority (Low, Medium, High). The list can also be cleared entirely via a dedicated button.

Features
Add To-Do items with task descriptions, responsible person's email, and priority level.
View all added To-Do items in a list.
Clear all tasks from the To-Do list.
Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You need Python and Flask installed on your computer. If you don't have Python installed, you can download it from python.org. To install Flask, run the following command:

bash
Copy code
pip install Flask
Installing
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/Katt27/IS211_Assignment11.git
cd IS211_Assignment11
Ensure that the index.html file is located inside a folder named templates in the same directory as todoapp.py. If not, create the folder and move the file:
bash
Copy code
mkdir templates
mv index.html templates/index.html
Running the Application
To run the application, execute the following command in the root directory of the project:

bash
Copy code
python todoapp.py
This will start a web server on http://localhost:5000. Open your web browser and go to this address to use the application.

Using the Application
To Add a To-Do Item: Fill out the form on the main page with the task description, email of the responsible person, and select the priority. Click the "Add To-Do Item" button to submit.
To Clear the List: Click the "Clear" button on the main page to remove all tasks from the list.
