#About

Simple python tornado web-server with a ping response.

## Settings

You can change the logger config and the desired port on `settings.py`:
* Default logger has three different log files: *debug.log*, *info.log* and *error.log* and a console debug output.
* Default port is `8889`.

## Requirements

* Tornado is required.

To make sure you have all the packages installed, run `pip install -r requirements.txt`

## How to use

* Run `python main_ws_ping.py`
* On the web browser open [http://127.0.0.1:8889/ping](http://127.0.0.1:8889/ping).
* The web-server accepts **POST** or **GET** requests and always answers _1_.

##License

This is licensed under the MIT license.