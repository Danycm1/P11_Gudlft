def test_login_with_wrong_email(client):
    response = client.post('/showSummary', data={'email': 'wrong@example.com'}, follow_redirects=True)

    data = response.data.decode()
    assert response.status_code == 200
    assert "Email is invalid. Please try again." in data


def test_login_with_correct_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)

    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome," in data
