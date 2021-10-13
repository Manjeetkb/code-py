import math
c1 = 0.727143
c2 = 3.71823
c3 = 0.586920
c4 = 4.97894
#v = 930
T = 300
M = 28.8                        #buffer gas
m_H = 1.00794
m_C = 12.0107
m_O = 15.999
m_N = 14.0067
#m = (3*m_H)+(1*m_O)
#m = (4*m_H)+(1*m_N)
#m = (1*m_N)+(1*m_O)
m = (2*m_O)
print ("\n  mass of the ion:", m)
print ("\n  Temperature is:", T)
m1 = m*1.67*10**(-27) 
M1 = M*1.67*10**(-27)
k_b  = 1.38*10**-23
mol = input("Enter name of the molecule: ")
mm = float(input("Enter mass neutral molecule (a.m.u.): "))
dipole_moment =float(input("\n Enter dipole moment in Debye: "))
plz =float(input("\n Enter polarizability in Ang^3 : "))
K_Lang = float(input("\n Enter value of K_Lang: "))
f = open((mol), 'w')
f.write("..............>>>>Name of the molecule: %s"" \r\n" % (mol))
f.write("\n  Temperature in the drift tube: %.0f"" K\r\n" % T)
f.write("\n  Dipole moment of molecule: %.2f"" Debye\r\n" % dipole_moment)
f.write("\n  Polarizability of molecule: %.2f"" Ang^3\r\n" % plz)
f.write("\n  Langevin collision rate: %.2f"" 10^-9cm^3s^-1\r\n" % K_Lang)

list = (585,739,906,1083,1290,1470)
for i in list:
    print (i)
    if i == 585:
        print ("number found", i)
        v = i*i
        E1 = 0.5*(m1*v)
        E2 = 0.5*(M1*v)
        E3 = 1.5*(k_b*T)
        E3_ev = E3*6.24*10**(18)
        KE_ion = E1+E2+E3
        KE_ion_ev = KE_ion*6.24*10**(18)
        print ("Kinetic energy of ion : ", KE_ion_ev, "eV", i, "m/s")
#        print "calculation for COM energy:..........."
        ms = (mm)/(mm+m)
        print (ms)
#        print E3_ev
        ke = (KE_ion_ev-E3_ev)
        KE_cm = E3_ev+(ms*ke)
        print ("COM Kinetic energy : ", KE_cm, "eV", i, "m/s")
        tau = dipole_moment/math.sqrt(plz*T)
        print ("value of tau is :", tau)

        eps = dipole_moment/math.sqrt(plz*KE_cm)
        print ("value of eps is : ", eps)
        theta = c3*(c4+math.log(tau))
        #print theta

        if eps > 1.5:
            S = math.exp(-2*(eps-1.5))
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)
            K_c3 = math.sin(theta)
            K_c4 = tau**(0.6)
            K_c5 = math.sqrt(eps-0.5)
            print (S)
#            print K_c2
#            print K_c3
#            print K_c4
#            print K_c5
            K_c6 = K_c2*K_c3*K_c4*K_c5
#            print K_c6
            K_c = 1+K_c1+K_c6
            K_cap = K_Lang*K_c
#            print "Value of K_c(tau,eps): ", K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
        elif eps <= 1.5:
            S = 1
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)*math.sin(theta)
        #   K_c3 = tau**(0.6)*math.sqrt(eps-0.5)
            K_c = 1+K_c1+K_c2
        #   print K_c1
        #   print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
#============================================end of E/N=80===========================================
    elif i == 739:
        print ("number found", i)
        v = i*i
        E1 = 0.5*(m1*v)
        E2 = 0.5*(M1*v)
        E3 = 1.5*(k_b*T)
        E3_ev = E3*6.24*10**(18)
        KE_ion = E1+E2+E3
        KE_ion_ev = KE_ion*6.24*10**(18)
        print ("Kinetic energy of ion and velocity : ", KE_ion_ev, "eV", i, "m/s")
#        print "calculation for COM energy:..........."
        ms = (mm)/(mm+m)
        print (ms)
#        print E3_ev
        ke = (KE_ion_ev-E3_ev)
        KE_cm = E3_ev+(ms*ke)
        print ("COM Kinetic energy : ", KE_cm, "eV", i, "m/s")
        tau = dipole_moment/math.sqrt(plz*T)
        print ("value of tau is :", tau)

        eps = dipole_moment/math.sqrt(plz*KE_cm)
        print ("value of eps is : ", eps)
        theta = c3*(c4+math.log(tau))
        #print theta

        if eps > 1.5:
            S = math.exp(-2*(eps-1.5))
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)
            K_c3 = math.sin(theta)
            K_c4 = tau**(0.6)
            K_c5 = math.sqrt(eps-0.5)
            print (S)
