data = """Some random
text of whatever form.
Bla bla bla."""
def printDataAsData(data):
    print('data = ""' + '"' + data + '""' + '"')
def printDataAsProgram(data):
    print(data)
printDataAsData(data)
printDataAsProgram(data)
print(2+2)
