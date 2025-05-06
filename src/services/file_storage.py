def save_pdf(file, upload_folder):
    import os

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_location = os.path.join(upload_folder, file.filename)

    with open(file_location, "wb") as f:
        f.write(file.file.read())

    return file_location