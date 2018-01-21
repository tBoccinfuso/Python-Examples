# Startup Python Script Example
import  os
 
# Set our folder paths
dir = 'WebApp'
cssFolder = '/css'
jsFolder = '/javascript'

# Create the folder if it doesn't exist.
if not os.path.exists(dir):
    os.makedirs(dir)

# Create css folder
if not os.path.exists(dir + '/' + cssFolder):
    os.makedirs(dir + '/' + cssFolder)

# Create javascript folder
if not os.path.exists(dir + '/' + jsFolder):
    os.makedirs(dir + '/' + jsFolder)


# Setting up our html file
html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="css/style.css">
        <title>Document</title>
    </head>
    <body>

    <script src='javascript/index.js'></script>
    </body>
    </html>
    '''
# Create and write our html string to a new file called index.html
Html_file= open("WebApp/index.html","w")
Html_file.write(html)
Html_file.close()

# Create index.js file by joining the new file to our Javascript directory
with open(os.path.join(dir + '/' + jsFolder, 'index.js'), 'w'):
    pass

# Create style.css file by joining the new file to our CSS directory
with open(os.path.join(dir + '/' + cssFolder, 'style.css'), 'w'):
    pass

# Thomas Boccinfuso - www.tboccinfuso.com / www.twitter.com/BoccinfusoT