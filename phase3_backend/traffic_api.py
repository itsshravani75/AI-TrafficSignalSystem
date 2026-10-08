import requests


BACKEND_URL = "http://127.0.0.1:5000/api/traffic"


def send_traffic_data(
    traffic_counts,
    waiting_times,
    next_green,
    signal_times
):
    data = {
        "vehicle_counts": traffic_counts,
        "waiting_times": waiting_times,
        "next_green": next_green,
        "green_times": signal_times
    }

    try:
        response = requests.post(
            BACKEND_URL,
            json=data,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Backend connection error:", error)
        return None