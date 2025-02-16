import requests

headers = {
        'Content-Type': 'application/json',
    }
def send_code(phone, code):
    url = "https://brainy-hummingbird-gbteam-4548a45b.koyeb.app/send_code/"
    json={
        "user_id": phone,
        "data": code
    }
    try:
        response = requests.post(url, json=json, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Произошла ошибка: {e}')
        print(f'Статус: {response.status_code}, Тело ответа: {response.text}')
        return None
    
print(send_code(phone="998881836222", code="123456"))



"""
order.json

{
    "total_price": 120000,
    "user_id": 1,
    "restaurant": 3
    "2": {
        "id": 2,
        "name": "Burger",
        "price": 15000,
        "quantity": 6,
        "total_price": 90000
    },
    "1": {
        "id": 1,
        "name": "Pizza",
        "price": 15000,
        "quantity": 2,
        "total_price": 30000
    }
}



"""

{
    "order": {
        "id" : 1,
        "created_at" : "date-time",
        "updated_at" : "date-time",
        "products" : [ {
            "id": 1,
            "price": 12000,
            "quantity": 2,
            "total_price": 24000
        },
        {
            "id": 2,
            "price": 10000,
            "quantity": 2,
            "total_price":20000
        },
        {
            "id": 3,
            "price": 5000,
            "quantity": 2,
            "total_price": 10000
        }
    ],
        "total_price": 54000,
        "lat": "647328413948",
        "long": "23678492965728",
        "user_id": 1,
        "restaurant":3

    }
}