from flask import Flask, jsonify,send_from_directory,request



from .kenzie import image

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000
# GET
#------------------------------------------------ LIST --------------------------------------
# objetivo : listar todos os arquivos 
@app.get('/files')
def list_files():
    dir_list = image.list_all_files() 
    files_list = []

    for files in dir_list:
        path = image.get_path(files)
        files_list.append(image.list_files(path))

    return dict(zip(dir_list,files_list)), 200

# objetivo : listar todos os arquivos de um determinado tipo
@app.get('/files/<string:extension>')
def list_image_by_extension(extension:str):
    dir_list = image.list_all_files()
    extension = image.get_extension(extension)
    output = []

    for files in dir_list: 
        if files == extension:
            path = image.get_path(files)
            lista = image.list_files(path)
            for images in lista:
                output.append(images)
        
    try:
        return jsonify(output), 200
    except:
        return {"message":f' A extensão {extension} nao existe'}, 404


#------------------------------------------------ DOWNLOAD --------------------------------------
# objetivo : download do arquivo solicitado em file_name 
@app.get('/download/<string:file_name>')
def download_image(file_name):
    extension = image.get_extension(file_name)
    path = image.get_path(extension) 

    try:
        return send_from_directory(directory=f"{path}", path=file_name, as_attachment=True), 200 
    except:
        return {"message":f' O arquivo {file_name} nao existe'}, 404


@app.get('/download-zip')
def download_dir_as_zip():
    extension = request.args.get('file_extension') 
    path = image.get_path(extension) 

    image.download_zip_files(extension) , 200 

    return send_from_directory(directory=f"../images", path=f"{extension}", as_attachment=True), 200 


#------------------------------------------------ UPLOAD 

@app.post('/upload')
def upload_image(): 
    files_list = []

    print(request.files)


    for file in request.files:
        filename= image.save_image(request.files[file]) 
        files_list.append(filename)

    

    return jsonify(files_list)

