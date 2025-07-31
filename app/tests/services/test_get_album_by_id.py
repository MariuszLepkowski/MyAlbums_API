from app.services import (
    get_album_by_id
)

from sqlalchemy.exc import NoResultFound
from unittest.mock import patch, MagicMock


@patch('app.services.db.session.execute')
def test_get_album_by_id_found(mock_execute):
    mock_result = MagicMock()
    mock_album = MagicMock()
    mock_result.scalar_one.return_value = mock_album
    mock_execute.return_value = mock_result

    album = get_album_by_id(1)

    assert album == mock_album
    mock_execute.assert_called_once()
    mock_result.scalar_one.assert_called_once_with()

@patch('app.services.db.session.execute')
def test_get_album_by_id_not_found(mock_execute):
    mock_result = MagicMock()
    mock_result.scalar_one.side_effect = NoResultFound
    mock_execute.return_value = mock_result

    album = get_album_by_id(999)

    assert album is None
    mock_execute.assert_called_once()
    mock_result.scalar_one.assert_called_once_with()