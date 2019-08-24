def f(l1,l2,l3): 
    dll = l1 + l2 + l3
    det = l1 * l2 * l3
    if (l1 == 0.):
        ell = -0.1
    else:
        den = det / 126. + 5.*l1*dll*(dll-l1) / 84.      
        if (den == 0.):
            if (dll == l1):
                if ( l1 > 0.0 ):
                    ell = 1.0 / l1
                else:
                    ell=-0.1
            else:
                dis = 7.*l1* (l1+6.*dll)
                
                if(dis < 0.0):
                    ell = -0.1
                else:
                    ell = (7.*l1 - math.sqrt(dis)) / (3.*l1*(l1-dll))
                    if ( ell < 0.0 ): 
                        ell = -0.1
        else:
            rden = 1.0 / den
            a1   = 3.*l1*(dll-l1) /14. * rden
            a1_2 = a1*a1
            a2 = l1 * rden
            a3 = -1.0 * rden
            q  = (a1_2 - 3.*a2) / 9.
            r  = (2.* a1_2*a1 - 9.*a1*a2 + 27.*a3) / 54.
            r_2_q_3 = r*r-q*q*q
            if (r_2_q_3 > 0):
                fabs_r = abs(r)
                sq  = (math.sqrt(r_2_q_3) + fabs_r)**0.333333333333333 
                ell = -fabs_r / r * (sq+q/sq) - a1/3.
                if ( ell < 0.0 ): 
                    ell = -0.1
            else:
                sq    = 2*math.sqrt(q)
                inv_3 = 1.0/3
                t     = math.acos(2*r/q/sq)
                s1 = -sq*math.cos(t * inv_3)-a1 * inv_3
                s2 = -sq*math.cos((t+2.*PI) * inv_3) - a1 * inv_3
                s3 = -sq*math.cos((t+4.*PI) * inv_3) - a1 * inv_3
                  
                if ( s1 < 0.0 ):
                    s1 = 1.e10
                   
                if ( s2 < 0.0 ):
                    s2 = 1.e10
                  
                if ( s3 < 0.0 ): 
                    s3 = 1.e10
                  
                ell = (s1 if s1 < s2 else s2)
                ell = (s3 if s3 <ell else ell)
                if ( ell == 1.e10 ):
                    ell = -0.1
    if (dll > 0.0 and ell > 0.0):
        inv_dll = 1.0 / dll
        ell+= -0.364 * inv_dll * math.exp(-6.5*(l1-l2)*inv_dll-2.8*(l2-l3)*inv_dll)
    return ell
