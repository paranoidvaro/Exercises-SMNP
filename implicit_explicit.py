import numpy as np
s_0 = 1
t_0 = 0
s_je = None
s_ji = None

#Explicit:     sj+1 = sj(1−10∆t)

#Implicit:     sj+1 = sj/(1 + 10∆t)
def forward_explicit(s_0, s_j , delta_t):
    s_j = s_j * (1 - (10 * delta_t))
    return s_j
    
def forward_implicit(s_0, s_j, delta_t):
    s_j = s_j / (1 + (10*delta_t))
    return s_j

times = [0.05, 0.1, 0.2, 0.25]

def compute_time(x, times):
    results = []
    for time in times:
        delta_t = time
        for i in range(x):
            if i == 0:
                s_je = s_0
                s_je = forward_explicit(s_0, s_je, delta_t)
                
                s_ji = s_0
                s_ji = forward_implicit(s_0, s_ji, delta_t)
            else:
                s_je = forward_explicit(s_0, s_je, delta_t)
                
                s_ji = forward_implicit(s_0, s_ji, delta_t)
                
        results.append({f'{time}': [s_je, s_ji]})
    return results

        
    
print(compute_time(4, times))