# rapyd-cli

A CLI tool to use Rapyd's fintech API.

*This is a work in progress.*

## Commands

Retrieve Payment:

### `rapyd payment retrieve ID`

```shell
usage: rapyd payment retrieve [-h] -e ENV id

retrieve a payment

options:
  -h, --help         show this help message and exit

required:
  id                 id of the payment; string starting with payment_
  -e ENV, --env ENV  the Rapyd environment
```