import order_functions
# Юлия Осина 27 когорта — Финальный проект. Инженер по тестированию плюс

def test_get_order():
    new_order_response = order_functions.post_new_order()
    track = new_order_response.json().get("track")
    
    order_response = order_functions.get_order_by_track(track)

    assert order_response.status_code == 200