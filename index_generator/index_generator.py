import subprocess
import os 
import sys
# Call with Python3

# Generate an index file in markdown, then call mdgen to create an html file with
# links to every single file with name "filename" in the directory + subdirectories

# SYNTAX
# indexgen.py filename index_filename
# EXAMPLE: indexgen LOG INDEX

filename = str(sys.argv[1])
index_filename = str(sys.argv[2])

# Find all files with name = filename
locs = subprocess.check_output(["find",".","-name", filename])
locs = locs.decode('utf8').split('\n')
del locs[len(locs)-1] # last entry will be blank, so remove it
locs.sort()
# now locs contains all of the paths to every "filename" file within this directory structure

# remove first period from each element in locs
locs = [ loc[1:] for loc in locs ]

class location:
	strs = []
	def __init__(self, s):
		self.strs = s.split('/')
def upcase_first_letter(s):
	return s[0].upper() + s[1:]
    # will capitalize first letter, leave all others untouched
def getbase(new,keys):
	if(new.get(keys[0],'no') == 'no'):
		return new
	elif(len(keys)>0):
		return getbase(new.get(keys[0]),keys[1:len(keys)])
	else:
		return None #rip
def group(dict):
	new = {}
	for x in range(len(dict)):
		y = 0 # index
		path = []
		temp = new
		while y < len(dict[x].strs):
			if(dict[x].strs[y] in temp):
				temp = temp.get(dict[x].strs[y])
			else:
				getbase(new,dict[x].strs).update({dict[x].strs[y]:{}})
				temp = temp.get(dict[x].strs[y])
			y+=1
	return new
def write_tree(str, path, level, dict):	
	if(dict.get(filename,'no') == 'no' and str != filename):
		if(level >= 0):
			# Use upcase_first_letter() to capitalize first letter in strings
			index_file.write(('\t'*level)+'* '+upcase_first_letter(str)+'\n') #write out to file somehow lol
	elif(str != filename):
		# this is where you would write html links
		index_file.write(('\t'*level)+'* ['+upcase_first_letter(str)+'](.'+path+'/'+str+'/'+filename+'.html)'+'\n') 
	# Alphabetize the keys before calling recursion
	alpha_keys = []
	for key in dict:
		alpha_keys += [key]
	alpha_keys.sort(key=lambda x: x.lower()) # case insensitive sort

	# Now proceed with recursion
	for key in alpha_keys:
		if(str != ''):
			path_new = path+'/'+str
		else:
			path_new = path

		write_tree(key,path_new,level+1,dict[key]) # recursive, keep track of path down the tree
	
def main():
	global locs
	global index_file
	dictionary = []
	for x in range(len(locs)):
		dictionary.append(location(locs[x]))

	tree = group(dictionary)
	
	# create index file
	index_file = open(index_filename,"w+")
	index_file.write('# Index\n')

	# write index file using recursive tree structure
	write_tree('', '',-2,tree)

	# close file
	index_file.close()
	
	# generate markdown file
	command = "mdgen -o "+index_filename
	subprocess.Popen(["/bin/sh", "-c", command])

main()
