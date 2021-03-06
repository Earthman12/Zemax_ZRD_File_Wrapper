# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:      arrayTraceNSCdemo.py
# Purpose:   demonstrate the function zGetNSCTraceArray() in the module
#            pyzdde.arraytrace for performing NSC ray tracing. This demo
#            is emulates the "NSCTraceDemo.c" external program that is
#            shipped with Zemax.
#
# Author:     Indranil Sinharoy
#
# Created:    Mon Mar 02 00:06:19 2015
# Copyright:  (c) Indranil Sinharoy, 2012 - 2015
# Licence:    MIT License
#-------------------------------------------------------------------------------
from __future__ import print_function, division
import pyzdde.arraytrace as at  # Module for array ray tracing
import pyzdde.zdde as pyz

# NOTE: The program assumes that an appropriate lens design file is already
# loaded into Zemax LDE.

ln = pyz.createLink()
ln.zGetRefresh()
# Get maximum number of segments
maxSeg = ln.zGetNSCSettings().maxSeg
# limit the number maximum number of segments to 50
nMaxSeg = maxSeg if maxSeg < 50 else 50

# Trace a single in NSC mode with polarization and splitting, but no scattering.
rayData = at.zGetNSCTraceArray(n=1, Eyr=1.0, usePolar=1, split=1, nMaxSegments=50)

# Print the output
print("Listing of NSC Trace data:")
print("{:^4} {:^4} {:^4} {:^6} {:^4} {:^14} {:^14} {:^14} {:^12}"
      .format('seg#', 'Prnt', 'Levl', 'In', 'Hit', 'X', 'Y', 'Z', 'Intensity'))

totalSegments = len(rayData)
for i, seg in enumerate(rayData):
    segLevel = seg.segment_level
    segParent = seg.segment_parent
    insideOf = seg.inside_of
    hitObj = seg.hit_object
    x, y, z, l, m, n = seg.x, seg.y, seg.z, seg.l, seg.m, seg.n
    intensity = seg.intensity
    opl = seg.opl
    print("{:4d} {:4d} {:4d} {:4d} {:4d} {:15.6E} {:15.6E} {:15.6E} {:8.4f}"
           .format(i+1, segParent, segLevel, insideOf, hitObj, x, y, z, intensity))

ln.close()