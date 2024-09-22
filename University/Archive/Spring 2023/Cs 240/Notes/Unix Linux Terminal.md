Path 
- Address of a file or directory the computer uses to keep track of files and directories

PATH variable 
- special variable that contains all of the directories that are automatically searched we attempt to run a program.
	- If we wrote a shell script called `hello.sh` and it's path is for example `/palce/with/the/hello.sh`
	-  function to all of the files in the current working directory that would be executable no matter what the current working directory is. 
		- By adding `/place/with/the` to the `$PATH` variable with the following command:
```
export PATH=$PATH:/place/with/the
```
- `export` : command
- then we are specifying the variable we to set `PATH`.
- Then we are saying we want to set the `PATH` variable to include everything that is already in the path, 
	- by first putting `$PATH`
- Then, we put a colon,
	- that delimits the list of directories in the `PATH` variable.
- Then we specify the location of the file or directory we want accessible from anywhere on the system.
- We will now be able to execute the script `hello.sh` located in `/place/with/the` from anywhere in our system, by typing in the file name without having to include the full path as you type it.
	- This is a temporary sol, because PATH variable will be gone when we close the window.
- *Note :*
	- (PATH) is the variable

We can see our PATH, and which directories are stored in it by entering
```
echo $PATH
```
in the command line (the `$` is used to call variables in bash and other Unix languages)

To view the current working directory we can use the command:
```
pwd
```
- note this provides the path staring from the root location, because it begins with `/`.
	- which denotes the start of the address system.
- (print working directory)

To see what directories and files are in the current directory we are sitting:
```
ls
```
- `ls` is for "list"
- (list content of a directory)

To move in the directory containing the file we want to work with:
```
cd
```
- (change directory)
	- Takes a positional argument that is the path(address) of the directory we want to change into.
		- This can be relative or absolute path.

`../` 
- specifies a directory one level "above" the current working directory

Absolute path 
- is an address that starts from one of two locations:
	- (either "root" (specified with "/" at the beginning of the path) **or** "home" (specified with "~/" at the beginning of the path) )
		- "Full path" - absolute path that starts at "root" with "/", always

Relative path
- address that starts from wherever your sitting in the current working directory.

Command line automatically looks in the current working directory, unless specified. 

Root
- Where the address system of the computer starts `/`

Home
- where the current user's location starts `~/`

View permissions of file in the current directory. (or a directory)
- use the command:
```
ls [file_name]
```
- which lists the information about files/directories.
- adding `-l` to the command returns a long list of information
```
ls -l [file_name]
```
- this is used if we wish to view the permissions of the file or directory in the current working directory. 
	- If we want to look at permissions of a file or directory somewhere else in the system, instead of the file name  `[file_name]` , use the absolute path `/the/place/of/the/file_or_directory`

