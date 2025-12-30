## Real-Time Python Chat Application
A simple client-server chat application built using Python's socket and threading libraries. This project demonstrates real-time communication between multiple clients through a central server.

## 🚀 Features
* Real-time Messaging: Exchange text messages instantly between users.

* Multi-client Support: The server handles multiple connections simultaneously using threading.

* Environment Configuration: Sensitive connection details (IP/Port) are managed via .env files for security.

* Command Line Interface (CLI): Lightweight and easy to run in any terminal.

## 🛠️ Key Concepts
This project covers several fundamental networking and programming concepts:

* Socket Programming: Using TCP/IP protocols for reliable data exchange.

* Threading: Managing concurrent tasks so the client can send and receive messages at the same time.

* Client-Server Architecture: A centralized server manages message broadcasting to all connected users.

## 📋 Prerequisites
* Python 3.x
* python-dotenv library

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Debarshi2006/OIBSIP.git]
   cd OIBSIP

2. **Install Dependencies:**
   ```bash
    pip install python-dotenv

## 💻 How to Run
* Start the Server: Run the server script first to start listening for connections.
    ```bash
    python server.py

* Start the Clients: Open new terminal windows for as many clients as you want and run:
    ```bash
    python client.py

Chat: Enter a nickname when prompted and start typing!

## 📁 Project Context
In the progression of the Oasis Infobyte Python Programming Internship, Project 7 serves as a deep dive into the Client-Server model and Network Communications. While previous projects focused on logic and local data management, this project addresses the challenge of real-time data exchange between independent systems. 