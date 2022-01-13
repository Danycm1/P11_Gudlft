def test_deduce_points_from_club_when_booking_places(client):
    response = client.post('/purchasePlaces',
                           data={'competition': 'Spring Festival', 'club': 'Iron Temple', 'places': '5'})

    data = response.data.decode()
    assert response.status_code == 200
    assert "Not enough points to purchase." in data
