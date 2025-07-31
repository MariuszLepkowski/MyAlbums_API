from unittest.mock import patch, MagicMock
from app.services import update_album_partially


@patch('app.services.get_album_by_id')
@patch('app.services.db.session.commit')
def test_update_album_partially_artist_only(mock_commit, mock_get_album):
    mock_album = MagicMock()
    mock_album.artist = "Old Artist"
    mock_album.title = "Same Title"
    mock_get_album.return_value = mock_album

    result = update_album_partially(1, {"artist": "New Artist"})

    assert result.artist == "New Artist"
    assert result.title == "Same Title"
    mock_commit.assert_called_once()
