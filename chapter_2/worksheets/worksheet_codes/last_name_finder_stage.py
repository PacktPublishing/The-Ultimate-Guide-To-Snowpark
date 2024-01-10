def last_name_finder(name_list:list):
  last_name_list = [name.split()[1] for name in name_list]
  return last_name_list