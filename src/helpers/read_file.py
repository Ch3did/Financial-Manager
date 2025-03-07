import re


def sgml_to_xml(ofx_data):
    # Transforma tags SGML em XML
    ofx_data = re.sub(r"<(\w+?)>", r"<\1>", ofx_data)
    ofx_data = re.sub(r"</(\w+?)>", r"</\1>", ofx_data)
    return ofx_data


def read_ofx_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        ofx_data = file.read()

    if "OFXHEADER" in ofx_data:
        match = re.search(r"<OFX>", ofx_data, re.S)
        if match:
            ofx_data = sgml_to_xml(ofx_data[match.start() :])
        else:
            raise ValueError("Arquivo OFX inválido: Não contém <OFX>")

    return ofx_data
