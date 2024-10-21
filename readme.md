# My Portfolio Website

## Requirements
- FastAPI
- Python 3.8+
- Docker 
- Bootstrap (CSS framework)

---   

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [Docker Setup](#docker-setup)
- [Auto Deployment](#auto-deployment)  <!-- Added Auto Deployment section -->
- [License](#license)

---   

## Introduction
This is a personal portfolio website built using FastAPI and Bootstrap. It features sections like skills, education, work experience, and contact information, along with social media links and a simple dark-themed design.

**Feature:**
- Responsive design
- Integration with Google Analytics
- Auto deployment pipeline with Render
- Contact form or project showcase

---   

## Technologies Used
- **python**: 
- **FastAPI**: Backend framework
- **Docker**: To deploy or run
- **Git & GitHub**: To push and deploy
- **Bootstrap**: CSS framework for responsive design
- **FontAwesome**: For social media icons
- **Google Analytics**: For tracking user activity

---   

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-portfolio.git
   cd your-portfolio

2. **Install dependencies**: Create a virtual environment and install dependencies from the requirements.txt file:
    ```bash
        python -m venv env
        source env/bin/activate  # On Windows: env\Scripts\activate
        pip install -r requirements.txt

3. **Google Analytics Integration**:
    If you want to track visitor activity using Google Analytics, follow these steps:

 - Go to Google Analytics.
- Create an account and a property for your portfolio.
- Get the Tracking ID (starts with "UA-").
- Add the following script to the head section of your index.html file (or equivalent):
    ```bash
        <!-- Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_TRACKING_ID"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'YOUR_TRACKING_ID');
        </script>

- Replace YOUR_TRACKING_ID with your actual tracking ID.
- Deploy your portfolio, and Google Analytics will start collecting data.    

4. **Configure Docker**:  Build your Docker image
    ```bash
    docker build -t fastapi-portfolio:v1.0 .

5. **Run the Docker container**:
    ```bash
    docker run -d -p 8000:8000 --name portfolio -v my_volume:/app/data fastapi-portfolio:v1.0

---   

## How to Run
1. Locally: 
- Run FastAPI using uvicorn:
     ```bash
     uvicorn app:app --reload 

2. API will be running at:
    ```bash
    http://127.0.0.1:8000/

3. Open your browser (Safari, Chrome, Brave) and enter the URL:
   ```bash
   http://localhost:8000/

---   

## Docker Setup
**To containerize and run the portfolio using Docker, follow these steps:**

1. Build Docker Image:
Every time you make changes to your code, you need to create a new Docker image. Run the following command to build a new image:
    ```bash  
    docker build -t fastapi-portfolio:v1.0 .

2. Run Docker Container:
After building the image, use the following command to run the Docker container:
    ```bash  
    docker run -d -p 8000:8000 --name portfolio -v my_volume:/app/data fastapi-portfolio:v1.0

- -d runs the container in detached mode.
- -p 8000:8000 maps the container’s port 8000 to your local machine’s port 8000.
- -v my_volume:/app/data mounts a volume for persistent storage (optional based on your needs).

3. Access the Application:
Once the container is running, navigate to http://localhost:8000 in your browser to view the portfolio.

---   

## Auto Deployment
- This portfolio is automatically deployed on Render whenever new changes are pushed to the main branch on GitHub.

**How It Works:**
1. Auto-Trigger: When you push your code to GitHub, Render detects the changes and triggers a new deployment.
2. Live Update: The updated portfolio goes live once the deployment is complete.

**To set up a similar auto-deployment system on Render:**
1. Create an account on Render.
2. Connect your GitHub repository.
3. Set up a new web service, and Render will handle the rest.

--- 

## License
- This project is licensed under the MIT License - see the [License](License) file for details.

---    

