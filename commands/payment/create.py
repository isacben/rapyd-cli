import json
import argparse

from tools.connector import make_request

description = "create a payment"

def run(args: list[str]) -> None:
   
    parser = argparse.ArgumentParser(prog="rapyd payment create", description=description)

    required_arguments = parser.add_argument_group('required')

    required_arguments.add_argument("--amount", help="payment amount", required=True)
    required_arguments.add_argument("--currency", help="payment currency", required=True)
    required_arguments.add_argument("--payment_method", help="payment method object or id", required=True)
    required_arguments.add_argument("-e", "--env", help="the Rapyd environment", required=True)
    
    parser.add_argument("--address", help="billing address object associated with this specific payment", default="")
    parser.add_argument("--capture", help="determines when the payment is processed for capture", default=None)
    parser.add_argument("--complete_payment_url", help="url where the customer is redirected after successfully completing an operation on an external page", default="")
    parser.add_argument("--customer", help="id of the customer who is making the payment", default="")
    parser.add_argument("--description", help="description of the payment", default="")
    parser.add_argument("--error_payment_url", help="url where the customer is redirected if an error occurs during or after an operation on an external page", default="")
    parser.add_argument("--ewallet", help="id of the wallet that the money is paid into", default="")
    parser.add_argument("--expiration", help="expiration of the payment in Unix time", default="")
    parser.add_argument("--fixed_side", help="whether the FX rate is fixed for the buy side or for the sell side", default="")
    parser.add_argument("--merchant_reference_id", help="id defined by the client", default="")
    parser.add_argument("--payment_fees", help="object that defines transaction fees and foreign exchange fees", default="")
    parser.add_argument("--payment_method_options", help="object describing additional information required for the payment", default="")
    parser.add_argument("--requested_currency", help="three-letter ISO 4217 code", default="")
    parser.add_argument("--statement_descriptor", help="description that appears in the customer's bank statement", default="")

    arguments = parser.parse_args(args)

    try:
        address = json.loads(arguments.address)
    except:
        address = arguments.address

    try:
        payment_method = json.loads(arguments.payment_method)
    except:
        payment_method = arguments.payment_method

    try:
        customer = json.loads(arguments.customer)
    except:
        customer = arguments.customer
    
    try:
        payment_fees = json.loads(arguments.payment_fees)
    except:
        payment_fees = arguments.payment_fees

    try:
        payment_method_options = json.loads(arguments.payment_method_options)
    except:
        payment_method_options = arguments.payment_method_options



    body = {
        "address": address,
        "amount": arguments.amount,
        "capture": arguments.capture,
        "complete_payment_url": arguments.complete_payment_url,
        "currency": arguments.currency,
        "customer": customer,
        "description": arguments.description,
        "error_payment_url": arguments.error_payment_url,
        "ewallet": arguments.ewallet,
        "expiration": arguments.expiration,
        "fixed_side": arguments.fixed_side,
        "merchant_reference_id": arguments.merchant_reference_id,
        "payment_fees": payment_fees,
        "payment_method": payment_method,
        "payment_method_options": payment_method_options,
        "requested_currency": arguments.requested_currency,
        "statement_descriptor": arguments.statement_descriptor,
    }

    path = f'/v1/payments'
    response = make_request(env=arguments.env, method='post', path=path, body=body)
    
    print(json.dumps(response, indent=4))
