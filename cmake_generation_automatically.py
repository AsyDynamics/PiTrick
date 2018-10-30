#!/usr/bin/python3

import os
#global base_dir
base_dir = '/home/pi/'
global pro_name, output_name, v_num, dir_proj

def input_info():
	pro_name = input('Enter project name:\n')
	while os.path.exists(pro_name):
		print ('Project with this name existed! Rename it:\n')
		pro_name = input()
	output_name = input('Enter project executable name:\n')
	v_num = input('Enter required cmake version, suggest less than 3.7:\n')
	return pro_name, v_num, output_name

def create_directory(dir_proj, pro_name):
	os.makedirs(base_dir + dir_proj + pro_name)
	os.makedirs(base_dir + dir_proj + pro_name + '/build')
	os.makedirs(base_dir + dir_proj + pro_name + '/bin')
	os.makedirs(base_dir + dir_proj + pro_name + '/src')
	print ('All directory and sub-directory are created\n')

def goto_directory():
	dir_proj = input('Enter the desired directory after /home/user/ with last /:\n')
	os.chdir(base_dir + dir_proj)
	print ('Now we are at ' + os.getcwd())
	return dir_proj

def create_cmakelist(dir_proj, pro_name, v_num, output_name):
	list = open(base_dir + dir_proj + pro_name + '/CMakeLists.txt', 'w')
	list.write('project(' + pro_name + ')\n')
	list.write('cmake_minimum_required(VERSION ' + v_num + ')\n')
	list.write('add_executable(' + output_name + ' src/main.cpp)\n')
	list.write('set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)\n')
	list.close()
	maincpp = open(base_dir + dir_proj + pro_name + '/src/main.cpp', 'w')
	maincpp.write('#include <iostream>\n')
	maincpp.write('using namespace std;\n')
	maincpp.write('int main(){\n')
	maincpp.write('    return 0;\n}')
	maincpp.close()
	print ('CMakeLists created\n')

dir_proj = goto_directory()
pro_name, v_num, output_name = input_info()
create_directory(dir_proj, pro_name)
create_cmakelist(dir_proj, pro_name, v_num, output_name)



#print (os.getcwd())

