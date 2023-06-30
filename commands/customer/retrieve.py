import json
import argparse

from lib.connector import make_request

description = "retrieve a customer"

def run(args: list[str]) -> None:
   
    parser = argparse.ArgumentParser(prog="rapyd customer retrieve", description=description)
    
    required_arguments = parser.add_argument_group('required')

    required_arguments.add_argument("customer", help="id of the customer object; string starting with cus_")
    required_arguments.add_argument("-e", "--env", help="the Rapyd environment", required=True)

    arguments = parser.parse_args(args)

    path = f'/v1/customers/{arguments.customer}'
    response = make_request(env=arguments.env, method='get', path=path)

    print(json.dumps(response, indent=4))