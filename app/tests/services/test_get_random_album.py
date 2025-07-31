from unittest.mock import patch, MagicMock
from app.services import get_random_album


@patch('app.services.get_all_albums')
@patch('app.services.random.choice')
def test_get_random_album(mock_choice, mock_get_all_albums):
    # Symulujemy 3 albumy w bazie
    mock_album_list = ['a1', 'a2', 'a3']
    mock_get_all_albums.return_value = mock_album_list

    # Symulujemy, że random.choice wybierze 'a2'
    mock_choice.return_value = 'a2'

    result = get_random_album()

    assert result == 'a2'
    mock_choice.assert_called_once_with(mock_album_list)
