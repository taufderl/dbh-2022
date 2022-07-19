#!/usr/bin/env python3

import IPython

def check(param_1):
  uVar1 = 0
  if (param_1[4] == '-'):
    if (param_1[9] == '-'):
      if (param_1[0xf] == '-'):
        #if (*param_1 == param_1[7]):                ##??
        if (param_1[0] == param_1[7]):
          if (param_1[0xc] == param_1[8]):
            if (param_1[3] == 'M'):
              if (param_1[0xc] == 'G'):
                if (param_1[0x12] == 'Z'):
                  if ((ord(param_1[5]) ^ ord(param_1[10])) == 1):
                    if ((ord(param_1[1]) ^ ord(param_1[7])) == 0x23):
                        uVar1 = 1
  return uVar1;

# 0123456789abcdef012
# Ab M-3 AG-2 G  -  Z

# Ab0M-30AG-20G00-00Z
key = 'Ab0M-30AG-20G00-00Z'
print(len(key))
print(check(key))

IPython.embed()