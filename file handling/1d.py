f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
#"a" - Append - will create a file if the specified file does not exist
#"x" - Create - will create a file, returns an error if the file exist
#"w" - Write - will create a file if the specified file does not exist
f = open("myfile.txt", "x")