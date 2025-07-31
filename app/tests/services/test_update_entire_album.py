from unittest.mock import patch, MagicMock
from app.services import update_entire_album


@patch('app.services.get_album_by_id')
@patch('app.services.db.session.commit')
def test_update_entire_album_success(mock_commit, mock_get_album):
    # Symulujemy istniejący album
    mock_album = MagicMock()
    mock_get_album.return_value = mock_album

    data = {"artist": "Pink Floyd", "title": "The Wall"}
    result = update_entire_album(1, data)

    assert result == mock_album
    assert mock_album.artist == "Pink Floyd"
    assert mock_album.title == "The Wall"
    mock_commit.assert_called_once()
