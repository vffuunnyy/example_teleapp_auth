# Telegram Example Bot

This example demonstrates how to set up and use the [teleapp_auth](https://github.com/vffuunnyy/teleapp_auth) library.
The `teleapp_auth` library provides authentication functionalities for the Telegram WebApp.

## Prerequisites

Before you begin, ensure you have met the following requirements:

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/vffuunnyy/example_teleapp_auth.git
```

2. **Install Dependencies**

```bash
poetry install
```

3. **Create a `.env` File**

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
BOT_TOKEN=1111111111:11111111111111111111111111111111111
HOST=https://test.example.com
PORT=443
WEBHOOK_PATH=/tg_bot
```

4. **Edit ngix.conf**

Edit the `nginx.conf` file in the `test_bot` directory and replace the `server_name` and `ssl_certificate` values with your own.

5. **Run the Example**

```bash
docker-compose up
```

## Example Request

#### Request

```bash
curl --location 'http://127.0.0.1:8000/api/check_data' \
--header 'Content-Type: application/json' \
--data '{"auth_data": "query_id=AAEmj9sVAAAAACaP2xXjTtUN&user=%7B%22id%22%3A366710566%2C%22first_name%22%3A%22%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A3%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22vffuunnyy%22%2C%22language_code%22%3A%22en%22%2C%22is_premium%22%3Atrue%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1726656532&hash=fcdeec0fcbe55e52cedb50e58d5212fbc040ed0099dbb20b1de04458ed04f061"}'
```

#### Response

```json
{
    "status": true,
    "user": {
        "id": 366710566,
        "is_bot": null,
        "first_name": "ニューシャ",
        "last_name": "",
        "username": "vffuunnyy",
        "language_code": "en",
        "is_premium": true,
        "added_to_attachment_menu": null,
        "allows_write_to_pm": true,
        "photo_url": null
    }
}
```


## Used Libraries

- [teleapp_auth](https://github.com/vffuunnyy/teleapp_auth)
- [telegrinder](https://github.com/timoniq/telegrinder)
- [blacksheep](https://github.com/Neoteroi/BlackSheep)
- [granian](https://github.com/emmett-framework/granian)
- [uvloop](https://github.com/MagicStack/uvloop) (Linux only)
- [structlog](https://github.com/hynek/structlog)
- [envparse](https://github.com/rconradharris/envparse)