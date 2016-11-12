from django.core.management.base import BaseCommand, CommandError
from stoprice.models import StockName
import requests
import json
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = 'Send an email'

    def handle(self, *args, **options):
        stock_details = StockName.objects.all()

        for stock_detail in stock_details:
            company_code = stock_detail.company_code
            target_price = stock_detail.target_price
            email_address = stock_detail.user.email
            print email_address
            print target_price

            web_url = 'http://money.rediff.com/money1/currentstatus.php?companycode={}'.format(company_code)
            json_string = requests.get(web_url).content
            json_dict = json.loads(json_string)
            ltp = json_dict['LastTradedPrice']
            print ltp

            if ltp > target_price:
                send_mail(
                    'Stock Price Surge',
                    'Prices for {} have gone up'.format(company_code),
                    settings.DEFAULT_FROM_EMAIL,
                    [email_address],
                    fail_silently=False,
                )






