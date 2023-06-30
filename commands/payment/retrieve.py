import json
import argparse

from tools.connector import make_request

description = "retrieve a payment"

def run(args: list[str]) -> None:
   
    parser = argparse.ArgumentParser(prog="rapyd payment retrieve", description=description)
    
    required_arguments = parser.add_argument_group('required')

    required_arguments.add_argument("id", help="id of the payment; string starting with payment_")
    required_arguments.add_argument("-e", "--env", help="the Rapyd environment", required=True)

    arguments = parser.parse_args(args)

    path = f'/v1/payments/{arguments.id}'
    response = make_request(env=arguments.env, method='get', path=path)

    print(json.dumps(response, indent=4))