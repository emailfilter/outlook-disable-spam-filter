from argparse import ArgumentParser, SUPPRESS
from outlookdisablespamfilter.shared import transfer_spam_emails


def command_line_parser():
    """
    Main function primarly used for the command line interface
    """
    parser = ArgumentParser(prog="outlookdisablespamfilter", add_help=False)
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument(
        "-e",
        "--outlook_email",
        help="Outlook.com Email Address",
        required=True
    )
    required.add_argument(
        "-p",
        "--outlook_app_password",
        help="Outlook.com App Password",
        required=True
    )
    optional.add_argument(
        '-h',
        '--help',
        action='help',
        default=SUPPRESS,
        help='show this help message and exit'
    )
    args = parser.parse_args()
    transfer_spam_emails(
        outlook_email=args.outlook_email,
        outlook_app_password=args.outlook_app_password
    )


if __name__ == "__main__":
    command_line_parser()
