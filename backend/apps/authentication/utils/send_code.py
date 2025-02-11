import requests

headers = {
        'Content-Type': 'application/json',
    }
def send_code(phone, code):
    url = "https://brainy-hummingbird-gbteam-4548a45b.koyeb.app/send_code/"
    data={
        "user_id": phone,
        "data": code
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Произошла ошибка: {e}')
        print(f'Статус: {response.status_code}, Тело ответа: {response.text}')
        return None
    
