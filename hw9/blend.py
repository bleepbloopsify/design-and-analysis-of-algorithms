s1 = 'hello'
s2 = 'nike'
s3 = 'nheiklloe'

def is_blend(s1, s2, blend):
  b_pos = 0
  pos1 = 0
  pos2 = 0

  while True:

    if len(s1) == pos1 and len(s2) == pos2 and b_pos == len(blend):
      return True

    if len(s1) == pos1:
      if s2[pos2] == blend[b_pos]:
        b_pos += 1
        pos2 += 2
    elif len(s2) == pos2:
      pass
    else:
      pass