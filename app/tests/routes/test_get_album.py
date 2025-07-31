from unittest.mock import patch, MagicMock


@patch('app.routes.get_album_by_id')
def test_pick_album_by_valid_id(mock_get_album_by_id, client):
    mock_album = MagicMock()
    mock_album.id = 1
    mock_album.artist = "Peter Gabriel"
    mock_album.title = "So"

    mock_get_album_by_id.return_value = mock_album

    response = client.get('/albums/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'artist': "Peter Gabriel",
        'title': "So",
    }

@patch('app.routes.get_album_by_id')
def test_pick_album_by_invalid_id(mock_get_album_by_id, client):
    mock_get_album_by_id.return_value = None

    response = client.get('/albums/3')

    assert response.status_code == 404
    assert response.json['error'] == "The album with requested id does not exist."


@patch('app.routes.get_all_albums')
def test_all_albums(mock_get_all_albums, client):
    mock_album1 = MagicMock()
    mock_album1.id = 1
    mock_album1.artist = "Peter Gabriel"
    mock_album1.title = "So"

    mock_album2 = MagicMock()
    mock_album2.id = 2
    mock_album2.artist = "Peter Gabriel"
    mock_album2.title = "Us"

    mock_get_all_albums.return_value = [mock_album1, mock_album2]

    response = client.get('/albums/')

    assert response.status_code == 200
    assert response.json == [
        {
            "artist": "Peter Gabriel",
            "id": 1,
            "title": "So"
        },
        {
            "artist": "Peter Gabriel",
            "id": 2,
            "title": "Us"
        },
    ]

@patch('app.routes.get_random_album')
def test_pick_random_album(mock_get_random_album, client):
    mock_album = MagicMock()
    mock_album.id = 42
    mock_album.artist = "Prince"
    mock_album.title = "Purple Rain"

    mock_get_random_album.return_value = mock_album

    response = client.get('/albums/random')

    assert response.status_code == 200
    assert response.json == {
        "id": 42,
        "artist": "Prince",
        "title": "Purple Rain"
    }

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to MyAlbums_API!"}

