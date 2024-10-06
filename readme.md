# Student Conduct Tracker Flask Application

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Tink-A-Ton/student-conduct-tracker)

Flask application designed using the **Model-View-Controller (MVC)** architecture. This app allows for 

## Installation Guide
<details>
<summary><code>There are several ways you can install the application</code></summary>

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Tink-A-Ton/student-conduct-tracker.git
    cd Comp3613A1
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
    
4. **Run the Code**
    ```sh
    flask init
    ```

#### **Alernative**
- [Downloading repository as ZIP](https://github.com/Tink-A-Ton/student-conduct-tracker/archive/refs/heads/main.zip)
- Running the following command in a terminal, assuming you have [GitHub CLI](https://cli.github.com/) installed:

</details>

## Model Diagram 



## Test & CLI Commands 

Below are the available CLI commands for database operations and testing:

| Command                        | Description                                                                                          | Usage                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| `flask init`                   | Creates and initializes the database.                                                                | `flask init`                                               |
| `flask test user`             | Runs User tests (Unit and/or Integration).                                                           | `flask test user [type]` (default: all)                   |
| `flask test student`          | Runs Student tests (Unit and/or Integration).                                                        | `flask test student [type]` (default: all)                |
| `flask test review`           | Runs Review tests (Unit and/or Integration).                                                         | `flask test review [type]` (default: all)                 |
| `flask test all`              | Runs all tests (Unit and Integration) sequentially.                                                  | `flask test all`                                          |
| `flask help`                  | Displays all available commands and their descriptions.                                              | `flask help`                                             |
