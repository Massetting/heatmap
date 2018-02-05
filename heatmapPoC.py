# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 13:36:39 2018

@author: amassett
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:08:01 2017

@author: amassett
"""
import os
import numpy
import matplotlib.pyplot as plt
location=r"C:\myfolder"
def histo2dim(xx,yy,nbins=5000,minran=0,maxran=10000): 
    edges=numpy.histogram(range(minran,maxran),bins=nbins)[1]   
    binr=numpy.histogram2d(xx,yy, bins=[edges,edges])
    xed,yed=binr[1],binr[2]
    return binr, xed,yed
def plot_it(binr, xed,yed, figsize=[50,50], dpi=300,location=r"C:\myfolder",xlab="",ylab="",xlim=[0,3000],ylim=[0,3000]):
    
    fig = plt.figure(figsize=(figsize[0], figsize[1]), dpi=dpi)
    ax = fig.add_subplot(111)
    ax.set_title('imshow: equidistant')
        
    ax.set_xlim(xlim[0],xlim[1])
    ax.set_ylim(0, 3000)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)

    im = plt.imshow(binr.T, cmap='YlOrRd',clim=(50,10000), interpolation='nearest',origin='low',extent=[xed[0], xed[-1], yed[0], yed[-1]])
    fig.colorbar(im)
    fignam=('figure.jpg')
    fnam=os.path.join(location,fignam)
    fig.savefig(fnam)
    plt.close()    