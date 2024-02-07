import math


#class for vectors
class ve:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

#class for constant vectors
class cVE:

  def __init__(self, bool, x, y, z):
    self.bool = bool
    self.x = x
    self.y = y
    self.z = z



#function for printing vector
def vP(v):
  print(v.x, v.y, v.z)

#function for magnitude
def getMag(v):
  return math.sqrt(v.x**2 + v.y**2 + v.z**2)


#function for creating unit vector
def getUnit(v):
  return vMult(1 / (getMag(v)), v)


#function for scalar multiplication
def vMult(c, u):
  return ve(c * u.x, c * u.y, c * u.z)


#function for vector addition and subraction
def vAdd(v1, v2):
  return ve(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


def vSub(v1, v2):
  return ve(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)


#function for dot product
def vDot(v1, v2):
  return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


#function for cross product
def vCross(v1, v2):
  return ve(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z,
          v1.x * v2.y - v1.y * v2.x)


#function for turning cartesian vector into polar vector
def stoc(v):
  x = v.x * math.sin(v.z * math.pi/180) * math.cos(v.y * math.pi/180)
  y = v.x * math.sin(v.z * math.pi/180) * math.sin(v.y * math.pi/180)
  z = v.x * math.cos(v.z * math.pi/180)
  return ve(x,y,z)


#function for turning polar vector into cartesian vector
def ctos(v):
  r = getMag(ve(v.x ,v.y, v.z))
  t = math.atan(v.y/v.x) * 180/math.pi if v.x != 0 else math.atan(v.y/10E-10) * 180/math.pi
  p = math.acos(v.z/r) * 180/math.pi

  return ve(r,t,p)

#function for matrix multiplication
def mMult(v, m11, m12, m13, m21, m22, m23, m31, m32, m33):
  return ve(v.x * m11 + v.y * m21 + v.z * m31, v.x * m12 + v.y * m22 + v.z * m32, v.x * 
            m13 + v.y * m23 + v.z * m33)

