def test_booking_past_competition(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Spring Festival', 'club': 'She Lifts', 'places': '12'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "You cannot purchase places from past competition" in data
