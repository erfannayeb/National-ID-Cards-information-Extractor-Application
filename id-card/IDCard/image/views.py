from django.shortcuts import render, redirect
from .forms import ImageForm
from card.models import Card
import os
import torch
import shutil
from ocr.OCR import ocr

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/image/best.pt', force_reload=True)
model.conf = 0.60


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uploaded_image_name = form.cleaned_data['image'].name
            print(uploaded_image_name)
            uploaded_image_name_path = f"./uploaded_images/{uploaded_image_name}"
            print(uploaded_image_name_path)
            uploaded = True
            shutil.rmtree('C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs')
            result(uploaded_image_name_path)


            detected_images_dir_BirthDate = 'C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs/detect/exp/crops/Birth Date'
            detected_images_dir_Name = 'C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs/detect/exp/crops/Name'
            detected_images_dir_LastName = 'C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs/detect/exp/crops/Last Name'
            detected_images_dir_Father = 'C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs/detect/exp/crops/Father'
            detected_images_dir_Validity = 'C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs/detect/exp/crops/Validity'
            detected_images_dir_Number = 'C:/Users/ASUS/Desktop/Bachelor/id-card/id-card/IDCard/runs/detect/exp/crops/Number'


            number = ocr(imagePath(detected_images_dir_Number))
            first_name = ocr(imagePath(detected_images_dir_Name))
            last_name = ocr(imagePath(detected_images_dir_LastName))
            birth_date = ocr(imagePath(detected_images_dir_BirthDate))
            father = ocr(imagePath(detected_images_dir_Father))
            expiration_date = ocr(imagePath(detected_images_dir_Validity))
            Card.objects.create(
                first_name=first_name,
                last_name=last_name,
                card_id=number,
                father_name=father,
                birth_data=birth_date,
                expiration_data=expiration_date
            )
            redirect("/user")
            #return render(request, 'upload_image.html', {'form': form, 'uploaded': uploaded})
            return redirect("/user")
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

# crop detected images
def result(path):
    results = model(path)  # inference
    #results.print()
    results.crop(save=True)
def imagePath(dir_path):
    detected_images_list = [os.path.join(dir_path, _file) for _file in
                                         os.listdir(dir_path)]
    return detected_images_list[0]





