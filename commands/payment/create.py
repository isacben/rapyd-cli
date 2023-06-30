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
    parser.add_argument("--customer", help="id of the customer who is making the payment", default="")
    parser.add_argument("--description", help="description of the payment", default="")
    parser.add_argument("--ewallet", help="id of the wallet that the money is paid into", default="")
    parser.add_argument("--expiration", help="expiration of the payment in Unix time", default="")
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

    body = {
        "address": address,
        "amount": arguments.amount,
        "capture": arguments.capture,
        "currency": arguments.currency,
        "customer": customer,
        "description": arguments.description,
        "ewallet": arguments.ewallet,
        "expiration": arguments.expiration,
        "payment_method": payment_method,
        "statement_descriptor": arguments.statement_descriptor,
    }

    #print(json.dumps(body))

    path = f'/v1/payments'
    response = make_request(env=arguments.env, method='post', path=path, body=body)
    
    print(json.dumps(response, indent=4))