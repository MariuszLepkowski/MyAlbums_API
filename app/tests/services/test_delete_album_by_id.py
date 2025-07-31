from unittest.mock import patch, MagicMock
from app.services import delete_album_by_id


@patch('app.services.get_album_by_id')
@patch('app.services.db.session')
def test_delete_album_by_id_found(mock_session, mock_get_album):
    # Symulujemy istnienie albumu
    mock_album = MagicMock()
    mock_get_album.return_value = mock_album

    result = delete_album_by_id(5)

    assert result == mock_album
    mock_session.delete.assert_called_once_with(mock_album)
    mock_session.commit.assert_called_once()