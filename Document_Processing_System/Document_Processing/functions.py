def handle_uploaded_file(f):  
    with open('Document_Processing/static/images/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 