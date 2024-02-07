import ve
import c
import dq
import di
import math


#list of all particles
ldp = []


#class for particle elements
class dp:

  def __init__(self, r, v, a, q, m):
    self.r = r
    self.v = v
    self.a = a
    self.q = q
    self.m = m


def mdp(x, y, z, vx, vy, vz, q, m):
  r = ve.ve(x, y, z)
  v = ve.ve(vx, vy, vz)
  a = ve.ve(0, 0, 0)
  p = dp(r, v, a, q, m)
  ldp.append(p)



#method for finding E field
def cE(i):
  #start by creating an Electric and field vector and setting it to 0 for every loop
  if dq.cEB == True:
    E = dq.cEF
  else:
    E = ve.ve(0, 0, 0)



  #for each particle, going through each charge element
  for j in range(len(dq.ldq)):

    #vector for distance between particle and charge
    d = ve.vSub(ldp[i].r, dq.ldq[j].r)

    #condition for d not being zero so no divide by zero error
    if (ve.getMag(d) != 0):

      #calculating E contribution from particle
      m = (c.k * dq.ldq[j].q) / (ve.getMag(d))**2
      E = ve.vAdd(E, ve.vMult(m, ve.getUnit(d)))

    else:
      # if the charge and particle are in the same place, just add a zero vector
      E = ve.vAdd(E, ve.ve(0, 0, 0))

  ve.vP(E)
  return E
  
def cB(i):
  #start by creating an Magnetic field vector and setting it to 0 for every loop
  B = ve.ve(0, 0, 0)

  #for each particle, going through each charge element
  for j in range(len(di.ldi)):

    #vector for distance between particle and current
    d = ve.vSub(ldp[i].r, di.ldi[j].r)

    #condition for d not being zero so divide by zero
    if (ve.getMag(d) != 0):

      #calculating B contribution from current
      m = ((c.u/4*math.pi) * di.ldi[j].i) / (ve.getMag(d))**2
      B = ve.vAdd(B, ve.vMult(m, ve.vCross(di.ldi[j].s, ve.getUnit(d))))

    else:
     # if the current and particle are in the same place, just add a zero vector (will have to change later)
     B = ve.vAdd(B, ve.ve(0, 0, 0))
  return B

#Lorentz law and equations of motion for each particle 
def cM(E, B, i):
   
  ldp[i].a = ve.vMult(ldp[i].q / ldp[i].m, ve.vAdd(E, ve.vCross(ldp[i].v, B)) )

  # finding v from a using adjustible "dt"
  ldp[i].v = ve.vAdd(ldp[i].v, ve.vMult(
      c.dt, ldp[i].a))  

  #finding r from v
  ldp[i].r = ve.vAdd(ldp[i].r, ve.vMult(c.dt, ldp[i].v))  
  
  #returning particle coordinates for plotting
  ve.vP(ldp[i].v)
  return ldp[i].r

