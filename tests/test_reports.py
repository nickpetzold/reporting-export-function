import json
from unittest import mock

from app import app

JSON_STR = '{"organization":"Arsenal FC","reported_at":"2018-11-24","created_at":"2010-12-25","inventory":[{"name":"football","price":"100.00"},{"name":"goal","price":"5000.00"}]}'
JSON_DATA = json.loads(JSON_STR)

@mock.patch("app.routes.get_data_for_report_id", return_value=JSON_DATA)
def test_pdf_report(mocked_data_function):
    report_id = 1
    response = app.test_client().get(
        f"/report_pdf/{report_id}"
    )
    assert response._status_code == 200
    headers = dict(response.headers)
    assert headers["Content-type"] == "application/pdf"
    assert headers["Content-Disposition"] == f"inline; filename=report_{report_id}.pdf"
    mocked_data_function.assert_called_once_with("1")


@mock.patch("app.routes.get_data_for_report_id", return_value=JSON_DATA)
def test_xml_report(mocked_data_function):
    report_id = 1
    response = app.test_client().get(
        f"/report_xml/{report_id}"
    )
    assert response._status_code == 200
    headers = dict(response.headers)
    assert headers["Content-type"] == "text/xml; charset=utf-8"
    mocked_data_function.assert_called_once_with("1")