from datetime import datetime


def log_result(message):

    timestamp = datetime.now().strftime("%H:%M:%S")

    formatted_message = f"[{timestamp}] {message}"

    with open("dns_logs.txt", "a") as file:
        file.write(formatted_message + "\n")