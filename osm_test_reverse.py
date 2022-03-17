import pytest
from modules.Osm_api import OsmApi


@pytest.mark.parametrize("lat, lon, location, zoom", [('54.8009038', '55.1994565', 'Алексеевский сельсовет, Blagovarsky District, Bashkortostan, Volga Federal District, Russia', '18'), ('20.7580586', '-156.3105232', 'Maui County, Hawaii, United States', '18'), ('56.01223', '92.86902', 'Siberian State Technological University, проспект Мира, Центральный район, Krasnoyarsk, Krasnoyarsk Urban Okrug, Krasnoyarsk Krai, Siberian Federal District, 660000, Russia', '18'), ('56.0354965', '93.12687458384087', '73, улица Кирова, Beryozovka, городское поселение Берёзовка, Beryozovsky Rayon, Krasnoyarsk Krai, Siberian Federal District, 662520, Russia', '18')])
def test_reverse_geocoding(lat, lon, location, zoom):
    loc_resp, status_code = OsmApi(lat, lon, location, zoom).reverse_request('json')
    assert 200 == status_code
    assert location != loc_resp

@pytest.mark.parametrize("lat, lon, location, zoom", [('54.8009038', '55.1994565', 'Алексеевский сельсовет, Blagovarsky District, Bashkortostan, Volga Federal District, Russia', '18'), ('20.7580586', '-156.3105232', 'Maui County, Hawaii, United States', '18'), ('56.01223', '92.86902', 'Siberian State Technological University, проспект Мира, Центральный район, Krasnoyarsk, Krasnoyarsk Urban Okrug, Krasnoyarsk Krai, Siberian Federal District, 660000, Russia', '18'), ('56.0354965', '93.12687458384087', '73, улица Кирова, Beryozovka, городское поселение Берёзовка, Beryozovsky Rayon, Krasnoyarsk Krai, Siberian Federal District, 662520, Russia', '18')])
def test_reverse_geocoding_xml(lat, lon, location, zoom):
    loc_resp, status_code = OsmApi(lat, lon, location, zoom).reverse_request('xml')
    assert 200 == status_code
    assert location != loc_resp