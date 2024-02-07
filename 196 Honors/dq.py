import ve
import math
#list of all infiniteimal electrostatic elements
ldq = []

cEB = False

#class for electrostatic elements
class dq:

  def __init__(self, r, q):
    self.r = r
    self.q = q


#creating a single electrostatic object and adding to list
def mdq(x, y, z, q):
  r = ve.ve(x, y, z)
  q = dq(r, q)
  ldq.append(q)


def cEM(x, y, z, m):
  cEB = True
  cEF = ve.vMult(m, ve.getUnit(ve.ve(x,y,z)))

  