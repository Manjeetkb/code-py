import numpy as np
import re
import math
from scipy import interpolate
import matplotlib.pyplot as plt

#============================================================================
#mol1 = {'mass': 177.028, 'plz': 6.4, 'DP': 2.88}
#print "mol1['mass']: ", mol1['mass']
#print "mol1['plz']: ", mol1['plz']
#print "mol1['DP']: ", mol1['DP']
#mm = mol1['mass']
#==============================================================================
import re

s = 'c8h12n2o1'                #input("enter :")


print (s)
list_of_nums = list(map(int, re.findall('\d+', s)))
print (list_of_nums)
for j in s:
    if j == "c":
        C = 12.01
    if j == "h":
        H = 1.0079
    if j == "n":
        N = 14.0067
    if j == "o":
        O = 15.999
 
 

list = [list_of_nums]
for i in list:
    if i[0] >= 1:
        CM = C*i[0]
        print(CM)
    if i[1] >= 1:
        CM1 = H*i[1]
        print(CM1)
    if i[2] >= 1:
        CM2 = N*i[2]
        print(CM2)
    if i[3] >= 1:
        CM3 = O*i[3]
        print(CM3)

mm = CM+CM1+CM2+CM3
print (mm)
#===============================================================================
#mm = float(input("\n Enter mass of the molecule in amu: "))
print ("Select ion of your choice (ex.): hyd for H3O+, amm for NH4+, nit for NO+ and oxy for O2+")
m_H = 1.00794
m_C = 12.0107
m_O = 15.999
m_N = 14.0067
m_Cl = 35.453
m_Br = 79.904

ion = input("\n  Enter your ion of choice:")
if ion == 'hyd':
    m1 = (3*m_H)+(1*m_O)
    mu = (m1*mm)/(m1+mm)
    mu1 = mu*1.67*10**(-27)
    print (" mass of ion:", m1)
elif ion == 'amm':
    m2 = (4*m_H)+(1*m_N)  
    mu = (m2*mm)/(m2+mm)
    mu1 = mu*1.67*10**(-27)    
    print (" mass of ion:", m2)
elif ion == 'nit':
    m3 = (1*m_N)+(1*m_O)
    mu = (m3*mm)/(m3+mm)
    mu1 = mu*1.67*10**(-27)
    print (" mass of ion:", m3)
elif ion == 'oxy':
    m4 = (2*m_O)
    mu = (m4*mm)/(m4+mm)
    mu1 = mu*1.67*10**(-27)
    print (" mass of ion:", m4)
#print mu
print ("reduced mass is:", mu1)
#===============================================================================
import math

#k_L = sqrt((pi*alpha*q**2)/mu*epsilon)


#polarizability =float(input("\n  Enter polarizability in ang^3 : "))
#dipole_moment =float(input("\n  Enter dipole moment in Debye: "))
#==================================================================================
def tem_150():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.075,0.120,0.151,0.174,0.191,0.205,0.216,0.225,0.232,0.238,0.243,0.247,0.251,0.253,0.256,0.258,0.260,0.262,0.263,0.264,0.266,0.267,0.268,0.269])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_200():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.065,0.103,0.135,0.159,0.177,0.192,0.204,0.213,0.222,0.229,0.234,0.239,0.244,0.248,0.251,0.254,0.256,0.258,0.260,0.261,0.263,0.264,0.265,0.267])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_250():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array  ([0.054,0.094,0.124,0.147,0.166,0.181,0.193,0.204,0.213,0.220,0.227,0.232,0.237,0.241,0.245,0.248,0.251,0.254,0.256,0.258,0.260,0.262,0.264,0.265])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_300():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.045,0.084,0.115,0.137,0.156,0.172,0.185,0.196,0.205,0.213,0.220,0.226,0.231,0.235,0.240,0.243,0.247,0.250,0.252,0.255,0.257,0.259,0.260,0.262])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_350():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.039,0.076,0.106,0.130,0.149,0.164,0.178,0.189,0.198,0.206,0.213,0.220,0.225,0.230,0.234,0.238,0.242,0.245,0.248,0.251,0.253,0.255,0.257,0.259])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_400():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.034,0.070,0.100,0.125,0.144,0.159,0.171,0.182,0.192,0.201,0.208,0.214,0.220,0.225,0.230,0.234,0.238,0.241,0.244,0.247,0.250,0.252,0.254,0.256])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_450():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.030,0.064,0.094,0.118,0.138,0.155,0.167,0.178,0.187,0.195,0.203,0.210,0.215,0.221,0.226,0.230,0.234,0.237,0.241,0.243,0.246,0.249,0.251,0.253])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

