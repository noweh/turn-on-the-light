with open('../README.md', 'r') as file:
    fileData = file.read()
    if 'Power ON' in fileData:
        # turn on the lights
        fileData = fileData.replace('power-on.png', 'power-off.png')
        fileData = fileData.replace('Power ON', 'Power OFF')
        fileData = fileData.replace('bulb-on.png', 'bulb-off.png')
        fileData = fileData.replace('Bulb ON', 'Bulb OFF')
    else:
        # turn off the lights
        fileData = fileData.replace('power-off.png', 'power-on.png')
        fileData = fileData.replace('Power OFF', 'Power ON')
        fileData = fileData.replace('bulb-off.png', 'bulb-on.png')
        fileData = fileData.replace('Bulb OFF', 'Bulb ON')

with open('../README.md', 'w') as file:
    file.write(fileData)