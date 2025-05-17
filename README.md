SimpleTimeService Flask App (Task 1)

📄 Project Overview

SimpleTimeService is a lightweight Python Flask web application that returns the current time in Indian Standard Time (IST) and the IP address of the visitor. It is containerized using Docker and can run anywhere — locally, on EC2, or in cloud containers.

🚀 Features

Returns timestamp in Asia/Kolkata timezone

Displays the visitor's IP address

Simple REST API on root endpoint /

Built with Flask

Dockerized using a secure, lightweight Python base image

📁 Project Structure

simple-time-service/
├── app/
│   └── app.py            # Flask application code
├── Dockerfile            # Docker build instructions
├── README.md             # Project documentation

🛠️ Requirements

Python 3.8+

Docker

(Optional) GitHub account & DockerHub account for version control and image hosting

⚙️ How to Run Locally (Without Docker)

cd app
pip install flask pytz
python app.py

Then open your browser:

http://localhost:8080

🐳 How to Build & Run with Docker

1. Build the Docker Image

docker build -t simple-time-service .

2. Run the Container

docker run -d -p 8080:8080 simple-time-service

3. Test the Application

Open in browser or run:

curl http://localhost:8080

Expected output:

{
  "timestamp": "2025-05-01T10:00:00+05:30",
  "ip": "127.0.0.1"
}

☁️ Deploy to EC2 (Manual)

Launch an EC2 instance with Docker installed.

Open port 8080 in the security group.

SSH into the instance:

ssh -i your-key.pem ubuntu@<ec2-public-ip>

Pull and run:

docker pull nabeel111/simple-time-service:latest
docker run -d -p 8080:8080 nabeel111/simple-time-service

Access the app via:

http://<ec2-public-ip>:8080

🔐 Security Note

Flask app should not be used in production without a proper WSGI server (e.g., Gunicorn).

Container runs as a non-root user (as per best practices).

🧹 Cleanup

docker ps -a
# Stop and remove container
docker stop <container-id>
docker rm <container-id>

👨‍💻 Author

Created by Nabeel SK as part of DevOps hands-on Task 1.

📘 License

This project is for educational purposes only.

