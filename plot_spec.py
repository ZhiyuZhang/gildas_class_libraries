import matplotlib.pyplot as plt
import numpy as np
import os
from   astropy.io import fits
import astropy.units as u
import sys, copy
from   astropy.io import ascii
import matplotlib.style
import matplotlib as mpl
import matplotlib.ticker as plticker
mpl.style.use('classic')
import matplotlib.pylab as pylab
params = {'legend.fontsize': 15,
         'axes.labelsize'  : 15,
         'axes.titlesize'  : 15,
         'xtick.labelsize' : 15,
         'ytick.labelsize' : 15}
pylab.rcParams.update(params)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']


# ------------------------------- 
etamb       = 0.64
modx        = [-350, 350]

#window      = [-200, 250]
#SourceName  = r"Arp299"
#Line        = r"HCN $J=4\rightarrow3$"
#targ        = 'arp299'
#linename    = 'hcn'


#window      = [-200, 250]
#SourceName  = r"Arp299"
#Line        = r"HCO$^+$ $J=4\rightarrow3$"
#targ        = 'arp299'
#linename    = 'hcop'


#window      = [-180, 150]
#SourceName  = r"NGC253"
#Line        = r"HCN $J=4\rightarrow3$"
#targ        = 'n253'
#linename    = 'hcn'

#window      = [-180, 150]
#SourceName  = r"NGC253"
#Line        = r"HCO$^+$ $J=4\rightarrow3$"
#targ        = 'n253'
#linename    = 'hcop'

#window      = [-220, 200]
#SourceName  = r"NGC660"
#Line        = r"HCN $J=4\rightarrow3$"
#targ        = 'n660'
#linename    = 'hcn'
#ytick_step  = 5
#err_step    = 1 

modx        = [-350, 350]
window      = [-220, 200]
SourceName  = r"NGC660"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n660'
linename    = 'hcop'
ytick_step  = 5
err_step    = 1 


modx        = [-350, 350]
window      = [-120, 150]
SourceName  = r"NGC891"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n891'
linename    = 'hcn'
ytick_step  = 5
err_step    = 1 

modx        = [-350, 350]
window      = [-120, 150]
SourceName  = r"NGC891"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n891'
linename    = 'hcop'
ytick_step  = 10 
err_step    = 2 


modx        = [-350, 350]
window      = [-200, 100]
SourceName  = r"Maffei2"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'maffei2'
linename    = 'hcn'
ytick_step  = 10 
err_step    = 2 

modx        = [-350, 350]
window      = [-200, 100]
SourceName  = r"Maffei2"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'maffei2'
linename    = 'hcop'
ytick_step  = 10 
err_step    = 2 

modx        = [-350, 350]
window      = [-200, 150]
SourceName  = r"NGC1068"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n1068'
linename    = 'hcn'
ytick_step  = 10 
err_step    = 2 

modx        = [-350, 350]
window      = [-200, 150]
SourceName  = r"NGC1068"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n1068'
linename    = 'hcop'
ytick_step  = 10 
err_step    = 5 

modx        = [-350, 350]
window      = [-120, 150]
SourceName  = r"NGC1097"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n1097'
linename    = 'hcn'
ytick_step  = 5  
err_step    = 2 

modx        = [-350, 350]
window      = [-120, 150]
SourceName  = r"NGC1097"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n1097'
linename    = 'hcop'
ytick_step  =  5 
err_step    = 1 

modx        = [-350, 350]
window      = [-170, 150]
SourceName  = r"NGC1365"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n1365'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 5 

modx        = [-350, 350]
window      = [-50,  50]
SourceName  = r"IC342"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'ic342'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 2 

modx        = [-350, 350]
window      = [-50, 50]
SourceName  = r"IC342"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'ic342'
linename    = 'hcop'
ytick_step  = 20 
err_step    = 2 


modx        = [-350, 350]
window      = [-150,  200]
SourceName  = r"NGC1808"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n1808'
linename    = 'hcn'
ytick_step  = 10 
err_step    = 2 


modx        = [-350, 350]
window      = [-150,  200]
SourceName  = r"NGC1808"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n1808'
linename    = 'hcop'
ytick_step  = 10 
err_step    = 2 

modx        = [-350, 350]
window      = [-150,  200]
SourceName  = r"NGC2146"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n2146'
linename    = 'hcn'
ytick_step  = 10 
err_step    = 5 

modx        = [-350, 350]
window      = [-150,  200]
SourceName  = r"NGC2146"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n2146'
linename    = 'hcop'
ytick_step  = 10 
err_step    = 1 

modx        = [-350, 350]
window      = [-150,  150]
SourceName  = r"NGC2903"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n2903'
linename    = 'hcn'
ytick_step  = 5 
err_step    = 1 

modx        = [-350, 350]
window      = [-150,  150]
SourceName  = r"NGC2903"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n2903'
linename    = 'hcop'
ytick_step  = 5  
err_step    = 0.5 

modx        = [-350, 350]
window      = [-150,  150]
SourceName  = r"M82"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'm82'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 2 

modx        = [-350, 350]
window      = [-150,  150]
SourceName  = r"M82"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'm82'
linename    = 'hcop'
ytick_step  = 50 
err_step    = 2 

modx        = [-350, 350]
window      = [-200,  200]
SourceName  = r"NGC3079"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n3079'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 2 

modx        = [-350, 350]
window      = [-200,  200]
SourceName  = r"NGC3079"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n3079'
linename    = 'hcop'
ytick_step  = 20 
err_step    = 2 

modx        = [-350, 350]
window      = [-200,  200]
SourceName  = r"NGC3521"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n3521'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 2 

