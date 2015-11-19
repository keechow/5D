data = ["one","two","three","four","six","one","two","three","four","six"]

file_handler = open("write_test","w")

file_handler.writelines(data)

file_handler.close()
