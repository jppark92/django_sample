from django.db import models

# 이곳은 모델정의..

class Location(models.Model):
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50,null=True,blank =True)
	country = models.CharField(max_length=50)

	def __str__(self):
		if self.state:
			return "%s,%s,%s" %(self.city,slef.state,self.country)
		else:
			return "%s,%s" %(self.city,self.country)

        class Admin:
		list_display = ("city","state","country")


class Job(models.Model):
	pub_date = models.DateField()
	job_title = models.CharField(max_length=50)
	job_description = models.TextField()
	location = models.ForeignKey(Location)

	def __init__(self):
		return "%s (%s)" %(self.job_title,self.location)