modx        = [-350, 350]
window      = [-200,  200]
SourceName  = r"NGC3521"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n3521'
linename    = 'hcop'
ytick_step  = 5  
err_step    = 2 

modx        = [-350, 350]
window      = [-150, 150]
SourceName  = r"NGC3627"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n3627'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 2 

modx        = [-350, 350]
window      = [-150, 150]
SourceName  = r"NGC3627"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n3627'
linename    = 'hcop'
ytick_step  = 5  
err_step    = 2 

modx        = [-350, 350]
window      = [-150, 200]
SourceName  = r"NGC3628"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n3628'
linename    = 'hcn'
ytick_step  = 20 
err_step    = 1 

modx        = [-350, 350]
window      = [-150, 200]
SourceName  = r"NGC3628"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n3628'
linename    = 'hcop'
ytick_step  = 10  
err_step    = 1 

modx        = [-350, 350]
window      = [-200, 200]
SourceName  = r"NGC4631"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n4631'
linename    = 'hcn'
ytick_step  = 5  
err_step    = 2 

modx        = [-350, 350]
window      = [-200, 200]
SourceName  = r"NGC4631"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n4631'
linename    = 'hcop'
ytick_step  = 5   
err_step    = 2 

modx        = [-350, 350]
window      = [-150, 150]
SourceName  = r"NGC4736"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n4736'
linename    = 'hcn'
ytick_step  = 5  
err_step    = 0.5  

modx        = [-350, 350]
window      = [-150, 150]
SourceName  = r"NGC4736"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n4736'
linename    = 'hcop'
ytick_step  = 5   
err_step    = 1 

modx        = [-350, 350]
window      = [-100, 100]
SourceName  = r"M83"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'm83'
linename    = 'hcn'
ytick_step  = 20  
err_step    = 2  

modx        = [-350, 350]
window      = [-100, 100]
SourceName  = r"M83"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'm83'
linename    = 'hcop'
ytick_step  = 20  
err_step    = 2  

modx        = [-350, 350]
window      = [-200, 200]
SourceName  = r"NGC5457"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n5457'
linename    = 'hcn'
ytick_step  = 5  
err_step    = 0.5  

modx        = [-350, 350]
window      = [-200, 200]
SourceName  = r"NGC5457"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n5457'
linename    = 'hcop'
ytick_step  = 5   
err_step    = 1  

modx        = [-350, 350]
window      = [-100, 100]
SourceName  = r"NGC6946"
Line        = r"HCN $J=4\rightarrow3$"
targ        = 'n6946'
linename    = 'hcn'
ytick_step  = 20  
err_step    = 2  

modx        = [-350, 350]
window      = [-100, 100]
SourceName  = r"NGC6946"
Line        = r"HCO$^+$ $J=4\rightarrow3$"
targ        = 'n6946'
linename    = 'hcop'
ytick_step  = 20   
err_step    = 2  


 
#window      = [-200, 200]
#SourceName  = r"NGC3079"
#Line        = r"HCN $J=4\rightarrow3$"
#targ        = 'n3079'
#linename    = 'hcn'



# -------------------------------


# -- plotting
plt.clf()
f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
plt.subplots_adjust(wspace=0, hspace=0.0)
box           = ax2.get_position()
ax2.set_position([box.x0, box.y0+box.height*0.6, box.width, box.height * 0.4 ])

ax1.set_xlim(modx)
velo, spec = np.loadtxt('/data/malatang/plotting/'+targ+'/'+linename+'/averaged_spectrum.dat',  unpack = True)
spec       = spec * 1000 / etamb 
winchans   = np.where( (velo >= np.min(window)) & (velo <= np.max(window)))

ax1.hlines(0,np.min(velo),np.max(velo), color=new_colors[0],linewidth=2)
ax1.fill_between(velo[winchans],spec[winchans], step="mid", alpha=0.4,color=new_colors[0],interpolate=True)
ax1.step(        velo,spec, linewidth=1,  label=SourceName,where='mid',color='black')
ax1.set_ylabel(r'$T_{\rm mb}$ (mK)', labelpad=3)
ax1.legend(loc=2,title=Line,prop={'size':15},frameon=None,)

loc = plticker.MultipleLocator(base=ytick_step) # this locator puts ticks at regular intervals
ax1.yaxis.set_major_locator(loc)
ax1.set_ylim(np.min(spec)*1.1,np.max(spec)*1.5) 

velo, spec = np.loadtxt('/data/malatang/plotting/'+targ+'/'+linename+'/noise_spectrum.dat',  unpack=True)
spec       = spec * 1000 / etamb 
ax2.fill_between(velo[winchans],spec[winchans], step="mid", alpha=0.1,color=new_colors[0])
ax2.step(        velo,spec, linewidth=1,  label='Noise',where='mid',color=new_colors[0])
ax2.legend( loc=2, borderaxespad=0.,prop={'size':15},frameon=None)

ax2.set_ylim(np.min(spec)*0.9,np.max(spec)*1.1) 
ax2.set_xlabel(r'Relative Velocity ($\rm km\ s^{-1}$)', labelpad=3)
ax2.set_ylabel(r'$T_{\rm mb}$ (mK)', labelpad=3)
loc = plticker.MultipleLocator(base=err_step) # this locator puts ticks at regular intervals
ax2.yaxis.set_major_locator(loc)

plt.savefig(SourceName+"-"+str(Line)[0:3]+'.pdf',bbox_inches='tight', pad_inches=0.1)

os.system("open "+SourceName+"-"+str(Line)[0:3]+'.pdf')