#            print K_c2
#            print K_c3
#            print K_c4
#            print K_c5
            K_c6 = K_c2*K_c3*K_c4*K_c5
#            print K_c6
            K_c = 1+K_c1+K_c6
#            print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
#            print "Value of K_c(tau,eps): ", K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
        elif eps <= 1.5:
            S = 1
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)*math.sin(theta)
        #   K_c3 = tau**(0.6)*math.sqrt(eps-0.5)
            K_c = 1+K_c1+K_c2
        #   print K_c1
        #   print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
#==============================================end of E/N=100========================================
    elif i == 906:
        print ("number found", i)
        v = i*i
        E1 = 0.5*(m1*v)
        E2 = 0.5*(M1*v)
        E3 = 1.5*(k_b*T)
        E3_ev = E3*6.24*10**(18)
        KE_ion = E1+E2+E3
        KE_ion_ev = KE_ion*6.24*10**(18)
        print ("Kinetic energy of ion : ", KE_ion_ev, "eV", i, "m/s")
#        print "calculation for COM energy:..........."
        ms = (mm)/(mm+m)
        print (ms)
#        print E3_ev
        ke = (KE_ion_ev-E3_ev)
        KE_cm = E3_ev+(ms*ke)
        print ("COM Kinetic energy : ", KE_cm, "eV", i, "m/s")
        tau = dipole_moment/math.sqrt(plz*T)
        print ("value of tau is :", tau)

        eps = dipole_moment/math.sqrt(plz*KE_cm)
        print ("value of eps is : ", eps)
        theta = c3*(c4+math.log(tau))
        #print theta

        if eps > 1.5:
            S = math.exp(-2*(eps-1.5))
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)
            K_c3 = math.sin(theta)
            K_c4 = tau**(0.6)
            K_c5 = math.sqrt(eps-0.5)
            print (S)
#            print K_c2
#            print K_c3
#            print K_c4
#            print K_c5
            K_c6 = K_c2*K_c3*K_c4*K_c5
#            print K_c6
            K_c = 1+K_c1+K_c6
#            print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
#            print "Value of K_c(tau,eps): ", K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
        elif eps <= 1.5:
            S = 1
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)*math.sin(theta)
        #   K_c3 = tau**(0.6)*math.sqrt(eps-0.5)
            K_c = 1+K_c1+K_c2
        #   print K_c1
        #   print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
#===================================================end of E/N=120============================================
    elif i == 1083:
        print ("number found", i)
        v = i*i
        E1 = 0.5*(m1*v)
        E2 = 0.5*(M1*v)
        E3 = 1.5*(k_b*T)
        E3_ev = E3*6.24*10**(18)
        KE_ion = E1+E2+E3
        KE_ion_ev = KE_ion*6.24*10**(18)
        print ("Kinetic energy of ion : ", KE_ion_ev, "eV", i, "m/s")
#        print "calculation for COM energy:..........."
        ms = (mm)/(mm+m)
        print (ms)
#        print E3_ev
        ke = (KE_ion_ev-E3_ev)
        KE_cm = E3_ev+(ms*ke)
        print ("COM Kinetic energy : ", KE_cm, "eV", i, "m/s")
        tau = dipole_moment/math.sqrt(plz*T)
        print ("value of tau is :", tau)

        eps = dipole_moment/math.sqrt(plz*KE_cm)
        print ("value of eps is : ", eps)
        theta = c3*(c4+math.log(tau))
        #print theta

        if eps > 1.5:
            S = math.exp(-2*(eps-1.5))
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)
            K_c3 = math.sin(theta)
            K_c4 = tau**(0.6)
            K_c5 = math.sqrt(eps-0.5)
            print (S)
#            print K_c2
#            print K_c3
#            print K_c4
#            print K_c5
            K_c6 = K_c2*K_c3*K_c4*K_c5
#            print K_c6
            K_c = 1+K_c1+K_c6
#            print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("Value of K_c(tau,eps): ", K_c)
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
        elif eps <= 1.5:
            S = 1
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)*math.sin(theta)
        #   K_c3 = tau**(0.6)*math.sqrt(eps-0.5)
            K_c = 1+K_c1+K_c2
        #   print K_c1
        #   print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
#=======================================================end of E/N=140========================================
    elif i == 1290:
        print ("number found", i)
        v = i*i
        E1 = 0.5*(m1*v)
        E2 = 0.5*(M1*v)
        E3 = 1.5*(k_b*T)
        E3_ev = E3*6.24*10**(18)
        KE_ion = E1+E2+E3
        KE_ion_ev = KE_ion*6.24*10**(18)
        print ("Kinetic energy of ion : ", KE_ion_ev, "eV", i, "m/s")
#        print "calculation for COM energy:..........."
        ms = (mm)/(mm+m)
        print (ms)
