def test_booking_successful(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Openclassrooms', 'club': 'Simply Lift', 'places': '12'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "Great-booking complete!" in data


def test_booking_zero_or_less_places(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Openclassrooms', 'club': 'She Lifts', 'places': '0'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "You must at least buy one place" in data


def test_booking_more_places_than_available(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Openclassrooms small', 'club': 'Iron Temple', 'places': '4'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "You cannot purchase more places than available." in data
