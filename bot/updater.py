import time

import requests


class Updater:
    def __init__(self, token: str) -> None:
        self.token: str = token
        self.last_update_id: int | None = None

    def get_updates(self) -> list[dict]:
        payload = {"offset": self.last_update_id}
        response = requests.get(
            f"https://api.telegram.org/bot{self.token}/getUpdates", params=payload
        )
        if response.status_code == 200:
            data = response.json()
            return data["result"]

        return []

    def start_polling(self) -> None:
        while True:
            for update in self.get_updates():
                print(update["update_id"])

                self.last_update_id = update["update_id"] + 1

            time.sleep(0.3)
