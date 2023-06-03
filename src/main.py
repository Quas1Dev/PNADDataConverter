import xlrd
import Variable

# Open the workbook
workbook = xlrd.open_workbook("../data/dicionario_pessoas.xls")
sheet = workbook.sheet_by_index(0)

# Print information about the sheet
print(f"Name {sheet.name}")
print(f"Número de linhas {sheet.nrows}")
print(f"Número de colunas {sheet.ncols}")

variables = []

newVar = None
for idx, line in enumerate(sheet.get_rows()):
    print(line)
    firstCell = line[0]

    # Check if the first cell type is a Number
    if firstCell.ctype == 2:
    	# Add new Variable object created in the previous round 
    	# of iteration
        if newVar:
            variables.append(newVar)

        # Extract values from the line to create a new Variable
        firstPosition = line[0].value
        size = line[1].value
        code = line[2].value
        description = line[4].value

        newVar = Variable(firstPosition, size, code, description)

        # Extract category information
        categoryType = line[5].value
        categoryDescType = line[6].value

        # Add category to the newVar
        newVar.addCategory({
            'categoryType': categoryType,
            'vategoryDescType': categoryDescType
        })
    else:
        if newVar:
            # Extract category information when the first cell type is not Number.
            categoryType = line[5].value
            categoryDescType = line[6].value
            newVar.addCategory({
                'categoryType': categoryType,
                'vategoryDescType': categoryDescType
            })

    # Break the loop after processing 50 rows
    if idx > 50:
        break

print(f"Total of variables {len(variables)}")
for variable in variables:
    print(variable)
    for category in variable.category:
        print(f"\t {category}")
