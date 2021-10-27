from flask import Flask, jsonify,send_from_directory,request

from .kenzie import image

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000


@app.get('/download-zip')
def download_dir_as_zip():
    check_all_repos = image.check_if_empty_repo_exist()
    zip_file = str(zip(range(3), [1,2,3]))

    with open('./images/example.zip','a') as f:
        f.write(zip_file)
        f.write("\n")

    if check_all_repos == False:
        send_from_directory(directory="../images", path='example.zip', as_attachment=True), 404 
        print(request.headers)
        return {"message": "erro 404"}


@app.get('/files')
def list_all_images():
    images_list = image.list_all_images()
    return jsonify(images_list), 200


@app.get('/files/<string:extension>')
def list_image_by_extension(extension:str):
    images_list = image.list_all_images()
    output = []
    for imagens in images_list: 
        if imagens.split(".")[-1] == extension:
            output.append(imagens)
    return jsonify(output), 200


@app.get('/download/<string:file_name>')
def download_image(file_name):
    images_list = image.list_all_images() 
    if file_name in images_list:
       return send_from_directory(directory="../images", path=file_name, as_attachment=True), 200 
    else:
        return {'message': 'o arquivo não existe, insira um arquivo válido'} , 404







#fazer o dowload de um arquivo existente



#dowload das imagens em outros formatos    

# upload das imagens 
@app.post('/upload')
def upload_image(): 
    files_list = []

    for file in request.files:
        filename= utils.save_image(request.files[file]) 
        files_list.append(filename)

    return jsonify(files_list)

