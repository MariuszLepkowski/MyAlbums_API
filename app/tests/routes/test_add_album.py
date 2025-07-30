from unittest.mock import patch, MagicMock


@patch(target='app.routes.create_album')
def test_add_album_with_valid_data(mock_create_album, client):
    mock_album = MagicMock()
    mock_album.artist = "Peter Gabriel"
    mock_album.title = "So"

    mock_create_album.return_value = mock_album

    response = client.post('/albums/', json={
        "artist": "Peter Gabriel",
        "title": "So"
    })

    assert response.status_code == 201
    assert response.json["message"] == "Successfully added Peter Gabriel - So to the database."


@patch(target='app.routes.create_album')
def test_add_album_with_missing_keys(mock_create_album, client):
    mock_album = MagicMock()
    mock_album.artist = "Peter Gabriel"
    mock_album.title = "So"

    mock_create_album.return_value = mock_album

    response = client.post('/albums/', json={
        "artist": "Peter Gabriel",
    })

    assert response.status_code == 400
    assert response.json["error"] == "Missing keys: title"

@patch(target='app.routes.create_album')
def test_add_album_with_missing_values(mock_create_album, client):
    mock_album = MagicMock()
    mock_album.artist = ""
    mock_album.title = ""

    mock_create_album.return_value = mock_album

    response = client.post('/albums/', json={
        "artist": "",
        "title": ""
    })

    assert response.status_code == 400
    assert response.json["error"] == "Empty values for: artist, title"


@patch(target='app.routes.create_album')
def test_add_album_with_no_data(mock_create_album, client):
    mock_album = MagicMock()
    mock_album.artist = ""
    mock_album.title = ""

    mock_create_album.return_value = mock_album

    response = client.post('/albums/', json={})

    assert response.status_code == 400
    assert response.json["error"] == "No input data provided"
