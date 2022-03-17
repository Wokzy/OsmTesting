import pytest
from modules.Osm_api import OsmApi


@pytest.mark.parametrize("lat, lon, location", [('55.0282171', '82.9234509', 'Novosibirsk'), ('53.0199838', '158.6471356', 'Петропавловск-Камчатский'), ('59.9949054', '30.3311633', 'Санкт-Петербург, Большой Сампсониевский 60А'), ('55.7504461', '37.6174943', 'Moscow')])
def test_direct_geocoding_positive(lat, lon, location):
    print('Checking direct_request')
    lat_resp, lon_resp, status_code = OsmApi(lat, lon, location).direct_request('json')
    assert 200 == status_code
    assert lat == lat_resp
    assert lon == lon_resp


@pytest.mark.parametrize("lat, lon, location", [('', '82.9234509', 'Novosibirsk 53'),('','','1'),('55.0282171','82.9234509','asdfasfasfd'), ('5', '3', 'Санкт-Петербург, Большой Сампсониевский 60А'), ('55.7504461', '37.6174943', 'London')])
def test_direct_geocoding_negativ(lat, lon, location):
    lat_resp, lon_resp, status_code = OsmApi(lat, lon, location).direct_request('json')
    assert 200 == status_code
    assert lat != lat_resp
    assert lon != lon_resp

@pytest.mark.parametrize("lat, lon, location", [('55.0282171', '82.9234509', 'Novosibirsk'), ('53.0199838', '158.6471356', 'Петропавловск-Камчатский'), ('59.9949054', '30.3311633', 'Санкт-Петербург, Большой Сампсониевский 60А'), ('55.7504461', '37.6174943', 'Moscow')])
def test_direct_geocoding_positive_xml(lat, lon, location):
    print('Checking direct_request')
    lat_resp, lon_resp, status_code = OsmApi(lat, lon, location).direct_request('xml')
    assert 200 == status_code
    assert lat == lat_resp
    assert lon == lon_resp


@pytest.mark.parametrize("lat, lon, location", [('', '82.9234509', 'Novosibirsk 53'),('','','1'),('55.0282171','82.9234509','asdfasfasfd'), ('55.7504461', '37.6174943', 'Kiev'), ('5', '3', 'Санкт-Петербург, Большой Сампсониевский 60А')])
def test_direct_geocoding_negativ_xml(lat, lon, location):
    lat_resp, lon_resp, status_code = OsmApi(lat, lon, location).direct_request('xml')
    assert 200 == status_code
    assert lat != lat_resp
    assert lon != lon_resp