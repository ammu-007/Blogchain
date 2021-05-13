from django.shortcuts import render
from BTC.ml_model import predict_result

# Create your views here.
def predict(request):
    return render(request, "BTC/predict.html")


def prediction(request):
    return render(request, "BTC/prediction.html", {})


def result(request):
    var1 = float(request.GET["transactions"])
    var2 = float(request.GET["fee"])
    var3 = float(request.GET["trends"])
    var4 = float(request.GET["gold"])
    var5 = float(request.GET["sp"])
    var6 = float(request.GET["oil"])
    var7 = float(request.GET["m2"])
    l = [var1, var2, var3, var4, var5, var6, var7]
    print(l)
    price = f"The predicted price is {predict_result(l)}"
    return render(request, "BTC/prediction.html", {"result": price})