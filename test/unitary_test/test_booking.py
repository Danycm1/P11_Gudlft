def test_booking_past_competition(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Spring Festival', 'club': 'She Lifts', 'places': '12'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "You cannot purchase places from past competition" in data


def test_booking_more_than_12_places(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Openclassrooms', 'club': 'Simply Lift', 'places': '13'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "You cannot purchase more than 12 places." in data


def test_deduce_points_from_club_when_booking_places(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Openclassrooms', 'club': 'Iron Temple', 'places': '5'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "Not enough points to purchase." in data
