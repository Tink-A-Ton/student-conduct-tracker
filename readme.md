# Student Conduct Tracker
Flask application designed using the **Model-View-Controller (MVC)** architecture.<br/>It allows staff to create and view student reviews.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
<!-- 
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Tink-A-Ton/student-conduct-tracker) -->


## Installation 
<details>
<summary><code>There are several ways you can install the application</code></summary>

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Tink-A-Ton/student-conduct-tracker.git
    cd student-conduct-tracker
    ```

2. **(Optional) Create a virtual environment**:

    - Using `venv`:
        ```sh
        python -m venv venv
        source venv/bin/activate    # On Windows use `venv\Scripts\activate`
        ```
    - Using `conda`:
        ```sh
        conda create --name your-env-name python=3.x
        conda activate your-env-name
        ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```
    
4. **Initialize the application**
    ```sh
    flask init
    ```

5. **Run the application**
    ```sh
    flask run
    ```

#### **Alernative**
- [Downloading repository as ZIP](https://github.com/Tink-A-Ton/student-conduct-tracker/archive/refs/heads/main.zip)
- Running the following command in a terminal, assuming you have [GitHub CLI](https://cli.github.com/) installed:

</details>

# API Routes
## Student Routes

1. ```/student/<id> [GET]``` : Retrieve student details by ID.
2. ```/students [GET]``` : Retrieve all students.
3. ```/student [POST]``` : Add a new student (admin only).

## Review Routes

1. ```/reviews [GET]``` : Retrieve all reviews.
2. ```/reviews/<student_id> [GET]``` : Retrieve reviews for a specific student by ID.
3. ```/review [POST]``` : Create a new review for a student.
4. ```/review/<id> [GET]``` : Retrieve a review by ID.


Routes for server can be tested via [postman](https://documenter.getpostman.com/view/26820239/2sAXxMhE3D)



## Model Diagram 

The model diagram denotes a User class that is inherited by Admin and Staff, along with a Student data class.<br/>Staff write Reviews for Students, while Admins add new Students to the system.

<img src="https://imgur.com/BeUcGZM.png" alt="Model Diagram" height="500"/>

## Test & CLI Commands

| Command              | Description                                   | Usage                                |
|----------------------|-----------------------------------------------|--------------------------------------|
| `flask init`         | Creates and initializes the database.         | `flask init`                         |
| `flask test user`    | Runs User tests (Unit/Integration).           | `flask test user [type]`             |
| `flask test student` | Runs Student tests (Unit/Integration).        | `flask test student [type]`          |
| `flask test review`  | Runs Review tests (Unit/Integration).         | `flask test review [type]`           |
| `flask test all`     | Runs all tests sequentially.                  | `flask test all`                     |
| `flask test unit`    | Runs all Unit tests.                          | `flask test unit`                    |
| `flask test int`     | Runs all Integration tests.                   | `flask test int`                     |
| `flask help`         | Displays available commands.                  | `flask help`                         |

