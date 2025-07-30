from unittest.mock import patch, MagicMock


@patch('app.services.db.session.commit')
@patch('app.services.db.session.delete')
@patch('app.services.get_album_by_id')
def test_delete_album_with_valid_id(mock_get_album_by_id, mock_delete, mock_commit, client):
    mock_album = MagicMock()
    mock_album.id = 1
    mock_album.artist = 'Peter Gabriel'
    mock_album.title = 'So'
    mock_get_album_by_id.return_value = mock_album

    response = client.delete('/albums/1')

    assert response.status_code == 200
    assert response.json["message"] == "Successfully deleted album with id: 1 Peter Gabriel So"
    mock_delete.assert_called_once_with(mock_album)
    mock_commit.assert_called_once()

@patch('app.services.get_album_by_id')
def test_delete_album_with_invalid_id(mock_get_album_by_id, client):
    mock_get_album_by_id.return_value = None

    response = client.delete('/albums/999')

    assert response.status_code == 404
    assert response.json["error"] == "The album with requested id does not exist."