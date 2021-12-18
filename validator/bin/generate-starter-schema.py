import xlrd
import json

filename = ("schema/FEC_Format_v8.3.0.1.xlsx")

wb = xlrd.open_workbook(filename)
sheet = wb.sheet_by_index(18) # Form 3X

# schema = {
#     "$schema": "http://json-schema.org/draft-07/schema#",
#     "$id": "https://github.com/mjtravers/fecfile-online-sandbox/blob/main/validator/schema/form3x.json",
#     "title": "FEC Form 3X",
#     "description": "Report of receipts and disbursements for other than an authorized committee.",
#     "type": "object",
#     "properties": {},
#     "additionalProperties": False,
#     "required": []
# }

print(sheet.nrows)
print(sheet.ncols)

# for col_num in range(sheet.ncols):
#     if (sheet.cell_value(0, col_num):
# 	print(sheet.cell_value(0, i))


        # "title": "FILER COMMITTEE ID NUMBER",
        # "description": "FEC ID number registered to this committee",
        # "type": "string",
        # "pattern": "^C[0-9]{8}$",
        # "minLength": 9,
        # "maxLength": 9,
        # "examples": ["C00123456"],
        # "fec_line": "2",
        # "fec_type": "A/N-9",
        # "fec_requiredErrorLevel": "error",
        # "fec_valueReference": None,
        # "fec_ruleReference": None