#        print E3_ev
        ke = (KE_ion_ev-E3_ev)
        KE_cm = E3_ev+(ms*ke)
        print ("COM Kinetic energy : ", KE_cm, "eV", i, "m/s")
        tau = dipole_moment/math.sqrt(plz*T)
        print ("value of tau is :", tau)

        eps = dipole_moment/math.sqrt(plz*KE_cm)
        print ("value of eps is : ", eps)
        theta = c3*(c4+math.log(tau))
        #print theta

        if eps > 1.5:
            S = math.exp(-2*(eps-1.5))
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)
            K_c3 = math.sin(theta)
            K_c4 = tau**(0.6)
            K_c5 = math.sqrt(eps-0.5)
            print (S)
#            print K_c2
#            print K_c3
#            print K_c4
#            print K_c5
            K_c6 = K_c2*K_c3*K_c4*K_c5
#            print K_c6
            K_c = 1+K_c1+K_c6
#            print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
#            print "Value of K_c(tau,eps): ", K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
        elif eps <= 1.5:
            S = 1
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)*math.sin(theta)
        #   K_c3 = tau**(0.6)*math.sqrt(eps-0.5)
            K_c = 1+K_c1+K_c2
        #   print K_c1
        #   print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
#=====================================================end of E/N=160===================================
    elif i == 1470:
        print ("number found", i)
        v = i*i
        E1 = 0.5*(m1*v)
        E2 = 0.5*(M1*v)
        E3 = 1.5*(k_b*T)
        E3_ev = E3*6.24*10**(18)
        KE_ion = E1+E2+E3
        KE_ion_ev = KE_ion*6.24*10**(18)
        print ("Kinetic energy of ion : ", KE_ion_ev, "eV", i, "m/s")
#        print "calculation for COM energy:..........."
        ms = (mm)/(mm+m)
        print (ms)
#        print E3_ev
        ke = (KE_ion_ev-E3_ev)
        KE_cm = E3_ev+(ms*ke)
        print ("COM Kinetic energy : ", KE_cm, "eV", i, "m/s")
        tau = dipole_moment/math.sqrt(plz*T)
        print ("value of tau is :", tau)

        eps = dipole_moment/math.sqrt(plz*KE_cm)
        print ("value of eps is : ", eps)
        theta = c3*(c4+math.log(tau))
        #print theta

        if eps > 1.5:
            S = math.exp(-2*(eps-1.5))
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)
            K_c3 = math.sin(theta)
            K_c4 = tau**(0.6)
            K_c5 = math.sqrt(eps-0.5)
#            print S
#            print K_c2
#            print K_c3
#            print K_c4
 #           print K_c5
#            K_c6 = K_c2*K_c3*K_c4*K_c5
#            print K_c6
            K_c = 1+K_c1+K_c6
#            print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
#            print "Value of K_c(tau,eps): ", K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
        elif eps <= 1.5:
            S = 1
            a = tau**(0.4)
            b = eps*eps
            K_c1 = c1*a*b*S
            K_c2 = c2*(1-S)*math.sin(theta)
        #   K_c3 = tau**(0.6)*math.sqrt(eps-0.5)
            K_c = 1+K_c1+K_c2
        #   print K_c1
        #   print "Value of K_c(tau,eps): ", K_c
            K_cap = K_Lang*K_c
            print ("..............>>>>>\n      The Capture rate constant k_cap is :  ", K_cap, "10^(-9)cm^3 s^-1", "@", i, "m/s")
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  ")
            f.write("\n  Velocity of ions in drift tube: %.0f"" m/s\r\n" % i)
            f.write("\n  Total kinetic energy of ion: %.5f"" eV\r\n" % KE_ion_ev)
            f.write("\n  COM kinetic energy of ion-molecule collision: %.5f"" eV\r\n" % KE_cm)
            f.write("\n  Capture collision rate constant: %.2f"" 10^(-9)cm^3 s^-1\r\n" % K_cap)
            f.write("............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
#===============================================================================
#mol = raw_input("Enter name of the molecule: ")
#f = open((mol), 'w')
#f.write()
#f.write("\n  Temperature in the drift tube: %f"" K\r\n" % T)
#f.write("\n  Total kinetic energy of ion: %f"" eV\r\n" % KE_ion_ev)
#f.write("\n  COM kinetic energy of ion-molecule collision: %f"" eV\r\n" % #KE_cm)
#f.write("\n  Dipole moment of molecule: %f"" Debye\r\n" % dipole_moment)
#f.write("\n  Polarizability of molecule: %f"" Ang^3\r\n" % plz)
#f.write("\n  Langevin collision rate: %f"" 10^-9cm^3s^-1\r\n" % K_Lang)
#f.write("\n  Capture collision rate constant: %f"" 10^(-9)cm^3 s^-1\r\n" % #K_cap)
#f.write("Calculated values are:\r\n")
#f.write("\n  Velocity in the drift tube: %f"" K\r\n" % T)
f.close()
