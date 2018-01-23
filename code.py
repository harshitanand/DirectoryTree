import os
import sys
import argparse

def walk_normal(startpath):
  i = 1
  print startpath,
  for root, dirs, files in os.walk(startpath):
      level = root.replace(startpath, '').count(os.sep)
      if level == 0 and i != 1:
          indent = '|--- '
          subindent = '|' + ' ' * 6  + indent
      elif level != 0 and i != 1:
          indent = '|' + ' ' * 6 * (level) + '|--- '
          subindent = '|' + ' ' * 6 * (level + 1) + '|--- '
      else:
          indent = ''
          subindent = '|--- '
      i += 1
      print('{}{}'.format(indent, os.path.basename(root)))
      for f in files:
            print('{}{}'.format(subindent, f))

def walk_rtl(startpath):
    res, i = [], 1
    for root, dirs, files in os.walk('Desktop/'):
        level = root.replace(startpath, '').count(os.sep)
        if level == 0 and i != 1:
          indent = ' ---|'
          subindent =  indent + ' ' * 6 + '|'
        elif level != 0 and i != 1:
          indent =  ' ---|' + ' ' * 6 * (level) + '|'
          subindent = ' ---|' + ' ' * 6 * (level + 1) + '|'
        else:
          indent = ''
          subindent = ' ---|'
        i += 1
        res.append('{}{}'.format(os.path.basename(root), indent))
        for f in files:
              res.append('{}{}'.format(f, subindent))

    max_len = len(max(res, key=len))
    res.remove(res[0])
    print ' ' * (max_len - len(startpath)) + startpath
    for item in res:
      extra_space = max_len - len(item)
      item  = ' ' * extra_space + item
      print item

if __name__ == "__main__":
    startpath = ''
    parser = argparse.ArgumentParser()
    parser.add_argument("--rtl")

    args, leftovers = parser.parse_known_args()
    if args.rtl is not None:
      walk_rtl(args.rtl)
    else:
      startpath = sys.argv[1] or 'Desktop/'
      print ''
      walk_normal(startpath)
      
