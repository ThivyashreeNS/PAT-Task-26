"""test_imdb_search.py"""
import pytest
from Task_26.Pages.ImdbSearch import ImdbSearch

def test_imdb_search():
    obj = ImdbSearch()
    expected_url = "https://www.imdb.com/search/name/?name=Jackie%20Chan&birth_monthday=04-07&gender=male"
    result_url = obj.imdb_search()
    assert expected_url == result_url
    print("Success: Imdb Search")
    obj.close_driver()