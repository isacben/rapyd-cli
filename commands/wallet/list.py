import json
import argparse

from lib.connector import make_request

description = "list wallets"

def run(args: list[str]) -> None:
   
    parser = argparse.ArgumentParser(prog="rapyd wallet list", description=description)
    
    required_arguments = parser.add_argument_group('required')

    parser.add_argument("--ewallet_reference_id", default="", help="wallet ID defined by the customer or end user")
    parser.add_argument("--page_number", default=1, help="page number to retrieve (1 if not specified)")
    parser.add_argument("--page_size", default=10, help="number of results per page")
    parser.add_argument("--type", default="", help="type of wallet", choices=['company', 'person', 'client'])
    
    required_arguments.add_argument("-e", "--env", help="the Rapyd environment", required=True)

    arguments = parser.parse_args(args)

    path = (
        f'/v1/user/wallets/?type={arguments.type}'
        f'&ewallet_reference_id={arguments.ewallet_reference_id}'
        f'&page_number={arguments.page_number}'
        f'&page_size={arguments.page_size}')
    
    response = make_request(env=arguments.env, method='get', path=path)

    print(json.dumps(response, indent=4))