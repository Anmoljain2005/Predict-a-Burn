# Predict-a-Burn: Calories Burnt Prediction Web Application

**Predict-a-Burn** is a machine learning-based web application designed to predict the number of calories burned during various physical activities. By analyzing user input, the model provides accurate calorie expenditure estimates, aiding users in tracking and managing their fitness goals effectively.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User-Friendly Interface**: Intuitive design for seamless user experience.
- **Accurate Predictions**: Utilizes advanced machine learning algorithms to estimate calorie burn.
- **Customizable Inputs**: Users can input various parameters such as activity type, duration, and intensity.

## 🔥 Interface Preview

Here's a look at the Predict-a-Burn web app in action:

![Web Interface Screenshot](static\Image\Frontend_SS.png)

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Anmoljain2005/Predict-a-Burn.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Predict-a-Burn
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application:


```bash
python application.py
```

Then, open your web browser and go to `http://localhost:8000` to access the application.

## Project Structure


```plaintext
Predict-a-Burn/
├── artifacts/
├── catboost_info/
├── notebook/
├── src/
├── static/
├── templates/
├── .gitignore
├── application.py
├── requirements.txt
└── setup.py
```

- **artifacts/**: Contains saved models and other artifacts.
- **catboost_info/**: Directory related to CatBoost model information.
- **notebook/**: Jupyter notebooks for exploratory data analysis and model development.
- **src/**: Source code for the application.
- **static/**: Static files like CSS, JavaScript, and images.
- **templates/**: HTML templates for the web application.
- **application.py**: Main Flask application file.
- **requirements.txt**: List of Python dependencies.
- **setup.py**: Setup script for packaging.

## Model Information

The application leverages the CatBoost machine learning algorithm to predict calorie expenditure based on user inputs. The model is trained on a diverse dataset to ensure accuracy across various activities and user profiles.

## Contributors

| Name | GitHub | Roll Number |  
|-------|--------|-------------|  
| **Anmol Jain** | [Anmol Jain](https://github.com/Anmoljain2005) | 230008009 |  
| **Salaj Bansal** | [Salaj Bansal](https://github.com/SalajBansal05) | 230002063 |  
| **Nidarsana M** | [Nidarsana M](https://github.com/Nidarsana02) | 230004031 |  

## Acknowledgements

This Prediction Model is part of the course **MA-212: Regression Analysis** under the guidance of **Dr. Mohd. Arshad**.

---