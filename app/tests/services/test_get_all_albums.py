from unittest.mock import patch, MagicMock
from app.services import get_all_albums


@patch('app.services.db.session.execute')
def test_get_all_albums(mock_execute):
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = ['album1, album2']
    """
    mock_execute.return_value → symuluje to, co zwraca db.session.execute(...)

    .scalars.return_value = mock_scalars → symuluje .scalars()

    .all.return_value = [...] → symuluje .all()

    """
    mock_execute.return_value.scalars.return_value = mock_scalars

    albums = get_all_albums()

    assert albums == ['album1, album2']
    mock_execute.assert_called_once()


