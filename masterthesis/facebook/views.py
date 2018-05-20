from django.shortcuts import render





#Function to enter the features of a post into the database
def setFeatures(request):
    if request.method == 'POST':
        if 'number_of_words' in request.POST:
            number_of_words = request.POST['number_of_words']
            post = Post(number_of_words = number_of_words)
            post.save()
            return HttpResponse("Success")

    return HttpResponse('FAIL!!!!!')
