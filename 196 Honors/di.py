import ve
import math

#list of all infiniteimal magnetostatic elements
ldi = []


#class for electrostatic elements
class di:

  def __init__(self, r, i, s):
    self.r = r
    self.i = i
    self.s = s


#creating a single electrostatic object and adding to list
def mdi(x, y, z, i, s):
  r = ve.ve(x, y, z)
  i = di(r, i, s)
  ldi.append(i)



lds = []

def mdI(x1, y1, z1, x2, y2, z2, i):
  j = 10000
  mx = (x2 - x1) / j
  my = (y2 - y1) / j
  mz = (z2 - z1) / j

  for k in range(j):
    x = x1 + k * mx
    y = y1 + k * my
    z = z1 + k * mz
    mdi(x, y, z, i, ve.getUnit(ve.ve(x2 - x1, y2-y1 , z2-z1)))


    
#class for creating loop of current
def mdIL(r, i):

  lds.clear()

  #create a single polar vector in xy plane to start
  v = ve.ctos(ve.ve(r,0,0))

  #uses polar cordinates to create loop of vectors in xy plane and append them to list
  j = 0
  while j < 360:
    u = ve.ve(v.x, v.y + j, v.z)
    u = ve.stoc(u)
    lds.append(u)
    j += 0.1


  #goes through the list of vectors and for each creates a pointing vector for B field
  for j in range(len(lds)):
   s = ve.vSub(lds[j+1], lds[j]) if j != len(lds) - 1 else ve.vSub(lds[0], lds[j])
   s = ve.getUnit(s)


   mdi(lds[j].x, lds[j].y, lds[j].z, i, s)
    


 