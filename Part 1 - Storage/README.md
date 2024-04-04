<div style="display: flex; justify-content: center; align-items: center; width: 500px; margin: 0 auto;">
    <img src="https://avatars.githubusercontent.com/u/44686652?v=4" height=100 style="align-self: center;">
    <img alt="image" src="https://github.com/GuillaumeDorschner/ESILV-Cryptography-S8-1/assets/44686652/43f3aba2-7fcc-46a9-b818-73c2ad932501" height=100 style="align-self: center;">
    <div style="padding: 20px; text-align: center;">
        <h3 style="font-size: 16px;">Project CryptoGraphie - 1</h3>
        <h3 style="font-size: 16px;">Guillaume Dorschner & Jules Deleuse</h3>
        <h3 style="font-size: 16px;">A4 - CCC</h3>
    </div>
    <img src="https://www.esilv.fr/ecole-ingenieur/logos/logo_esilv_png_couleur.png" width="100" style="align-self: center;">
</div>

# Introduction

This project is a comprehensive exploration of cryptographic principles and their application in securing user data. Through a two-part implementation focusing on **password storage** and **Password-Authenticated Key Exchange (PAKE)** [see here](https://github.com/GuillaumeDorschner/ESILV-Cryptography-S8-2), this project demonstrates robust security practices in application development.


# Project Implementation

Requirement for the implementation: password storage. Think about it as you are building some application that has user system (username and password) and you need to store the password securely. You should implement your solution, taking into accounts all the attack scenarios we have discussed. Basically the grade will be scored according to how secure your implementation is. The implementation needs to be runnable, where I can enter my username and password for registration and logging in (the interface can be a web app, or terminal etc).

If you are using any cryptographic encryption implementation, you need to use [google tink library](https://developers.google.com/tink) (except for the hash functions). Implementation using other libraries does not count.

# Getting Started

## Installation

> [!WARNING]
> For running the project locally in an easier-to-debug manner, follow the order below. In the future, we will use Docker-compose for project execution. Respect the following order:
> 1. docker compose up
>    ```bash
>     docker-compose up
>     ```
> 2. terminal 2
>    ```bash
>     flask run --host=0.0.0.0 --port=80
>     ```

We use docker to run the application for simplicity. You can install docker from [here](https://docs.docker.com/get-docker/).

1. Download docker on your computer
2. Download the [release](https://github.com/GuillaumeDorschner/ESILV-Cryptography-S8/releases/latest) of the project
3. Change the example.env to .env and fill in the environment variables. Then run the following command to start the application:

```bash
docker compose up
```

# What we will be using

All the code is written in Python, and we will be using the following libraries:
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [PostgreSQL database](https://www.postgresql.org/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Argon2](https://en.wikipedia.org/wiki/Argon2)
- [Google Tink](https://developers.google.com/tink) for all cryptographic operations.

```mermaid
graph LR
    Front[Flask Frontend] <--> Server
    Database[Postgres Database] <--> Server
    Server[Flask Backend] --> Postgres[PostgreSQL database]
    Server[Flask Backend] --> Flask-Login[Flask-Login]
    Server[Flask Backend] --> Argon2[Argon2]
    Server[Flask Backend] --> Tink[Google Tink]
```

# Diagrams and Explanations

Example of Sequence Diagram.

### First part of the project: Password storage

```mermaid
    sequenceDiagram
    participant U as User (Alice)
    participant S as Server (Bob)
    participant D as Database

    Note over U,S: Registration Phase
        U->>S: Hello I want to signup I'm Bob with password "1234"
        S-->>S: Hash the password with salt
        S-->>D: Store: hashed password & salt
        S-->>S: Generate a session token
        S-->>D: Store: session token
        S-->>U: Welcome Bob | send the session token

    Note over U,S: Login Phase
        U->>S: Hello, I'm Bob with password "1234"
        S-->>D: Retrieve: hashed password & salt
        S-->>S: Hash the password with the retrieved salt
        S-->>S: Compare the hashed password with the one in the database
        S-->>D: Generate a session token
        S-->>U: Welcome Bob | send the session token
```
