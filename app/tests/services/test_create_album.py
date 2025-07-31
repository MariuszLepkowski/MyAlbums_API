from unittest.mock import patch, MagicMock
from app.services import create_album

"""
def create_album(data):
    new_album = Album(artist=data["artist"], title=data["title"])
    db.session.add(new_album)
    db.session.commit()
    return new_album
    
    Tworzy nową instancję Album

    Dodaje ją do sesji (czyli mówi SQLAlchemy: „chcę to zapisać”)

    Komituje (czyli faktycznie zapisuje w bazie)

    Zwraca ten obiekt

 Co chcemy przetestować?

    Że został stworzony obiekt Album z danymi

    Że został dodany do sesji

    Że został zapisany przez commit()

    I że funkcja zwraca dokładnie ten obiekt
"""

@patch('app.services.db.session') # podmieniamy prawdziwą sesję bazy na atrapę (mock)
def test_create_album(mock_session):
    # Tworzymy atrapę danych wejściowych – takie dane mogłyby przyjść w zapytaniu POST
    mock_data = {
        "artist": "Peter Gabriel",
        "title": "So"
    }

    #podmieniamy prawdziwą klasę Album na atrapę tej klasy, czyli mock_album_class
    with patch('app.services.Album') as mock_album_class:
        mock_album_instance = MagicMock() #tworzymy sztuczną instancję fikcyjnej klasy mock_album_class
        mock_album_class.return_value = mock_album_instance

        # wywołujemy funkcję, którą testujemy
        result = create_album(mock_data)

        # Sprawdzamy, czy obiekt został dodany do sesji i zapisany do bazy
        mock_session.add.assert_called_once_with(mock_album_instance)
        mock_session.commit.assert_called_once()

        assert result == mock_album_instance




