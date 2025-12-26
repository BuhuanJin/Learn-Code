def get_all_dirs(root_path: str) -> lsit:
  dirs_list = []
  
  if not os.path.exists(root_path) or not os.path.isdir(root_path):
    return dirs_list
  
  dirs_list.append(os.path.abspath(root_path))
  
  for item in os.listdir(root_path):
    item_path = os.path.join(root_path, item)
    
    if os.path.isdir(item_path):
      dirs_list.extend(get_all_dirs(item_path))
   
  return dirs_list 

************************************************************************************
这代码，dirs_list 是函数栈中的变量，每次调用，它都是空的。
append 和 extend 确实 操作的是 同一个 dirs_list。
正向时：dirs_list.append 都只加了 当前所在的目录。
返回时：dirs_list 有 ↑，再额外 （扁平化地）添加了 上一个递归返回时的 return 内容 

dirs_list 再清掉，又返回到 上一个 dirs_list
之前的 append 几乎都可以无视了，除了 第一个 append —— 递归到顶了
而又extend 之前返回的 所有的目录，所以，结果是 得到了 所有的目录

*************************************************************************************
