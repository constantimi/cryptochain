import subprocess
import sys
import yaml
import commands
def check_keys(keys, yml, instance_type):
	keys = keys.split()		
	for x in range(len(keys)):
		if yml[instance_type].has_key(keys[x]) == False:
			print "Error, missing or misspelled key- ",keys[x]	
			sys.exit()

if sys.argv[1] == "createSQL":
	with open("SQLinstance.yml", 'r') as stream:
		r = yaml.load(stream)
	check_keys("zone name", r, 'SQL')

	name = r['SQL']['name']
	zone = r['SQL']['zone']
	command = "gcloud sql instances create {} --zone {}".format(name, zone)	
	subprocess.check_output(command.split())

if sys.argv[1] == "createCluster":
 	with open("cluster.yml", 'r') as stream:
		r = yaml.load(stream)
	check_keys("zone name num-nodes machine-type", r, 'cluster')
	name = r['cluster']['name']
	nodes = r['cluster']['num-nodes']
	zone = r['cluster']['zone']
	machine_type = r['cluster']['machine-type']

	command = "gcloud container clusters create {} --zone {} --num-nodes {} --machine-type {}".format(name, zone, nodes, machine_type)
	subprocess.check_output(command.split())

if sys.argv[1] == "createInstance":
	print("STEP ONE")
	with open("instance.yml", 'r') as stream:
		r = yaml.load(stream)
	check_keys("zone name machine-type", r, 'instance')
	name = r['instance']['name']
	zone = r['instance']['zone']	
	machine_type = r['instance']['machine-type']

	command = "gcloud compute instances create {} --zone {} --machine-type {}".format(name, zone, machine_type)
	subprocess.call(command.split())

	print("STEP TWO") 
	command = "gcloud compute scp modifier.sh {}:~ --zone {}".format(name,zone)
	subprocess.call(command.split())
	
	print("STEP THREE")
	ip = 'gcloud --format="value(networkInterfaces[0].accessConfigs[0].natIP)" compute instances list  --filter="name=({})"'.format(name)
 	ip = commands.getoutput(ip)
	command = 'ssh-keygen -R {}'.format(ip)
	subprocess.call(command.split())
	command = "ssh -o  StrictHostKeyChecking=no stiefff@{} sudo /home/stiefff/modifier.sh".format(ip)
	subprocess.call(command.split())
	
