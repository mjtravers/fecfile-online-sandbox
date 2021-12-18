import openpyxl
import json

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/mjtravers/fecfile-online-sandbox/blob/main/validator/schema/form3x.json",
    "title": "FEC Form 3X",
    "description": "Report of receipts and disbursements for other than an authorized committee.",
    "type": "object",
    "properties": {},
    "additionalProperties": False,
    "required": []
}

COL_SEQ = 0
FIELD_DESCRIPTION = 1
TYPE = 2
REQUIRED = 3
SAMPLE_DATA = 4
VALUE_REFERENCE = 5
RULE_REFERENCE = 6

filename = ("FEC_Format_v8.3.0.1.xlsx")
wb = openpyxl.load_workbook(filename)
ws = wb['F3X']

for row in ws.iter_rows(min_row=5, max_col=7, max_row=136, values_only=True):
    if not row[1] or row[0] == "--":
        continue
    print(row)

    prop = {}
    field_type = row[TYPE]
    token = row[FIELD_DESCRIPTION].replace(" ", "_").replace(".", "").replace("(", "").replace(")", "")

    prop["title"] = row[FIELD_DESCRIPTION]
    prop["description"] = ""

    if field_type.startswith("AMT-"):
        prop["type"] = "number"
        prop["minimum"] = 0
        prop["maximum"] = 999999999999
    if field_type.startswith("NUM-"):
        prop["type"] = "integer"
        prop["minimum"] = 0
        prop["maximum"] = 0
    if field_type.startswith("A/N-") or field_type.startswith("A-"):
        prop["type"] = "string"
        prop["minlength"] = 0
        prop["maxlength"] = 0
        prop["pattern"] = "^[A-z0-9]{0,0}$"

    if row[SAMPLE_DATA]:
        prop["examples"] = [row[SAMPLE_DATA]]

    prop["fec_line"] = "0"
    prop["fec_type"] = field_type

    if row[REQUIRED]:
        prop["fec_requiredErrorLevel"] = row[REQUIRED]
        if "error" in row[REQUIRED]:
            schema["required"].append(token)
    if row[VALUE_REFERENCE]:
        prop["fec_valueReference"] = row[VALUE_REFERENCE]
    if row[RULE_REFERENCE]:
        prop["fec_ruleReference"] = row[RULE_REFERENCE]

    if row[FIELD_DESCRIPTION] != None:
        schema["properties"][token] = prop

f = open("schema-out.json", "w")
f.write(json.dumps(schema))
f.close()