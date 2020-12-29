import pytest
import pandas as pd
from app.app import app, cagr


def test_non_empty_data():
    data = pd.read_csv('../app/dataset.csv')
    assert data.empty is False


def test_empty_data():
    data = pd.read_csv('data.csv')
    assert data.empty is True


def test_home_page():
    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"The app is up and running" in response.data


def test_cagr_zero():
    with pytest.raises(ZeroDivisionError):
        cagr(0, 1, 1)


def test_cagr_ok():
    assert round(cagr(9000, 13000, 3), 2) == 0.13


def test_get_data_empty():
    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/get_data')
        assert b"Please, provide the id!" in response.data
