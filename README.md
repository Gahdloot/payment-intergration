<h1>Payment Integrator</h1>

<p>A Django app for integrating payments with multiple gateways. Currently supports integration with <em>[Gateway 1]</em> and <em>[Gateway 2]</em>.</p>

<h2>Features</h2>

<ul>
  <li>Easy integration with multiple payment gateways</li>
  <li>Automated payment status tracking</li>
  <li>Customizable payment form</li>
  <li>Support for multiple currencies</li>
</ul>

<h2>Installation</h2>

<p>Install the package using pip:</p>

<pre><code>pip install django-payment-integrator
</code></pre>

<p>Add <code>payment_integrator</code> to your <code>INSTALLED_APPS</code> in <code>settings.py</code>:</p>

<pre><code>INSTALLED_APPS = [
    ...
    'payment_integrator',
]
</code></pre>

<p>Run the migrations to create the necessary database tables:</p>

<pre><code>python manage.py migrate
</code></pre>

<h2>Configuration</h2>

<p>To configure the payment integrator, add the following to your <code>settings.py</code>:</p>

<pre><code>PAYMENT_INTEGRATOR = {
    'GATEWAY_1': {
        'API_KEY': '[api_key]',
        'API_SECRET': '[api_secret]',
    },
    'GATEWAY_2': {
        'API_KEY': '[api_key]',
        'API_SECRET': '[api_secret]',
    },
}
</code></pre>

<h2>Usage</h2>

<p>To use the payment integrator, you will need to create a payment form and process the payment using the provided functions.</p>

<pre><code>from payment_integrator.forms import PaymentForm
from payment_integrator.utils import process_payment

# Create the payment form
form = PaymentForm(request.POST or None)

if form.is_valid():
    # Process the payment
    result = process_payment(form.cleaned_data, gateway='GATEWAY_1')

    if result['status'] == 'success':
        # Payment successful
    else:
        # Payment failed
</code></pre>

<p>For more information on the available functions and options, see the documentation.</p>

<h2>Documentation</h2>

<p>For full documentation, see <a href="#">https://django-payment-integrator.readthedocs.io/</a>.</p>
