from django.db import models

# Create your models here.

class Developer(models.Model):
	developer_name = models.CharField(max_length=50)
	developer_id = models.CharField(max_length=12, primary_key=True,)


class Project(models.Model):
	project_name = models.CharField(max_length=50)
	project_id = models.CharField(max_length=12, primary_key=True,)
	project_type = models.CharField(max_length=20)
	start_date = models.DateField()
	end_date = models.DateField(null=True)
	year = models.CharField(max_length=12)
	description = models.CharField(max_length=250, null=True)
	
	
class ProjectAssignment(models.Model):
	assignment_id = models.CharField(max_length=50)
	developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
	project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
	support_staff = models.CharField(max_length=50)
	start_date = models.DateField()
	assignment_date = models.DateField(null=True)
	
class projectTask(models.Model):
	task_id = models.CharField(max_length=50)
	developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
	project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
	
class ProjectProgress(models.Model):
	assignment_id = models.CharField(max_length=50)
	task_id = models.ForeignKey(projectTask, on_delete=models.CASCADE)
	project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
	status = models.CharField(max_length=50)
	description = models.CharField(max_length=250, null=True)