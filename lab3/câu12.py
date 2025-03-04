#def container_check_digit(container):
char_map = {chr(i): i - 55 for i in range(65, 91)}  
char_map.update({str(i): i for i in range(10)})
