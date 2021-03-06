from django.core.management.base import BaseCommand, CommandError
from polls.models import Department,User
import csv



class Command(BaseCommand):

	def handle(self, *args, **options):
		with open('/home/user/sample_server/polls/sample_data.xls') as f:
			data=csv.reader(f)
			for each in data:
				print each[0]
				kwargs={
							"first_name":each[0],
							"last_name":each[1],
							"age":each[2],
							"mobile_number":each[3],
							"email":each[4],
							"department":Department.objects.get(name=each[5]),
							"username":each[6]
							}
				User.objects.create(**kwargs)
