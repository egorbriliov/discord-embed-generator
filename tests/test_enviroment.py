"""File with tests function enviroment."""
import pytest

from utils.enviroment import Enviroment


@pytest.mark.parametrize(
    'name',
    (
        pytest.param('TOKEN'),
        pytest.param('NEW', marks=pytest.mark.xfail(
            reason='New not in .env file'))
        )
    )
def test_enviroment(name: str):
    """Test Enviroment get method."""
    return Enviroment.get(name=name)
