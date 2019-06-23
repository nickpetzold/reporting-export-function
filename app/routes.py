import json
import xml.etree.cElementTree as ET

import pdfkit
from flask import make_response, render_template

from app import app
from app.models import Report


def get_data_for_report_id(id):
    report = Report.query.get(id)
    json_str = report.type
    return json.loads(json_str)


@app.route("/report_pdf/<id>", methods=["GET"])
def report_query_pdf(id):
    filename = f"report_{id}.pdf"
    data = get_data_for_report_id(id)

    pdf_template = render_template("pdf_template.html", data=data)
    pdf = pdfkit.from_string(pdf_template, False)

    response = make_response(pdf)
    response.headers['Content-Disposition'] = f"inline; filename={filename}"
    response.headers['Content-type'] = 'application/pdf'
    return response


@app.route("/report_xml/<id>", methods=["GET"])
def report_query_xml(id):
    filename = f"report_{id}.pdf"
    data = get_data_for_report_id(id)

    report_element = ET.Element("report")

    ET.SubElement(report_element, "organization").text = data["organization"]
    ET.SubElement(report_element, "reported").text = data["reported_at"]
    ET.SubElement(report_element, "created").text = data["created_at"]

    for item in data["inventory"]:
        item_element = ET.SubElement(report_element, "item")
        ET.SubElement(item_element, "name").text = item["name"]
        ET.SubElement(item_element, "price").text = item["price"]

    report = ET.ElementTree(report_element)
    root = report.getroot()
    xml_string = ET.tostring(root, encoding='utf8', method='xml')

    response = make_response(xml_string)
    response.headers['Content-type'] = 'text/xml; charset=utf-8'
    return response

