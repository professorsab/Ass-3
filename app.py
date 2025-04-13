import os
import django
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import requests

# Django settings (NO SECRET_KEY needed)
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ],
)

django.setup()

# Views
@csrf_exempt
def predict_view(request):
    if request.method == 'POST':
        # Get user input from the form
        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))

        # Prepare the data to send to the prediction API
        data = {
            "fixed acidity": fixed_acidity,
            "volatile acidity": volatile_acidity,
            "citric acid": citric_acid,
            "residual sugar": residual_sugar,
            "chlorides": chlorides,
            "free sulfur dioxide": free_sulfur_dioxide,
            "total sulfur dioxide": total_sulfur_dioxide,
            "density": density,
            "pH": pH,
            "sulphates": sulphates,
            "alcohol": alcohol
        }

        try:
            response = requests.post(
                'https://55e9-104-196-142-66.ngrok-free.app/predict',  # Your public API
                json=data,
                headers={'Content-Type': 'application/json'}
            )
            prediction = response.json()
        except Exception as e:
            prediction = {'error': str(e)}

        return JsonResponse(prediction)

    return HttpResponse('''
        <h1>Wine Quality Predictor</h1>
        <form method="post">
            <label>Fixed Acidity:</label><br>
            <input type="number" step="0.1" name="fixed_acidity" required><br>

            <label>Volatile Acidity:</label><br>
            <input type="number" step="0.1" name="volatile_acidity" required><br>

            <label>Citric Acid:</label><br>
            <input type="number" step="0.1" name="citric_acid" required><br>

            <label>Residual Sugar:</label><br>
            <input type="number" step="0.1" name="residual_sugar" required><br>

            <label>Chlorides:</label><br>
            <input type="number" step="0.01" name="chlorides" required><br>

            <label>Free Sulfur Dioxide:</label><br>
            <input type="number" step="1" name="free_sulfur_dioxide" required><br>

            <label>Total Sulfur Dioxide:</label><br>
            <input type="number" step="1" name="total_sulfur_dioxide" required><br>

            <label>Density:</label><br>
            <input type="number" step="0.0001" name="density" required><br>

            <label>pH:</label><br>
            <input type="number" step="0.1" name="pH" required><br>

            <label>Sulphates:</label><br>
            <input type="number" step="0.1" name="sulphates" required><br>

            <label>Alcohol:</label><br>
            <input type="number" step="0.1" name="alcohol" required><br>

            <br><button type="submit">Predict Now</button>
        </form>
    ''')

# URL configuration
urlpatterns = [
    path('', predict_view),
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import sys

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
    sys.argv = ['app.py', 'runserver', '8000']
    execute_from_command_line(sys.argv)
