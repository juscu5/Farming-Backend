from django.core.management.base import BaseCommand
from costsavings.models import PH_Farming_Savings
from django.db import connection

class Command(BaseCommand):
    help = 'Insert data into farming_solution_savings table'

    def handle(self, *args, **kwargs):
        data = [
            {
                "site_ref": 1234,
                "Year": 2024,
                "quarter": "Q1",
                "account": "Expense",
                "amount": 5000,
                "created_dt_pht": "2024-04-01T10:00:00",
                "updated_dt_pht": "2024-04-01T11:30:00",
                "last_updated_by": "JohnDoe"
            },
            # Add remaining data entries here...
            {
                "site_ref": 5678,
                "Year": 2024,
                "quarter": "Q1",
                "account": "Revenue",
                "amount": 10000,
                "created_dt_pht": "2024-04-01T09:15:00",
                "updated_dt_pht": "2024-04-01T11:00:00",
                "last_updated_by": "JaneSmith"
            },
            {
                "site_ref": 9012,
                "Year": 2024,
                "quarter": "Q2",
                "account": "Expense",
                "amount": 7500,
                "created_dt_pht": "2024-04-01T13:45:00",
                "updated_dt_pht": "2024-04-01T15:20:00",
                "last_updated_by": "AliceJohnson"
            },
            {
                "site_ref": 3456,
                "Year": 2024,
                "quarter": "Q2",
                "account": "Revenue",
                "amount": 12000,
                "created_dt_pht": "2024-04-02T08:30:00",
                "updated_dt_pht": "2024-04-02T10:15:00",
                "last_updated_by": "BobAnderson"
            },
            {
                "site_ref": 7890,
                "Year": 2024,
                "quarter": "Q3",
                "account": "Expense",
                "amount": 6000,
                "created_dt_pht": "2024-04-03T14:00:00",
                "updated_dt_pht": "2024-04-03T16:30:00",
                "last_updated_by": "EmmaBrown"
            },
            {
                "site_ref": 2345,
                "Year": 2024,
                "quarter": "Q3",
                "account": "Revenue",
                "amount": 11000,
                "created_dt_pht": "2024-04-04T11:45:00",
                "updated_dt_pht": "2024-04-04T13:20:00",
                "last_updated_by": "ChrisDavis"
            },
            {
                "site_ref": 6789,
                "Year": 2024,
                "quarter": "Q4",
                "account": "Expense",
                "amount": 8500,
                "created_dt_pht": "2024-04-05T09:45:00",
                "updated_dt_pht": "2024-04-05T11:10:00",
                "last_updated_by": "GraceEvans"
            },
            {
                "site_ref": 123,
                "Year": 2024,
                "quarter": "Q4",
                "account": "Revenue",
                "amount": 13000,
                "created_dt_pht": "2024-04-06T12:30:00",
                "updated_dt_pht": "2024-04-06T14:45:00",
                "last_updated_by": "HenryFord"
            },
            {
                "site_ref": 456,
                "Year": 2024,
                "quarter": "Q1",
                "account": "Expense",
                "amount": 5500,
                "created_dt_pht": "2024-04-07T10:15:00",
                "updated_dt_pht": "2024-04-07T12:00:00",
                "last_updated_by": "IsabellaGarcia"
            },
            {
                "site_ref": 789,
                "Year": 2024,
                "quarter": "Q1",
                "account": "Revenue",
                "amount": 10500,
                "created_dt_pht": "2024-04-08T08:45:00",
                "updated_dt_pht": "2024-04-08T10:30:00",
                "last_updated_by": "JamesHarris"
            },
            {
                "site_ref": 234,
                "Year": 2024,
                "quarter": "Q2",
                "account": "Expense",
                "amount": 7800,
                "created_dt_pht": "2024-04-09T13:00:00",
                "updated_dt_pht": "2024-04-09T15:15:00",
                "last_updated_by": "KatherineIrwin"
            },
            {
                "site_ref": 567,
                "Year": 2024,
                "quarter": "Q2",
                "account": "Revenue",
                "amount": 11500,
                "created_dt_pht": "2024-04-10T10:30:00",
                "updated_dt_pht": "2024-04-10T12:45:00",
                "last_updated_by": "LiamJackson"
            },
            {
                "site_ref": 890,
                "Year": 2024,
                "quarter": "Q3",
                "account": "Expense",
                "amount": 6200,
                "created_dt_pht": "2024-04-11T14:15:00",
                "updated_dt_pht": "2024-04-11T16:40:00",
                "last_updated_by": "MiaKhan"
            },
            {
                "site_ref": 1234,
                "Year": 2024,
                "quarter": "Q3",
                "account": "Revenue",
                "amount": 11200,
                "created_dt_pht": "2024-04-12T11:00:00",
                "updated_dt_pht": "2024-04-12T13:25:00",
                "last_updated_by": "NoahLee"
            },
            {
                "site_ref": 5678,
                "Year": 2024,
                "quarter": "Q4",
                "account": "Expense",
                "amount": 8800,
                "created_dt_pht": "2024-04-13T09:30:00",
                "updated_dt_pht": "2024-04-13T11:55:00",
                "last_updated_by": "OliviaMartin"
            },
            {
                "site_ref": 9012,
                "Year": 2024,
                "quarter": "Q4",
                "account": "Revenue",
                "amount": 13500,
                "created_dt_pht": "2024-04-14T12:15:00",
                "updated_dt_pht": "2024-04-14T14:30:00",
                "last_updated_by": "PeterNguyen"
            },
            {
                "site_ref": 3456,
                "Year": 2024,
                "quarter": "Q1",
                "account": "Expense",
                "amount": 5700,
                "created_dt_pht": "2024-04-15T10:45:00",
                "updated_dt_pht": "2024-04-15T12:20:00",
                "last_updated_by": "QuinnO'Connor"
            },
            {
                "site_ref": 7890,
                "Year": 2024,
                "quarter": "Q1",
                "account": "Revenue",
                "amount": 10800,
                "created_dt_pht": "2024-04-16T08:00:00",
                "updated_dt_pht": "2024-04-16T10:05:00",
                "last_updated_by": "RachelPatel"
            },
            {
                "site_ref": 2345,
                "Year": 2024,
                "quarter": "Q2",
                "account": "Expense",
                "amount": 8000,
                "created_dt_pht": "2024-04-17T13:30:00",
                "updated_dt_pht": "2024-04-17T15:50:00",
                "last_updated_by": "SamuelQuinn"
            },
            {
                "site_ref": 6789,
                "Year": 2024,
                "quarter": "Q2",
                "account": "Revenue",
                "amount": 12500,
                "created_dt_pht": "2024-04-18T11:20:00",
                "updated_dt_pht": "2024-04-18T13:40:00",
                "last_updated_by": "TiffanyRoberts"
            }
        ]

        sql_insert = "INSERT INTO farming_solution_savings (site_ref, year, quarter, account, amount, created_dt_pht, updated_dt_pht, last_updated_by) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        with connection.cursor() as cursor:
            for entry in data:
                cursor.execute(sql_insert, (
                    entry['site_ref'], entry['Year'], entry['quarter'], entry['account'],
                    entry['amount'], entry['created_dt_pht'], entry['updated_dt_pht'],
                    entry['last_updated_by']
                ))

        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
