from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def user_profile(request: HttpRequest, ) -> HttpResponse:
    """
    function return data of user to html
    :param request:
    :return:
    """
    user_data = {
        "user_nick": "ArteZee",
        "user_first_name": "Artem",
        "user_last_name": "Zubrytskyi",
        "user_height": 1.75,
        "user_age": 22,
        "user_education": "Second degree",
    }
    return render(request, "user_profile.html", user_data)
