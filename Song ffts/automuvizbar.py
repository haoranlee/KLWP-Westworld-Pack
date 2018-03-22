#! /usr/bin/python

fftdict={}
for i in range(0,20):
	fftdict[i]={}

infile = open(r'C:\Users\Hao Ran Lee\Downloads\Song ffts\The 1975 - Chocolate_10sec_fft.txt','r')
for line in infile:
	fftlist=line.split(',')
	for i in range(0,20):
		fftdict[i][fftlist[0]]=fftlist[i+1]

barmax = [float(max(fftdict[i].values())) for i in range(0,20)]
infile.close()

outfile = {}
outviz = {}
for i in range(0,20):
	outfile[i] = open(r'C:\Users\Hao Ran Lee\Downloads\Song ffts\The 1975 - Chocolate_10sec_muviz' + '{:0>2d}'.format(i+1) + '.txt','w')
	outviz[i] = '''##KUSTOMCLIP##
{
  "clip_version": 1,
  "clip_cut": [],
  "clip_modules": [
    {
      "internal_type": "ProgressModule",
      "internal_title": "Muviz''' + '{:0>2d}'.format(i+1) + '''",
      "internal_toggles": {
        "position_offset_x": 10,
        "style_size": 10,
        "color_fgcolor": 100,
        "progress_progress": 0,
        "progress_max": 0,
        "progress_level": 10,
        "progress_count": 10
      },
      "internal_formulas": {
        "position_offset_x": "$gv(textmarg)+(686/159*8*(''' + str(i+1) + '''-1))$",
        "style_size": "$686/159*7$",
        "progress_level": "$mu(min,100,mu(max,0,(mi(pos)-(8*(''' + str(i+1) + '''-1)*(mi(len)/159)))/(7*(mi(len)/159))*100))$",
        "progress_count": "$mu(ceil,mi(len)/159*7)$"
      },
      "internal_globals": {
        "color_fgcolor": "blue"
      },
      "position_anchor": "BOTTOMLEFT",
      "position_offset_y": 1075.0,
      "progress_progress": "CUSTOM",
      "progress_level": 71.0,
      "progress_count": 20.0,
      "style_height": 105.0,
      "color_bgcolor": "#FFFFFFFF",
      "internal_animations": [
        {
          "type": "FORMULA",
          "formula": "$if(br(tasker,launch)\\u003d1,f,r)$",
          "action": "ADVANCED",
          "duration": 3.0,
          "delay": 12.0,
          "animator": [
            {
              "position": 0,
              "value": 0.0,
              "property": "SCALE_Y",
              "ease": "NORMAL"
            },
            {
              "position": 100,
              "value": ''' + str(0.05+0.95*barmax[i]/max(barmax)) + ''',
              "property": "SCALE_Y",
              "ease": "NORMAL"
            }
          ],
          "anchor": "MODULE_BOTTOM_LEFT"
        },'''

for k in fftdict[0].keys():
	for i in range(0,20):
		if k[2:] == '0.0':
			if int(float(k))>0:
				outviz[i] += '''
            {
              "position": 100,
              "value": ''' + str(0.05 + 0.95*float(fftdict[i][k])/barmax[i]) + ''',
              "property": "SCALE_Y",
              "ease": "STRAIGHT"
            }
          ],
          "anchor": "MODULE_BOTTOM_LEFT"
        }'''
				if int(float(k))!=60:
					outviz[i] += ','
				else:
					outviz[i] += '''
      ]
    }
  ]
}
##KUSTOMCLIP##'''
			if int(float(k))<60:
				outviz[i] += '''
        {
          "type": "FORMULA",
          "formula": "$if(mi(state)\\u003dPLAYING\\u0026tf(mi(pos),ss)\\u003e\\u003d''' + str(int(float(k))+0) + '\\u0026tf(mi(pos),ss)\\u003c' + str(int(float(k))+10) + ''',f,r)$",
          "action": "ADVANCED",
          "ease": "STRAIGHT",
          "duration": 100.0,
          "animator": ['''
		else:
			outviz[i] += '''
            {
              "position": ''' + str(int(float(k[2:])*10)) + ''',
              "value": ''' + str(0.05 + 0.95*float(fftdict[i][k])/barmax[i]) + ''',
              "property": "SCALE_Y",
              "ease": "STRAIGHT"
            },'''

for i in range(0,20):
	outfile[i].write(outviz[i])
	outfile[i].close()

if False:
	if False:
		if False:
			secint = int(float(k))
			outviz[i] += '            {\n              "position": 100,\n              "value": ' + str(0.05 + 0.95*float(fftdict[i][k])/barmax[i]) + ',\n              "property": "SCALE_Y",\n            "ease": "STRAIGHT"\n            }\n          ],\n          "anchor": "MODULE_BOTTOM_LEFT"\n        },\n        {\n          "type": "FORMULA",\n          "formula": "$if(mi(state)\\u003dPLAYING\\u0026mi(pos)\\u003e\\u003d' + str(secint) + '\\u0026mi(pos)\\u003c' + str(secint+10) + ',f,r)$",\n          "action": "ADVANCED",\n          "ease": "STRAIGHT",\n          "duration": 100.0,\n          "animator": [\n'
		else:
			outviz[i] += '            {\n              "position": ' + str(int(float(k[2:])*10)) + ',\n              "value": ' + str(0.05 + 0.95*float(fftdict[i][k])/barmax[i]) + ',\n    "property": "SCALE_Y",\n              "ease": "STRAIGHT"\n            },\n'