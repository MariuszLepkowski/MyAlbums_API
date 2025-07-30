from unittest.mock import patch, MagicMock


@patch('app.services.get_album_by_id')
def test_put_album_with_valid_data(mock_get_album_by_id, client):
    mock_album = MagicMock()
    mock_album.id = 1
    mock_album.artist = 'Peter Gabriel'
    mock_album.title = 'So'
    mock_get_album_by_id.return_value = mock_album

    response = client.put('albums/1', json={
        "artist": "Sting",
        "title": "Soul Cages"
    })

    assert response.status_code == 200
    assert response.json['message'] == "Successfully updated album with id: 1"


@patch('app.services.get_album_by_id')
def test_put_album_with_empty_data(mock_get_album_by_id, client):
    mock_album = MagicMock()
    mock_album.id = 1
    mock_album.artist = 'Peter Gabriel'
    mock_album.title = 'So'
    mock_get_album_by_id.return_value = mock_album

    response = client.put('albums/1', json={})

    assert response.status_code == 400
    assert response.json['error'] == "No input data provided"

@patch('app.services.get_album_by_id')
def test_put_album_with_empty_values(mock_get_album_by_id, client):
    mock_album = MagicMock()
    mock_album.id = 1
    mock_album.artist = 'Peter Gabriel'
    mock_album.title = 'So'
    mock_get_album_by_id.return_value = mock_album

    response = client.put('/albums/1', json={
        "artist": "",
        "title": ""
    })

    assert response.status_code == 400
    assert response.json["error"] == "Empty values for: artist, title"

@patch('app.services.get_album_by_id')
def test_put_album_with_empty_keys(mock_get_album_by_id, client):
    mock_album = MagicMock()
    mock_album.id = 1
    mock_album.artist = 'Peter Gabriel'
    mock_album.title = 'So'
    mock_get_album_by_id.return_value = mock_album

    response = client.put('/albums/1', json={
        "artist": "Sting",
    })

    assert response.status_code == 400
    assert response.json["error"] == "Missing keys: title"


@patch('app.services.get_album_by_id')
def test_put_album_with_wrong_id(mock_get_album_by_id, client):
    mock_get_album_by_id.return_value = None

    response = client.put('/albums/3', json={
        "artist": "Sting",
        "title": "Soul Cages"
    })

    assert response.status_code == 404
    assert response.json["error"] == "The album with requested id does not exist."