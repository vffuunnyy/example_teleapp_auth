# Telegram Example Bot

This example demonstrates how to set up and use the `teleapp_auth` library.
The `teleapp_auth` library provides authentication functionalities for the Telegram.

## Prerequisites

Before you begin, ensure you have met the following requirements:

## Setup Instructions

1. **Clone the Repository**

```sh
git clone https://github.com/vffuunnyy/teleapp_auth_example.git
```

2. **Install Dependencies**

```sh
poetry install
```

3. **Create a `.env` File**

Create a `.env` file in the root directory of the project and add the following environment variables:

```sh
BOT_TOKEN=1111111111:11111111111111111111111111111111111
HOST=https://test.example.com
PORT=443
WEBHOOK_PATH=/tg_bot
```

4. **Edit ngix.conf**

Edit the `nginx.conf` file in the `test_bot` directory and replace the `server_name` and `ssl_certificate` values with your own.

5. **Run the Example**

```sh
docker-compose up
```


## Used Libraries

- [teleapp_auth](https://github.com/vffuunnyy/teleapp_auth)
- [telegrinder](https://github.com/timoniq/telegrinder)
- [blacksheep](https://github.com/Neoteroi/BlackSheep)
- [granian](https://github.com/emmett-framework/granian)
- [uvloop](https://github.com/MagicStack/uvloop) (Linux only)
- [structlog](https://github.com/hynek/structlog)
- [envparse](https://github.com/rconradharris/envparse)