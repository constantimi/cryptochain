import os
import subprocess
import sys
import yaml
import commands
import argparse
HOME_DIR = os.environ["HOME"]

parser = argparse.ArgumentParser(description='Creating infrastructure.')
parser.add_argument('-sql', help='Create an SQL instance in Google Cloud Platform')
parser.add_argument('-cluster', help='Create a cluster in Google Cloud Platform')
parser.add_argument('-instance', help='Create a runner instance in Google Cloud Platform.')
parser.add_argument('-all', help = 'Create the whole infrastructure from scratch')
#args = parser.parse_args()

#print(args.accumulate(args.--sql))

def check_keys(keys, yml, instance_type):
	keys = keys.split()		
	for x in range(len(keys)):
		if yml[instance_type].has_key(keys[x]) == False:
			print "In", instance_type, "creation,"
			print "Error, missing or misspelled key - ",keys[x]	
			sys.exit()

def execute_command(command):
	subprocess.call(command.split())

if sys.argv[1] == "-sql" or sys.argv[1]=='-all':
	with open("infrastructure/SQLinstance.yml", 'r') as stream:
		r = yaml.load(stream)
	check_keys("zone name database-version password", r, 'SQL')

	name = r['SQL']['name']
	zone = r['SQL']['zone']
	database = r['SQL']['database-version']
	password = r['SQL']['password']
	machine_type=r['SQL']['tier']
	#creating the SQL instance
	execute_command("gcloud beta sql instances create {} --zone {} \
			--database-version={} \
		        --tier={} \
			--network=default".format(name, zone, database, machine_type))	
	execute_command("gcloud sql users set-password postgres no-host --instance={} --password={}".format(name,password))
	#creating the docker user
	execute_command("gcloud sql users create django \
   			--instance={} --password=django".format(name))
	execute_command("gcloud sql databases create django --instance={}".format(name))

	
if sys.argv[1] == "-cluster" or sys.argv[1]=='-all':
 	with open("infrastructure/cluster.yml", 'r') as stream:
		r = yaml.load(stream)
	check_keys("zone name num-nodes machine-type", r, 'cluster')
	name = r['cluster']['name']
	nodes = r['cluster']['num-nodes']
	zone = r['cluster']['zone']
	machine_type = r['cluster']['machine-type']

	execute_command("gcloud container clusters create {} \
		   	--enable-ip-alias \
			--zone {} \
			--num-nodes {} \
			--machine-type {}".format(name, zone, nodes, machine_type))


if sys.argv[1] == "-instance" or sys.argv[1]=='-all':
	print("CREATING VM")
	with open("infrastructure/instance.yml", 'r') as stream:
		r = yaml.load(stream)
	check_keys("zone name machine-type", r, 'instance')
	name = r['instance']['name']
	zone = r['instance']['zone']	
	machine_type = r['instance']['machine-type']

	execute_command("gcloud compute instances create {} \
			--zone {} \
			--machine-type {} \
			--create-disk size=25".format(name, zone, machine_type))

	print("SENDING FILES TO VM") 
	execute_command("gcloud compute scp ../cloud --recurse {}:~ --zone {}".format(name,zone))
	
	print("EXECUTING modifier.sh SCRIPT")
        command = "gcloud compute ssh {} --zone europe-west2-c --command".format(name).split()
        command.append('sudo sh {}/cloud/modifier.sh'.format(HOME_DIR))
        print(command)
	subprocess.call(command)

	
