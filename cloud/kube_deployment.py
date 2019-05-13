import yaml
import subprocess


def execute_command(command):
	subprocess.call(command.split())

with open("cloud/infrastructure/cluster.yml", 'r') as stream:
		cluster = yaml.load(stream)

name = cluster['cluster']['name']
zone = cluster['cluster']['zone']
#getting credentials 
execute_command("gcloud container clusters get-credentials {} --zone {}".format(name, zone))

execute_command("kubectl apply -f cloud/manifests/deployment.yml")
execute_command("kubectl apply -f cloud/manifests/service.yml")
execute_command("kubectl apply -f cloud/manifests/ingress.yml")
execute_command("kubectl apply -f cloud/manifests/cronjob.yml")
