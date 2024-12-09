from flask import Flask, request
import os
import socket

app = Flask(__name__)

# Get the environment variable for color; default to 'black'
color = os.getenv("COLOR", "black")
environment = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def hello():
    # Get the hostname of the current container
    hostname = socket.gethostname()
    # Return the HTML response with the hostname and configurable text color
    return f"""
    <html>
        <head><title>Hello App</title></head>
        <body style="text-align: center; font-family: Arial, sans-serif;">
            <h1 style="color: {color};">Hello, my name is: {hostname}</h1>
            <h2 style="color: {color};">Environment: <strong>{environment}</strong></h2>
        </body>
    </html>
    """


if __name__ == "__main__":
    # Run the app on port 8080
    app.run(host="0.0.0.0", port=8080)
