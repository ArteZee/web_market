from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

product_data = [{
        "id": 1,
        "product": "Wall E",
        "slug": "wall-e",
        "available": False,
        "description": "The robot WALL E has been diligently working on the deserted Earth year after year, cleaning our planet from mountains of garbage,"
                       "which people who flew into space left behind. He has no idea what will happen very soon"
                       "incredible events through which he will meet friends, rise to the stars and even be able to change to "
                       "to the best of their former owners, who completely forgot their native Earth",
        "price": 50_000.00,
    },
    {
            "id": 2,
            "product": "R2D2",
            "slug": "r2d2",
            "available": True,
            "description": "R2 is barrel shaped with a rotating dome acting as its head and including "
                           "a single eye. It has three props that allow it to walk, and each one has a wheel."
                           "Unlike his fellow protocol droid C-3PO, R2-D2 does not talk, but communicates via"
                           "sequences of bleeps, whistles, and trills that C-3PO can translate. It appears that "
                           "his masters also understand what he wants to say. Also, when connected to a fighter, R2-D2 can"
                           "communicate with the pilot by typing your lines on the monitor.",
            "price": 75_999.99
    },
    {
            "id": 3,
            "product": "C3PO",
            "slug": "c3po",
            "available": True,
            "description": "The constant companion of R2D2 is the protocol robot C3PO, who is known to speak two million languages,"
                           "including the language of the R2D2 robot. Looks stupid and sometimes cowardly, which does not prevent him from arousing sympathy."
                           "Albeit smaller than his vacuum cleaner partner.",
            "price": 100_000.99
    },
    {
        "id": 4,
        "product": "Bender",
        "slug": "bender",
        "available": True,
        "description": "Rough and alcoholic, lover of cigars and foul language, Bender is, however, sympathy."
                       "Maybe the whole point is that he always remains himself, says what he thinks"
                       "(except for those frequent times when he lies) and does not try to be someone else",
        "price": 99_999.00
    }]


def product_1(request: HttpRequest, ) -> HttpResponse:
    return render(request, "product_1.html",product_data[0])


def product_2(request: HttpRequest, ) -> HttpResponse:
    return render(request, "product_2.html", product_data[1])


def product_3(request: HttpRequest, ) -> HttpResponse:
    return render(request, "product_3.html", product_data[2])


def product_4(request: HttpRequest, ) -> HttpResponse:
    return render(request, "product_4.html", product_data[3])
