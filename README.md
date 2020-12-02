<p align="center">
  <a href="#" target="_blank" rel="noopener noreferrer">
    <img width="400" src="assets/logo_pxl.png" alt="PXL">
  </a>
</p>

<p align="center">
   <a href="https://opensource.org/licenses/MIT">
    <img alt="GitHub" src="https://img.shields.io/github/license/SheldonPi1999/ATT-Dashboard?style=for-the-badge">
  </a>

  <a href="https://github.com/JensVanhulst/IOT-Dashboard/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/SheldonPi1999/ATT-Dashboard?style=for-the-badge">
  </a>
</p>

# All Things Talk - Dashboard

This project is an IOT dashboard written in Vue.js and python. It is designed to work with the "All things talk rapid development kit"

---

## Table of Contents

- [All Things Talk - Dashboard](#all-things-talk---dashboard)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
  - [Configuration](#configuration)
    - [Setup sensor kit](#setup-sensor-kit)
    - [Development](#development)
    - [Ports](#ports)
  - [Workflow for development](#workflow-for-development)
  - [Deployment](#deployment)
  - [Contributors](#contributors)
  - [Questions](#questions)
  - [License](#license)

---

## Setup

You need to have the following tools installed on your system

> NOTE : If you install docker-desktop, docker-compose comes preinstalled. If you are on Linux you need to install docker and docker compose separately

| Software name  | version | version in project |       link       |
| :------------: | :-----: | :----------------: | :--------------: |
|     Python     |   3.8   |       3.8.5        |     [python]     |
|     Pipenv     | latest  |     2020.8.13      |     [pipenv]     |
|    Node JS     | 14.13.0 |      14.13.0       |     [nodejs]     |
|    Vue CLI     | latest  |   @vue/cli 4.5.8   |     [vuecli]     |
| Docker desktop | latest  |       latest       | [docker-desktop] |
|      Git       | latest  |       2.28.0       |      [git]       |
|   Heroku CLI   | latest  |   heroku/7.45.0    |   [heroku-cli]   |
|    Arduino     | latest  |       1.8.13       |    [arduino]     |

[python]: https://www.python.org/downloads/
[pipenv]: https://pipenv.pypa.io/en/latest/install/#installing-pipenv
[nodejs]: https://nodejs.org/en/download/
[vuecli]: https://cli.vuejs.org/guide/installation.html
[docker-desktop]: https://www.docker.com/products/docker-desktop
[git]: https://git-scm.com/downloads
[heroku-cli]: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
[arduino]: https://www.arduino.cc/en/software

Clone this repository

```sh
git clone https://github.com/SheldonPi1999/ATT-Dashboard
```

## Configuration

### Setup sensor kit

To setup your sensorkit you can follow this guide :
https://github.com/cteqeu/pxlairquality/blob/master/General/Slides/20200117_NB-IoT%20Project%20HW_To_Allthingstalk_Communication.pdf

Edit the code in `hardware/keys.h`

```c
/****
 * Enter your AllThingsTalk device credentials below
 */
#ifndef KEYS_h
#define KEYS_h
const char* DEVICE_ID = "CHANGE HERE";
const char* DEVICE_TOKEN = "CHANGE HERE";
const char* APN = "starter.att.iot";
#endif
```

After you edited the code. You will also need to install some libraries for the arduino and upload the sketch.

All of this can be done by using the following guide.
https://github.com/cteqeu/pxlairquality/blob/master/General/Slides/20200117_NB-IoT%20Project_Arduino.pdf

### Development

- You need to copy the environment variables from `db.env.sample` into a `db.env`
  and set the values.
- Change the following values in the `docker-compose.yaml` to what you want.
  These values will be your login credentials on pgAdmin

  ```yaml
    ...
    PGADMIN_DEFAULT_EMAIL: login-email@example.com
    PGADMIN_DEFAULT_PASSWORD: secret-password-here
    ...
  ```

- In the server folder change the values in `configuration.py` file

  ```python
  class Config(object):
    ENV = "production"
    PORT = 80
    # ENV = "dev"
    # PORT = 3000
    ATT_DEVICE_ID = "token-here"
    SECRET = 'secret-here'
    TEMPLATES_AUTO_RELOAD = True
    MQTT_BROKER_URL = "api.allthingstalk.io"
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = "maker:XXXXXXXX"
    MQTT_PASSWORD = 'xxxxxx'
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False
    MQTT_CLEAN_SESSION = True
  ```

- **_Client_**
  - You need to copy the environment variables from `.env.sample` into a `.env`
    and set the values to either `DEVELOPMENT` or `PRODUCTION`

### Ports

The following ports are used in development

|  Service   | Port |
| :--------: | :--: |
|    MQTT    | 1883 |
| Flask api  | 3000 |
| Vue client | 8081 |
| postgresql | 5432 |
|  pgAdmin   | 8080 |

The following ports are used in production

|  Service   | Port |
| :--------: | :--: |
|    MQTT    | 1883 |
| Flask api  |  80  |
| postgresql | 5432 |

## Workflow for development

Change into directory

```sh
cd ATT-Dashboard
```

Start docker database

```sh
# This command will download all images needed to setup the database
docker-compose up
```

After the database is running you can start up the server by

```sh
cd server

# Create a shell inside the environment
pipenv shell

# Install dependencies
pipenv install

# Run server
python app.py
```

The last step is to startup the client

```sh
cd client

# Install dependencies
npm install

# Run application
npm run serve
```

## Deployment

Build the client

> The following command will create static html, css, js files in de server public directory

```sh
cd client && npm run build
```

Create heroku app

```sh
heroku create my-app-name
```

Create Postgresql DB on heroku

```sh
heroku addons:create heroku-postgresql:hobby-dev -a my-app-name
```

Set heroku remote to git repo

```sh
heroku git:remote -a my-app-name
```

Push to heroku

```sh
git subtree push --prefix server heroku master
```

## Contributors

- **Jens Vanhulst** - _CONTRIBUTOR_ - [Jens Vanhulst](https://github.com/JensVanhulst)
- **Kasper Toetenel** - _CONTRIBUTOR_ - [Kasper Toetenel](https://github.com/SheldonPi1999)

## Questions

For questions and support please submit an issue.

## License

This project is licensed under the APACHE GPL 2 License - see the [LICENSE](LICENSE) file for details
