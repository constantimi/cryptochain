import yaml
import subprocess


def execute_command(command):
	subprocess.call(command.split())

with open("/home/stiefff/cloud/infrastructure/cluster.yml", 'r') as stream:
		cluster = yaml.load(stream)

name = cluster['cluster']['name']
zone = cluster['cluster']['zone']
#getting credentials 
execute_command("gcloud container clusters get-credentials {} --zone {}".format(name, zone))

execute_command("kubectl apply -f /home/stiefff/cloud/manifests/deployment.yml")
execute_command("kubectl apply -f /home/stiefff/cloud/manifests/service.yml")
execute_command("kubectl apply -f /home/stiefff/cloud/manifests/ingress.yml")
execute_command("kubectl apply -f /home/stiefff/cloud/manifests/cronjob.yml")
