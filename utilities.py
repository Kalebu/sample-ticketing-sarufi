def build_menu(body: str, button: str, title: str, rows: list):
    return {
        "send_button": {
            "body": body,
            "action": {
                "button": button,
                "sections": [
                    {
                        "title": title,
                        "rows": rows,
                    }
                ],
            },
        }
    }