def tem_500():
    mua = np.array([0.163,0.250,0.327,0.408,0.490,0.572,0.653,0.735,0.817,0.898,0.980,1.061,1.143,1.225,1.306,1.388,1.470,1.551,1.633,1.715,1.796,1.878,1.960,2.041])
    C = np.array([0.027,0.061,0.090,0.114,0.134,0.151,0.164,0.175,0.184,0.191,0.198,0.205,0.211,0.217,0.222,0.226,0.230,0.234,0.237,0.240,0.243,0.246,0.248,0.250])
    f = interpolate.interp1d(mua,C)
    newC = f(z)
    return (newC)

dipole_moment = float(input("Enter value of dipole moment :"))
polarizability = float(input("Enter value of polarizability :"))
z = dipole_moment/math.sqrt(polarizability)

#print(z)
C150 = tem_150()
C200 = tem_200()
C250 = tem_250()
C300 = tem_300()
C350 = tem_350()
C400 = tem_400()
C450 = tem_450()
C500 = tem_500()

print(C150)
print(C200)
print(C250)
print(C300)
print(C350)
print(C400)
print(C450)
print(C500)



mua1 = np.array([150,200,250,300,350,400,450,500])
C1 = np.array([C150,C200,C250,C300,C350,C400,C450,C500])

f = interpolate.interp1d(mua1,C1, fill_value='extrapolate')
T1 = 80
T2 = 100
T3 = 550
T4 = 600
print("------------------>")
print (f(T1))
print (f(T2))
print (f(T3))
print (f(T4))

val1 = f(T1)
val2 = f(T2)
val3 = f(T3)
val4 = f(T4)

list = np.array([val1,val2,C150,C200,C250,C300,C350,C400,C450,C500,val3,val4])
#print (list[0])
list1 = np.array([80,100,150,200,250,300,350,400,450,500,550,600])
#print (list1)
dict1 = zip(list1, list)
dict2 = dict(dict1)
#print (dict2)
#print (dict2[250])

T =float(input("\n  Enter value of temperature: "))
#for key, value in dict2.items():
#    print (key, value)

for i in list1:
    if i == T:
        C = dict2[i]
        print ("number is found", C)

#==================================================================================
#T = 380
alpha = polarizability*10**(-30)
DM = dipole_moment*3.336*10**(-30)


epsilon = 8.854*10**(-12)     # J^-1.C^2.m^-1
q = 1.602*10**(-19)           # C
#mu = 2.38*10**(-26)           # reduced mass
part1 = math.pi*alpha*q**2
part2 = mu1*epsilon
#print part1
#print part2
#print mu2
K_L = math.sqrt(part1/part2)
print (K_L)
#----------------------------------------Langavin

#part3 = C*muD*q/epsilon
part3 = (C*DM*q)/epsilon

k_b = 1.38*10**(-23)

#part4 = sqrt(1/(2.pi.mu.k_b.T))
part4 = math.sqrt(1/(2*math.pi*mu1*k_b*T))
part5 = part3*part4
K_ADO = (K_L+part5)*10**(6)

print ("\n Rate Constant at", T, "K is:", "%.4e" % K_ADO, " cm^3.s^-1")


#------------------------------K_cap(CT)-------------------















