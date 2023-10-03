import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

@pytest.mark.unit
@pytest.mark.high
def test_load():
    """Test load function """
    with open(f"arquivo_indesejado.txt", "w") as file_:
        file_.write("dados uteis somente para teste")
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'

@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function """
    with open(f"arquivo_indesejado.txt", "w") as file_:
        file_.write("dados uteis somente para teste")
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'