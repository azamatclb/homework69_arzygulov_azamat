# Create your views here.

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == "GET":
        return HttpResponse()
    else:
        return HttpResponseNotAllowed('')


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@require_http_methods(["POST"])
def add(request):
    try:
        data = json.loads(request.body)
        A = data.get("A")
        B = data.get("B")

        if not (is_valid_number(A) and is_valid_number(B)):
            return HttpResponseBadRequest(JsonResponse({"error": "Input must be numbers"}))

        result = float(A) + float(B)
        return JsonResponse({"answer": result})

    except json.JSONDecodeError:
        return HttpResponseBadRequest(JsonResponse({"error": "Wrong JSON"}))


@require_http_methods(["POST"])
def subtract(request):
    try:
        data = json.loads(request.body)
        A = data.get("A")
        B = data.get("B")

        if not (is_valid_number(A) and is_valid_number(B)):
            return HttpResponseBadRequest(JsonResponse({"error": "Input must be numbers"}))

        result = float(A) - float(B)
        return JsonResponse({"answer": result})

    except json.JSONDecodeError:
        return HttpResponseBadRequest(JsonResponse({"error": "Wrong JSON"}))


@require_http_methods(["POST"])
def multiply(request):
    try:
        data = json.loads(request.body)
        A = data.get("A")
        B = data.get("B")

        if not (is_valid_number(A) and is_valid_number(B)):
            return HttpResponseBadRequest(JsonResponse({"error": "Input must be numbers"}))

        result = float(A) * float(B)
        return JsonResponse({"answer": result})

    except json.JSONDecodeError:
        return HttpResponseBadRequest(JsonResponse({"error": "Wrong JSON!"}))


@require_http_methods(["POST"])
def divide(request):
    try:
        data = json.loads(request.body)
        A = data.get("A")
        B = data.get("B")

        if not (is_valid_number(A) and is_valid_number(B)):
            return HttpResponseBadRequest(JsonResponse({"error": "Input must be numbers"}))

        if float(B) == 0:
            return HttpResponseBadRequest(JsonResponse({"error": "Can't divide by zero"}))

        result = float(A) / float(B)
        return JsonResponse({"answer": result})

    except json.JSONDecodeError:
        return HttpResponseBadRequest(JsonResponse({"error": "Wrong JSON!"}))
