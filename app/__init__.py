from flask import Flask, jsonify,send_from_directory,request, zipfile

from .modules.image import utils 

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000



@app.get('/files')
def list_all_images():
    images_list = utils.list_all()
    return jsonify(images_list), 200


@app.get('/files/<string:extension>')
def list_image_by_extension(extension:str):
    images_list = utils.list_all()
    output = []
    for image in images_list: 
        if image.split(".")[-1] == extension:
            output.append(image)
    return jsonify(output), 200


#fazer o dowload de um arquivo existente
@app.get('/download/<string:file_name>')
def download_image(file_name):
    images_list = utils.list_all() 
    if file_name in images_list:
       return send_from_directory(directory="../images", path=file_name, as_attachment=True), 200 
    else:
        return {'message': 'o arquivo não existe, insira um arquivo válido'} , 404


#dowload das imagens em outros formatos    

# upload das imagens 
@app.post('/upload')
def upload_image(): 
    files_list = []

    for file in request.files:
        filename= utils.save_image(request.files[file]) 
        files_list.append(filename)

    return jsonify(files_list)

