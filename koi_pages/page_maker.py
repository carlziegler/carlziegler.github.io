import os, io


for number in range(0,10000):
	koiexists=False
	for line in open('cumulative.tab','r'):
		koinumber=int(float(line.split('\t')[1].replace('K','')))
		if number==koinumber:
			koiexists=True
			disposition='FALSE POSITIVE'
			for newline in open('cumulative.tab','r'):
				keplerplanet=str(int(float(newline.split('\t')[1].replace('K',''))))
				if keplerplanet==str(number):
					if str(newline.split('\t')[3])!='FALSE POSITIVE':
						disposition='CANDIDATE'
		
			if disposition=='CANDIDATE':
				output=open('KOI-'+str(number)+'.html','w')
				output.write('<html>'+'\n')

				output.write('<head>'+'\n')
				output.write('<title>Robo-AO KOI Survey</title>'+'\n')
				output.write('<link rel="stylesheet" href="../css/bootstrap.min.css">'+'\n')
				output.write('<link rel="stylesheet" href="../css/font-awesome.min.css">'+'\n')
				output.write('<link rel="stylesheet" href="../css/style.css">'+'\n')
				output.write('<link href="https://fonts.googleapis.com/css?family=Lora|Merriweather:300,400" rel="stylesheet">'+'\n')
 				output.write('<link rel="shortcut icon" type="image/x-icon" href="../robo_ao_logo.png" />')

				output.write('</head>'+'\n')
				output.write('<body>'+'\n')
				output.write('<div class="navbar navbar-default navbar-static-top" role="navigation">'+'\n')
				output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
				output.write('     <div class="container">'+'\n')
				output.write('          <div class="navbar-header">'+'\n')
				output.write('               <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">'+'\n')
				output.write('                    <span class="icon icon-bar"></span>'+'\n')
				output.write('                    <span class="icon icon-bar"></span>'+'\n')
				output.write('                    <span class="icon icon-bar"></span>'+'\n')
				output.write('               </button>'+'\n')

				output.write('               <a href="http://www.ifa.hawaii.edu/Robo-AO/" class="navbar-brand" target="_blank">Robo-AO</a>'+'\n')
				output.write('          </div>'+'\n')
				output.write('          <div class="collapse navbar-collapse">'+'\n')
				output.write('               <ul class="nav navbar-nav navbar-center">'+'\n')
				output.write('			<h4><form onsubmit="location.href='+str("'")+'KOI-'+str("'")+' + document.getElementById('+str("'")+'myInput'+str("'")+').value + '+str("'")+'.html'+str("'")+'; return false;">'+'\n')
				output.write(' 		<span style="display:inline-block; width: 200px;"></span>'+'\n')
				output.write('   KOI-<input type="text" id="myInput" />'+'\n')
				output.write('   <input type="submit" value="Go"/>'+'\n')
				output.write(' </form></h4>'+'\n')
				output.write('                </ul>'+'\n')
				output.write('                <ul class="nav navbar-nav navbar-right">'+'\n')
				output.write('                     <li><a href="../index.html">Home</a></li>'+'\n')
				output.write('                     <li><a href="../index.html#about">About</a></li>'+'\n')
				output.write('                     <li><a href="../contact.html">Contact</a></li>'+'\n')
				output.write('                </ul>'+'\n')
				output.write('           </div>'+'\n')
				output.write('   </div>'+'\n')
				output.write('   </div>'+'\n')
				output.write(' </body>'+'\n')
				output.write(' <span style="display:inline-block; height: 100px;"></span>'+'\n')
				output.write(' <h3><span style="display:inline-block; width: 20px;"></span>KOI-'+str(number)+'</h3>'+'\n')

				planetlist=[]
				if str(line.split('\t')[3])=='CANDIDATE':
					output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Planetary candidate</h4>'+'\n')
				if str(line.split('\t')[3])=='CONFIRMED':
					for newline in open('cumulative.tab','r'):
						keplerplanet=str(int(float(newline.split('\t')[1].replace('K',''))))
						if keplerplanet==str(number):
							if str(newline.split('\t')[3])=='CONFIRMED':
								planetlist.append(str(newline.split('\t')[2]))
					if len(planetlist)==1:
						output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Confirmed planet</h4>'+'\n')
						output.write(' <h4><span style="display:inline-block; width: 20px;"></span>'+str(line.split('\t')[2])+'</h4>'+'\n')
					if len(planetlist)>1:
						output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Confirmed planets</h4>'+'\n')
						for n in range(0,len(planetlist)):
							output.write(' <h4><span style="display:inline-block; width: 20px;"></span>'+str(planetlist[n])+'</h4>'+'\n')
				if str(line.split('\t')[3])=='FALSE POSITIVE':
					if disposition=='CANDIDATE':
						output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Planetary candidate</h4>'+'\n')

				output.write(' <h4><span style="display:inline-block; height: 20px;"></span> </h4>'+'\n')
				output.write(' <span style="display:inline-block; width: 50px;"></span>'+'\n')
				output.write(' <img style="border:1px solid #000000" src="https://users.physics.unc.edu/~caziegle/cutouts/KOI'+str(number)+'_cutout.png" alt="KOI-'+str(number)+'" height="384" width="384">'+'\n')
				output.write(' <span style="display:inline-block; width: 40px;"></span>'+'\n')
				output.write(' <img style="border:1px solid #000000" src="https://users.physics.unc.edu/~caziegle/ukirt/'+str(number)+'.png" alt="KOI-'+str(number)+'" height="384" width="384">'+'\n')
				output.write('  <span style="display:inline-block; width: 40px;"></span>'+'\n')
				output.write('	<img title="KOI-'+str(number)+'" src="https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels.png" onmouseover="this.src='+'\''+'https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels_aperture.png'+'\''+'" onmouseout="this.src='+'\''+'https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels.png'+'\''+'" height="424"/></a>'+'\n')
				if len(str(number))==1:
					output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-1<span style="display:inline-block; width: 115;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
				if len(str(number))==2:
					output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 105;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
				if len(str(number))==3:
					output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 90;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
				if len(str(number))==4:
					output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 80;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
				paperfound=False
				for line3 in open('observedkois.txt','r'):
					number3=str(line3.split('\t')[0])
					if number3==str(number):
						paper=line3.split('\t')[1].split('\n')[0]

						if paper=='1':
							if paperfound==False:
								output.write(' <h5><span style="display:inline-block; width: 55px;"></span>with any detected nearby stars circled (<a href="http://arxiv.org/abs/1312.4958" target="_blank">Law et al. 2014</a>)<span style="display:inline-block; width: 523px;"></span>detected nearby stars are labeled by their delta-magnitude.</h5>'+'\n')
								output.write(' <h5><span style="display:inline-block; width: 960px;"></span>Mouseover the image to display photometric aperture used.</h5>'+'\n')
								paperfound=True
						if paper=='2':
							if paperfound==False:
								output.write(' <h5><span style="display:inline-block; width: 50px;"></span>with any detected nearby stars circled (<a href="http://arxiv.org/abs/1604.08604" target="_blank">Baranec et al. 2016</a>)<span style="display:inline-block; width: 503px;"></span>detected nearby stars are labeled by their delta-magnitude.</h5>'+'\n')
								output.write(' <h5><span style="display:inline-block; width: 960px;"></span>Mouseover the image to display photometric aperture used.</h5>'+'\n')
								paperfound=True
						if paper=='3':
							if paperfound==False:
								output.write(' <h5><span style="display:inline-block; width: 55px;"></span>with any detected nearby stars circled (<a href="http://arxiv.org/abs/1605.03584" target="_blank">Ziegler et al. 2017</a>)<span style="display:inline-block; width: 503px;"></span>detected nearby stars are labeled by their delta-magnitude.</h5>'+'\n')
								output.write(' <h5><span style="display:inline-block; width: 960px;"></span>Mouseover the image to display photometric aperture used.</h5>'+'\n')
								paperfound=True
						if paper=='4':
							if paperfound==False:
								output.write(' <h5><span style="display:inline-block; width: 45px;"></span>with any detected nearby stars circled (<a href="https://arxiv.org/abs/1712.04454" target="_blank">Ziegler et al. 2018</a>)<span style="display:inline-block; width: 530px;"></span>detected nearby stars are labeled by their delta-magnitude.</h5>'+'\n')
								output.write(' <h5><span style="display:inline-block; width: 970px;"></span>Mouseover the image to display photometric aperture used.</h5>'+'\n')
								paperfound=True

				output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
				output.write(' <span style="display:inline-block; width: 170px;"></span>'+'\n')
				output.write(' <img style="border:0px solid #000000" src="https://users.physics.unc.edu/~caziegle/sensitivity_plots/'+str(number)+'_image_sensitivity.png" alt="KOI-'+str(number)+'" height="322" width="571">'+'\n')
				output.write(' <h5><span style="display:inline-block; width: 300px;"></span>Robo-AO 5-sigma detection sensitivity for KOI-'+str(number)+'</h5>'+'\n')
				output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
				nearbystars=0
				for line2 in open('combined_paper_nearby_star_list_sorted.txt','r'):
					koinumber2=line2.split('\t')[0]
					if str(koinumber2)==str(number):
						nearbystars+=1
						print koinumber2
						sep=line2.split('\t')[1]
						pa=line2.split('\t')[2]
						contrast=line2.split('\t')[3]
						reference=str(line2.split('\t')[4].split('\n')[0])
						if nearbystars==1:
							output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Nearby star properties</h4>'+'\n')
							output.write(' <table style="width:600px; margin-left:100px">'+'\n')
							output.write('   <tr>'+'\n')
							output.write('     <th>Separation</th>'+'\n')
							output.write('     <th>Position Angle</th> '+'\n')
							output.write('     <th> <a href="apj497133f2_hr.jpg" target="_blank">LP600</a> Contrast</th>'+'\n')
							output.write('     <th>Reference</th>'+'\n')
							output.write('   </tr>'+'\n')
							output.write('   <tr>'+'\n')
							output.write('     <th>    (")</th>'+'\n')
							output.write('     <th>(deg)</th> '+'\n')
							output.write('     <th>(mags)</th>'+'\n')
							output.write('     <th></th> '+'\n')
							output.write('   </tr>'+'\n')

						output.write('   <tr>'+'\n')
						output.write('     <td><h5>'+str(sep)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(pa)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(contrast)+'<br></h5>'+'\n')
						if reference=='1':
							output.write('     <td><h5><a href="http://arxiv.org/abs/1312.4958" target="_blank">Law et al. (2014)</a><br></h5>'+'\n')
						if reference=='2':
							output.write('     <td><h5><a href="http://arxiv.org/abs/1604.08604" target="_blank">Baranec et al. (2016)</a><br></h5>'+'\n')
						if reference=='3':
							output.write('     <td><h5><a href="http://arxiv.org/abs/1605.03584" target="_blank">Ziegler et al. (2017)</a><br></h5>'+'\n')
						if reference=='4':
							output.write('     <td><h5><a href="https://arxiv.org/abs/1712.04454" target="_blank">Ziegler et al. 2018</a><br></h5>'+'\n')
						output.write('   </tr>'+'\n')

				if nearbystars==0:
					output.write(' <h4><span style="display:inline-block; width: 20px;"></span>No nearby stars detected within 4" of KOI-'+str(number)+' in Robo-AO imaging</h4>'+'\n')
				output.write(' </table>'+'\n')
			
				output.write(' <table style="width:315px; margin-left:0px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write(' <th><h4><span style="display:inline-block; width: 20px;"></span>Planet properties</h4></th>')
				output.write('  <th><h5><span style="display:inline-block; height: 15px;"></span>(<a href="https://arxiv.org/abs/1609.04128" target="_blank">Kepler DR25</a>)</h5></th>')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <table style="width:1100px; margin-left:100px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th>Planet</th>'+'\n')
				output.write('     <th>Disposition</th>'+'\n')
				output.write('     <th>Period</th>'+'\n')
				output.write('     <th>Radius</th> '+'\n')
				output.write('     <th>Epoch</th>'+'\n')
				output.write('     <th>Transit duration</th>'+'\n')
				output.write('     <th>Transit depth</th>'+'\n')
				output.write('     <th>Eq. Temp.</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th></th>'+'\n')
				output.write('     <th></th>'+'\n')
				output.write('     <th>(days)</th>'+'\n')
				output.write('     <th>(R<sub>Earth</sub>)</th> '+'\n')
				output.write('     <th>(BJD)</th>'+'\n')
				output.write('     <th>(hrs)</th> '+'\n')
				output.write('     <th>(ppm)</th> '+'\n')
				output.write('     <th>(K)</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')

				for newline in open('cumulative.tab','r'):
					keplerplanet=str(int(float(newline.split('\t')[1].replace('K',''))))
					if keplerplanet==str(number):
						try:
							radius=float(newline.split('\t')[17])
							radius=float(newline.split('\t')[11])
							planetnumber=str('{:.2f}'.format(float(newline.split('\t')[1].replace('K',''))))
							if str(newline.split('\t')[3])=='FALSE POSITIVE':
								output.write('     <td><h5>'+planetnumber+'<br></h5></td>'+'\n')
								output.write('     <td><h5>False positive<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CANDIDATE':
								output.write('     <td><h5><a href="https://users.physics.unc.edu/~caziegle/lcs/'+planetnumber+'_lc.png" target="_blank">'+planetnumber+'<br></h5></td>'+'\n')
								output.write('     <td><h5>Candidate<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CONFIRMED':
								output.write('     <td><h5><a href="https://users.physics.unc.edu/~caziegle/lcs/'+planetnumber+'_lc.png" target="_blank">'+planetnumber+'<br></h5></td>'+'\n')
								output.write('     <td><h5>Confirmed<br></h5><h6>'+str(newline.split('\t')[2])+'</h6></td>'+'\n')
							#soutput.write('     <td><h5>'+str(newline.split('\t')[5])+'<br></h5><h6>&plusmn'+str('{:.10f}'.format(float(newline.split('\t')[6])))+'</h6></td>'+'\n')
							if newline.split('\t')[6]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'<br></h5><h6>&plusmn'+str('{:.10f}'.format(float(newline.split('\t')[6])))+'</h6></td>'+'\n')
							if newline.split('\t')[6]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'</h5></td>'+'\n')
							if newline.split('\t')[18]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'<br></h5><h6>&plusmn'+str('{:.2f}'.format(float(newline.split('\t')[18])))+'</h6></td>'+'\n')
							if newline.split('\t')[18]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'</h5></td>'+'\n')
							if newline.split('\t')[9]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'<br></h5><h6>&plusmn'+str('{:.8f}'.format(float(newline.split('\t')[9])))+'</h6></td>'+'\n')
							if newline.split('\t')[9]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'</h5></td>'+'\n')

							if newline.split('\t')[12]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[12])+'</h6></td>'+'\n')
							if newline.split('\t')[12]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'</h5></td>'+'\n')
							if newline.split('\t')[15]!='':
								output.write('     <td><h5>'+str(int(float(newline.split('\t')[14])))+'<br></h5><h6>&plusmn'+str(int(float(newline.split('\t')[15])))+'</h6></td>'+'\n')
							if newline.split('\t')[15]=='':
								output.write('     <td><h5>'+str(int(float(newline.split('\t')[14])))+'</h5></td>'+'\n')

							output.write('     <td><h5>'+str(int(float(newline.split('\t')[20])))+'<br></h5></td>'+'\n')
							output.write('   </tr>'+'\n')
						except:
							planetnumber=str('{:.2f}'.format(float(newline.split('\t')[1].replace('K',''))))
							if str(newline.split('\t')[3])=='FALSE POSITIVE':
								output.write('     <td><h5>'+planetnumber+'<br></h5></td>'+'\n')
								output.write('     <td><h5>False positive<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CANDIDATE':
								output.write('     <td><h5><a href="lcs/'+planetnumber+'_lc.png" target="_blank">'+planetnumber+'<br></h5></td>'+'\n')
								output.write('     <td><h5>Candidate<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CONFIRMED':
								output.write('     <td><h5><a href="lcs/'+planetnumber+'_lc.png" target="_blank">'+planetnumber+'<br></h5></td>'+'\n')
								output.write('     <td><h5>Confirmed<br></h5><h6>'+str(newline.split('\t')[2])+'</h6></td>'+'\n')
							if newline.split('\t')[6]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'<br></h5><h6>&plusmn'+str('{:.10f}'.format(float(newline.split('\t')[6])))+'</h6></td>'+'\n')
							if newline.split('\t')[6]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'</h5></td>'+'\n')
							if newline.split('\t')[18]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'<br></h5><h6>&plusmn'+str('{:.2f}'.format(float(newline.split('\t')[18])))+'</h6></td>'+'\n')
							if newline.split('\t')[18]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'</h5></td>'+'\n')
							if newline.split('\t')[9]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[9])+'</h6></td>'+'\n')
							if newline.split('\t')[9]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'</h5></td>'+'\n')

							if newline.split('\t')[12]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[12])+'</h6></td>'+'\n')
							if newline.split('\t')[12]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'</h5></td>'+'\n')
							if newline.split('\t')[15]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[14])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[15])+'</h6></td>'+'\n')
							if newline.split('\t')[15]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[14])+'</h5></td>'+'\n')
							output.write('     <td><h5>'+str(newline.split('\t')[20])+'<br></h5></td>'+'\n')
							output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <table style="width:490px; margin-left:0px">'+'\n')
				output.write('   <tr>'+'\n')
				nearbystars=0
				for line3 in open('updated_radii.txt','r'):
					koinumber3=int(float(line3.split(' & ')[0]))
					if str(number)==str(koinumber3):
						nearbystars+=1
				if nearbystars==1:
					output.write(' <th><h4><span style="display:inline-block; width: 20px;"></span>Corrected planetary radius </h4></th>')
					output.write('  <th><h5><span style="display:inline-block; height: 15px;"></span>(<a href="https://arxiv.org/abs/1712.04454" target="_blank">Ziegler et al. 2018</a>)</h5></th>')
					output.write('   </tr>'+'\n')
				if nearbystars>1:
					output.write(' <th><h4><span style="display:inline-block; width: 20px;"></span>Corrected planetary radii </h4></th>')
					output.write('  <th><h5><span style="display:inline-block; height: 15px;"></span>(<a href="https://arxiv.org/abs/1712.04454" target="_blank">Ziegler et al. 2018</a>)</h5></th>')
					output.write('   </tr>'+'\n')
				nearbystars=0
				for line3 in open('updated_radii.txt','r'):
					koinumber3=int(float(line3.split(' & ')[0]))
					if str(number)==str(koinumber3):
						nearbystars+=1
						planet=float(line3.split(' & ')[0])
						originalradius=line3.split(' & ')[6]
						radiusprimary=line3.split(' & ')[7]
						radiussecondary=line3.split(' & ')[8].split('\\')[0]
						if nearbystars==1:
							output.write(' <table style="width:850px; margin-left:100px">'+'\n')
							output.write('   <tr>'+'\n')
							output.write('     <th>Planet</th>'+'\n')
							output.write('     <th>Original derived</th> '+'\n')
							output.write('     <th>Corrected radius if</th>'+'\n')
							output.write('     <th>Corrected radius if</th>'+'\n')
							output.write('   </tr>'+'\n')
							output.write('   <tr>'+'\n')
							output.write('     <th>candidate</th>'+'\n')
							output.write('     <th>planetary radius</th> '+'\n')
							output.write('     <th>orbiting primary</th>'+'\n')
							output.write('     <th>orbiting bound secondary</th>'+'\n')
							output.write('   </tr>'+'\n')
							output.write('   <tr>'+'\n')
							output.write('     <th></th>'+'\n')
							output.write('     <th>(R<sub>Earth</sub>)</th> '+'\n')
							output.write('     <th>(R<sub>Earth</sub>)</th> '+'\n')
							output.write('     <th>(R<sub>Earth</sub>)</th> '+'\n')
							output.write('     <th></th> '+'\n')
							output.write('   </tr>'+'\n')

						output.write('   <tr>'+'\n')
						output.write('     <td><h5>'+str(planet)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(originalradius)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(radiusprimary)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(radiussecondary)+'<br></h5>'+'\n')
						output.write('   </tr>'+'\n')

				output.write(' <table style="width:325px; margin-left:0px">'+'\n')
				output.write(' <th><h4><span style="display:inline-block; width: 20px;"></span>Stellar parameters</h4></th>')
				output.write('  <th><h5><span style="display:inline-block; height: 15px;"></span>(<a href="https://arxiv.org/abs/1609.04128" target="_blank">Kepler DR25</a>)</h5></th>')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <table style="width:800px; margin-left:100px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th>RA</th>'+'\n')
				output.write('     <th>Dec</th>'+'\n')
				output.write('     <th>Kepler-band</th>'+'\n')
				output.write('     <th>Effective T</th>'+'\n')
				output.write('     <th>Surface gravity</th>'+'\n')
				output.write('     <th>Metallicity</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th>(degrees)</th>'+'\n')
				output.write('     <th>(degrees)</th> '+'\n')
				output.write('     <th>(mag)</th>'+'\n')
				output.write('     <th>(K)</th> '+'\n')
				output.write('     <th>(log<sub>10</sub>(cm/s<sup>2</sup>))</th>'+'\n')
				output.write('     <th>(dex)</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				found=False
				for line2 in open('cumulative.tab','r'):
					keplerplanet=str(int(float(line2.split('\t')[1].replace('K',''))))
					if keplerplanet==str(number):
						if found==False:
							found=True
							try:
								output.write('     <td><h5>'+str(line2.split('\t')[32])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[33])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[34])+'</h5></td>'+'\n')
								#print number, line2.split('\t')[24]
								if line2.split('\t')[24]!='':
									output.write('     <td><h5>'+str(int(float(line2.split('\t')[23])))+'<br></h5><h6>&plusmn'+str(int(float(line2.split('\t')[24])))+'</h6></td>'+'\n')
								if line2.split('\t')[24]=='':
									output.write('     <td><h5>'+str(int(float(line2.split('\t')[23])))+'</h5></td>'+'\n')
								if line2.split('\t')[27]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[27])+'</h6></td>'+'\n')
								if line2.split('\t')[27]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'</h5></td>'+'\n')
								if line2.split('\t')[30]!='':
									output.write('     <td><h5>'+str('{:.2f}'.format(float(line2.split('\t')[29])))+'<br></h5><h6>&plusmn'+str('{:.2f}'.format(float(line2.split('\t')[30])))+'</h6></td>'+'\n')
								if line2.split('\t')[30]=='':
									output.write('     <td><h5>'+str('{:.2f}'.format(float(line2.split('\t')[29])))+'</h5></td>'+'\n')
							except:
								output.write('     <td><h5>'+str(line2.split('\t')[32])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[33])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[34])+'</h5></td>'+'\n')
								if line2.split('\t')[24]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[23])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[24])+'</h6></td>'+'\n')
								if line2.split('\t')[24]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[23])+'</h5></td>'+'\n')
								if line2.split('\t')[27]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[27])+'</h6></td>'+'\n')
								if line2.split('\t')[27]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'</h5></td>'+'\n')
								if line2.split('\t')[30]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[29])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[30])+'</h6></td>'+'\n')
								if line2.split('\t')[30]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[29])+'</h5></td>'+'\n')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')

				output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Outside links for KOI-'+str(number)+'</h4>'+'\n')
				output.write(' <table style="width:40%; margin-left:50px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <h5><span style="display:inline-block; width: 100px;"></span><a href="http://simbad.u-strasbg.fr/simbad/sim-id?Ident=KOI-'+str(number)+'" target="_blank">SIMBAD Astronomical Database (if available)</a><br></h5>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <h5><span style="display:inline-block; width: 100px;"></span><a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/DisplayOverview/nph-DisplayOverview?objname=KOI-'+str(number)+'" target="_blank">NASA Exoplanet archive</a><br></h5>'+'\n')
				output.write('     <h5><span style="display:inline-block; width: 100px;"></span><a href="https://exofop.ipac.caltech.edu/kepler/edit_target.php?id='+str(number)+'" target="_blank"><i>Kepler</i> Exoplanet Follow-up Observing Program (access required)</a><br></h5>'+'\n')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <center><h5><span style="display:inline-block; height: 50px;"></span><span style="display:inline-block; width: 40px;"></span>&copy; Carl Ziegler and the Robo-AO collaboration</h5></center>'+'\n')
				output.write(' </html>'+'\n')

			if disposition=='FALSE POSITIVE':
				output=open('KOI-'+str(number)+'.html','w')
				output.write('<html>'+'\n')
				output.write('<head>'+'\n')
				output.write('<title>Robo-AO KOI Survey</title>'+'\n')
				output.write('<link rel="stylesheet" href="../css/bootstrap.min.css">'+'\n')
				output.write('<link rel="stylesheet" href="../css/font-awesome.min.css">'+'\n')
				output.write('<link rel="stylesheet" href="../css/style.css">'+'\n')
				output.write('<link href="https://fonts.googleapis.com/css?family=Lora|Merriweather:300,400" rel="stylesheet">'+'\n')
 				output.write('<link rel="shortcut icon" type="image/x-icon" href="../robo_ao_logo.png" />')
				output.write('</head>'+'\n')
				output.write('<body>'+'\n')
				output.write('<div class="navbar navbar-default navbar-static-top" role="navigation">'+'\n')
				output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
				output.write('     <div class="container">'+'\n')
				output.write('          <div class="navbar-header">'+'\n')
				output.write('               <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">'+'\n')
				output.write('                    <span class="icon icon-bar"></span>'+'\n')
				output.write('                    <span class="icon icon-bar"></span>'+'\n')
				output.write('                    <span class="icon icon-bar"></span>'+'\n')
				output.write('               </button>'+'\n')

				output.write('               <a href="http://www.ifa.hawaii.edu/Robo-AO/" class="navbar-brand" target="_blank">Robo-AO</a>'+'\n')
				output.write('          </div>'+'\n')
				output.write('          <div class="collapse navbar-collapse">'+'\n')
				output.write('               <ul class="nav navbar-nav navbar-center">'+'\n')
				output.write('			<h4><form onsubmit="location.href='+str("'")+'KOI-'+str("'")+' + document.getElementById('+str("'")+'myInput'+str("'")+').value + '+str("'")+'.html'+str("'")+'; return false;">'+'\n')
				output.write(' 		<span style="display:inline-block; width: 200px;"></span>'+'\n')
				output.write('   KOI-<input type="text" id="myInput" />'+'\n')
				output.write('   <input type="submit" value="Go"/>'+'\n')
				output.write(' </form></h4>'+'\n')
				output.write('                </ul>'+'\n')
				output.write('                <ul class="nav navbar-nav navbar-right">'+'\n')
				output.write('                     <li><a href="../index.html">Home</a></li>'+'\n')
				output.write('                     <li><a href="../index.html#about">About</a></li>'+'\n')
				output.write('                     <li><a href="../contact.html">Contact</a></li>'+'\n')
				output.write('                </ul>'+'\n')
				output.write('           </div>'+'\n')
				output.write('   </div>'+'\n')
				output.write('   </div>'+'\n')
				output.write(' </body>'+'\n')


				roboaoobserved=False
				for line3 in open('observedkois.txt','r'):
					number3=str(line3.split('\t')[0])
					if number3==str(number):
						roboaoobserved=True
						output.write(' <span style="display:inline-block; height: 100px;"></span>'+'\n')
						output.write(' <h3><span style="display:inline-block; width: 20px;"></span>KOI-'+str(number)+'</h3>'+'\n')

						output.write(' <h4><span style="display:inline-block; width: 20px;"></span>False positive</h4>'+'\n')
						output.write(' <h4><span style="display:inline-block; height: 20px;"></span> </h4>'+'\n')
						output.write(' <span style="display:inline-block; width: 50px;"></span>'+'\n')
						output.write(' <img style="border:1px solid #000000" src="https://users.physics.unc.edu/~caziegle/cutouts/KOI'+str(number)+'_cutout.png" alt="KOI-'+str(number)+'" height="384" width="384">'+'\n')
						output.write(' <span style="display:inline-block; width: 40px;"></span>'+'\n')
						output.write(' <img style="border:1px solid #000000" src="https://users.physics.unc.edu/~caziegle/ukirt/'+str(number)+'.png" alt="KOI-'+str(number)+'" height="384" width="384">'+'\n')
						output.write('  <span style="display:inline-block; width: 40px;"></span>'+'\n')
						output.write('	<img title="KOI-'+str(number)+'" src="https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels.png" onmouseover="this.src='+'\''+'https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels_aperture.png'+'\''+'" onmouseout="this.src='+'\''+'https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels.png'+'\''+'" height="424"/></a>'+'\n')
						if len(str(number))==1:
							output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 115;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
						if len(str(number))==2:
							output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 105;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
						if len(str(number))==3:
							output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 90;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
						if len(str(number))==4:
							output.write(' <h5><span style="display:inline-block; width: 67px;"></span>Robo-AO 8-arcsec centered cutout image of KOI-'+str(number)+'<span style="display:inline-block; width: 80;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 160;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
						output.write(' <h5><span style="display:inline-block; width: 105px;"></span>with any detected nearby stars circled<span style="display:inline-block; width: 600px;"></span>detected nearby stars are labeled by their delta-magnitude.</h5>'+'\n')
						output.write(' <h5><span style="display:inline-block; width: 970px;"></span>Mouseover the image to display photometric aperture used.</h5>'+'\n')
						output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
						output.write(' <span style="display:inline-block; width: 170px;"></span>'+'\n')
						output.write(' <img style="border:0px solid #000000" src="https://users.physics.unc.edu/~caziegle/sensitivity_plots/'+str(number)+'_image_sensitivity.png" alt="KOI-'+str(number)+'" height="322" width="571">'+'\n')
						output.write(' <h5><span style="display:inline-block; width: 300px;"></span>Robo-AO 5-sigma detection sensitivity for KOI-'+str(number)+'</h5>'+'\n')
				if roboaoobserved==False:
					output.write(' <span style="display:inline-block; height: 100px;"></span>'+'\n')
					output.write(' <h3><span style="display:inline-block; width: 20px;"></span>KOI-'+str(number)+'</h3>'+'\n')

					output.write(' <h4><span style="display:inline-block; width: 20px;"></span>False positive</h4>'+'\n')
					output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Not observed with Robo-AO</h4>'+'\n')
					output.write(' <span style="display:inline-block; width: 30px;"></span><img style="border:1px solid #000000" src="https://users.physics.unc.edu/~caziegle/ukirt/'+str(number)+'.png" alt="KOI-'+str(number)+'" height="384" width="384">'+'\n')
					output.write('  <span style="display:inline-block; width: 40px;"></span>'+'\n')
					output.write('	<img title="KOI-'+str(number)+'" src="https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels.png" onmouseover="this.src='+'\''+'https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels_aperture.png'+'\''+'" onmouseout="this.src='+'\''+'https://users.physics.unc.edu/~caziegle/pixels/'+str(number)+'_quarter4_pixels.png'+'\''+'" height="424"/></a>'+'\n')
					output.write(' <h5><span style="display:inline-block; width: 70px;"></span>UKIRT 1-arcmin field centered on KOI-'+str(number)+'<span style="display:inline-block; width: 180;"></span><i>Kepler</i> image of KOI-'+str(number)+' from Quarter 4 of observing. Any </h5>'+'\n')
					output.write(' <h5><span style="display:inline-block; width: 525px;"></span>detected nearby stars are labeled by their delta-magnitude.</h5>'+'\n')
					output.write(' <h5><span style="display:inline-block; width: 520px;"></span>Mouseover the image to display photometric aperture used.</h5>'+'\n')
				output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
				nearbystars=0
				for line2 in open('combined_paper_nearby_star_list_sorted.txt','r'):
					koinumber2=line2.split('\t')[0]
					if str(koinumber2)==str(number):
						nearbystars+=1
						print koinumber2
						sep=line2.split('\t')[1]
						pa=line2.split('\t')[2]
						contrast=line2.split('\t')[3]
						reference=str(line2.split('\t')[4].split('\n')[0])
						if nearbystars==1:
							output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Nearby star properties</h4>'+'\n')
							output.write(' <table style="width:600px; margin-left:100px">'+'\n')
							output.write('   <tr>'+'\n')
							output.write('     <th>Separation</th>'+'\n')
							output.write('     <th>Position Angle</th> '+'\n')
							output.write('     <th> <a href="apj497133f2_hr.jpg" target="_blank">LP600</a> Contrast</th>'+'\n')
							output.write('     <th>Reference</th>'+'\n')
							output.write('   </tr>'+'\n')
							output.write('     <th>    (")</th>'+'\n')
							output.write('     <th>(deg)</th> '+'\n')
							output.write('     <th>(mags)</th>'+'\n')
							output.write('     <th></th> '+'\n')
							output.write('   </tr>'+'\n')
						output.write('   <tr>'+'\n')
						output.write('     <td><h5>'+str(sep)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(pa)+'<br></h5>'+'\n')
						output.write('     <td><h5>'+str(contrast)+'<br></h5>'+'\n')
						if reference=='1':
							output.write('     <td><h5><a href="http://arxiv.org/abs/1312.4958" target="_blank">Law et al. (2014)</a><br></h5>'+'\n')
						if reference=='2':
							output.write('     <td><h5><a href="http://arxiv.org/abs/1604.08604" target="_blank">Baranec et al. (2016)</a><br></h5>'+'\n')
						if reference=='3':
							output.write('     <td><h5><a href="http://arxiv.org/abs/1605.03584" target="_blank">Ziegler et al. (2017)</a><br></h5>'+'\n')
						if reference=='4':
							output.write('     <td><h5><a href="https://arxiv.org/abs/1712.04454" target="_blank">Ziegler et al. (2018)</a><br></h5>'+'\n')
						output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')


				output.write(' <table style="width:315px; margin-left:0px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write(' <th><h4><span style="display:inline-block; width: 20px;"></span>Planet properties</h4></th>')
				output.write('  <th><h5><span style="display:inline-block; height: 15px;"></span>(<a href="https://arxiv.org/abs/1609.04128" target="_blank">Kepler DR25</a>)</h5></th>')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <table style="width:1100px; margin-left:100px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th>Planet</th>'+'\n')
				output.write('     <th>Disposition</th>'+'\n')
				output.write('     <th>Period</th>'+'\n')
				output.write('     <th>Radius</th> '+'\n')
				output.write('     <th>Epoch</th>'+'\n')
				output.write('     <th>Transit duration</th>'+'\n')
				output.write('     <th>Transit depth</th>'+'\n')
				output.write('     <th>Eq. Temp.</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th></th>'+'\n')
				output.write('     <th></th>'+'\n')
				output.write('     <th>(days)</th>'+'\n')
				output.write('     <th>(R<sub>Earth</sub>)</th> '+'\n')
				output.write('     <th>(BJD)</th>'+'\n')
				output.write('     <th>(hrs)</th> '+'\n')
				output.write('     <th>(ppm)</th> '+'\n')
				output.write('     <th>(K)</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')

				for newline in open('cumulative.tab','r'):
					keplerplanet=str(int(float(newline.split('\t')[1].replace('K',''))))
					if keplerplanet==str(number):
						try:
							radius=float(newline.split('\t')[17])
							radius=float(newline.split('\t')[11])
							planetnumber=str('{:.2f}'.format(float(newline.split('\t')[1].replace('K',''))))
							output.write('     <td><h5>'+planetnumber+'<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='FALSE POSITIVE':
								output.write('     <td><h5>False positive<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CANDIDATE':
								output.write('     <td><h5>Candidate<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CONFIRMED':
								output.write('     <td><h5>Confirmed<br></h5><h6>'+str(newline.split('\t')[2])+'</h6></td>'+'\n')
							#soutput.write('     <td><h5>'+str(newline.split('\t')[5])+'<br></h5><h6>&plusmn'+str('{:.10f}'.format(float(newline.split('\t')[6])))+'</h6></td>'+'\n')
							if newline.split('\t')[6]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'<br></h5><h6>&plusmn'+str('{:.10f}'.format(float(newline.split('\t')[6])))+'</h6></td>'+'\n')
							if newline.split('\t')[6]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'</h5></td>'+'\n')
							if newline.split('\t')[18]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'<br></h5><h6>&plusmn'+str('{:.2f}'.format(float(newline.split('\t')[18])))+'</h6></td>'+'\n')
							if newline.split('\t')[18]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'</h5></td>'+'\n')
							if newline.split('\t')[9]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'<br></h5><h6>&plusmn'+str('{:.8f}'.format(float(newline.split('\t')[9])))+'</h6></td>'+'\n')
							if newline.split('\t')[9]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'</h5></td>'+'\n')

							if newline.split('\t')[12]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[12])+'</h6></td>'+'\n')
							if newline.split('\t')[12]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'</h5></td>'+'\n')
							if newline.split('\t')[15]!='':
								output.write('     <td><h5>'+str(int(float(newline.split('\t')[14])))+'<br></h5><h6>&plusmn'+str(int(float(newline.split('\t')[15])))+'</h6></td>'+'\n')
							if newline.split('\t')[15]=='':
								output.write('     <td><h5>'+str(int(float(newline.split('\t')[14])))+'</h5></td>'+'\n')

							output.write('     <td><h5>'+str(int(float(newline.split('\t')[20])))+'<br></h5></td>'+'\n')
							output.write('   </tr>'+'\n')
						except:
							planetnumber=str('{:.2f}'.format(float(newline.split('\t')[1].replace('K',''))))
							output.write('     <td><h5><a href="lcs/'+planetnumber+'_lc.png" target="_blank">'+planetnumber+'<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='FALSE POSITIVE':
								output.write('     <td><h5>False positive<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CANDIDATE':
								output.write('     <td><h5>Candidate<br></h5></td>'+'\n')
							if str(newline.split('\t')[3])=='CONFIRMED':
								output.write('     <td><h5>Confirmed<br></h5><h6>'+str(newline.split('\t')[2])+'</h6></td>'+'\n')
							if newline.split('\t')[6]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'<br></h5><h6>&plusmn'+str('{:.10f}'.format(float(newline.split('\t')[6])))+'</h6></td>'+'\n')
							if newline.split('\t')[6]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[5])+'</h5></td>'+'\n')
							if newline.split('\t')[18]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'<br></h5><h6>&plusmn'+str('{:.2f}'.format(float(newline.split('\t')[18])))+'</h6></td>'+'\n')
							if newline.split('\t')[18]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[17])+'</h5></td>'+'\n')
							if newline.split('\t')[9]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[9])+'</h6></td>'+'\n')
							if newline.split('\t')[9]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[8])+'</h5></td>'+'\n')

							if newline.split('\t')[12]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[12])+'</h6></td>'+'\n')
							if newline.split('\t')[12]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[11])+'</h5></td>'+'\n')
							if newline.split('\t')[15]!='':
								output.write('     <td><h5>'+str(newline.split('\t')[14])+'<br></h5><h6>&plusmn'+str(newline.split('\t')[15])+'</h6></td>'+'\n')
							if newline.split('\t')[15]=='':
								output.write('     <td><h5>'+str(newline.split('\t')[14])+'</h5></td>'+'\n')
							output.write('     <td><h5>'+str(newline.split('\t')[20])+'<br></h5></td>'+'\n')
							output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')


				output.write(' <table style="width:325px; margin-left:0px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write(' <th><h4><span style="display:inline-block; width: 20px;"></span>Stellar parameters</h4></th>')
				output.write('  <th><h5><span style="display:inline-block; height: 15px;"></span>(<a href="https://arxiv.org/abs/1609.04128" target="_blank">Kepler DR25</a>)</h5></th>')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <table style="width:800px; margin-left:100px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th>RA</th>'+'\n')
				output.write('     <th>Dec</th>'+'\n')
				output.write('     <th>Kepler-band</th>'+'\n')
				output.write('     <th>Effective T</th>'+'\n')
				output.write('     <th>Surface gravity</th>'+'\n')
				output.write('     <th>Metallicity</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <th>(degrees)</th>'+'\n')
				output.write('     <th>(degrees)</th> '+'\n')
				output.write('     <th>(mag)</th>'+'\n')
				output.write('     <th>(K)</th> '+'\n')
				output.write('     <th>(log<sub>10</sub>(cm/s<sup>2</sup>))</th>'+'\n')
				output.write('     <th>(dex)</th>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				found=False
				for line2 in open('cumulative.tab','r'):
					keplerplanet=str(int(float(line2.split('\t')[1].replace('K',''))))
					if keplerplanet==str(number):
						if found==False:
							found=True
							try:
								output.write('     <td><h5>'+str(line2.split('\t')[32])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[33])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[34])+'</h5></td>'+'\n')
								#print number, line2.split('\t')[24]
								if line2.split('\t')[24]!='':
									output.write('     <td><h5>'+str(int(float(line2.split('\t')[23])))+'<br></h5><h6>&plusmn'+str(int(float(line2.split('\t')[24])))+'</h6></td>'+'\n')
								if line2.split('\t')[24]=='':
									output.write('     <td><h5>'+str(int(float(line2.split('\t')[23])))+'</h5></td>'+'\n')
								if line2.split('\t')[27]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[27])+'</h6></td>'+'\n')
								if line2.split('\t')[27]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'</h5></td>'+'\n')
								if line2.split('\t')[30]!='':
									output.write('     <td><h5>'+str('{:.2f}'.format(float(line2.split('\t')[29])))+'<br></h5><h6>&plusmn'+str('{:.2f}'.format(float(line2.split('\t')[30])))+'</h6></td>'+'\n')
								if line2.split('\t')[30]=='':
									output.write('     <td><h5>'+str('{:.2f}'.format(float(line2.split('\t')[29])))+'</h5></td>'+'\n')
							except:
								output.write('     <td><h5>'+str(line2.split('\t')[32])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[33])+'</h5></td>'+'\n')
								output.write('     <td><h5>'+str(line2.split('\t')[34])+'</h5></td>'+'\n')
								if line2.split('\t')[24]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[23])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[24])+'</h6></td>'+'\n')
								if line2.split('\t')[24]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[23])+'</h5></td>'+'\n')
								if line2.split('\t')[27]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[27])+'</h6></td>'+'\n')
								if line2.split('\t')[27]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[26])+'</h5></td>'+'\n')
								if line2.split('\t')[30]!='':
									output.write('     <td><h5>'+str(line2.split('\t')[29])+'<br></h5><h6>&plusmn'+str(line2.split('\t')[30])+'</h6></td>'+'\n')
								if line2.split('\t')[30]=='':
									output.write('     <td><h5>'+str(line2.split('\t')[29])+'</h5></td>'+'\n')
				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')

				output.write(' <h4><span style="display:inline-block; width: 20px;"></span>Outside links for KOI-'+str(number)+'</h4>'+'\n')
				output.write(' <table style="width:40%; margin-left:50px">'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <h5><span style="display:inline-block; width: 100px;"></span><a href="http://simbad.u-strasbg.fr/simbad/sim-id?Ident=KOI-'+str(number)+'" target="_blank">SIMBAD Astronomical Database (if available)</a><br></h5>'+'\n')
				output.write('   </tr>'+'\n')
				output.write('   <tr>'+'\n')
				output.write('     <h5><span style="display:inline-block; width: 100px;"></span><a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/DisplayOverview/nph-DisplayOverview?objname=KOI-'+str(number)+'" target="_blank">NASA Exoplanet archive</a><br></h5>'+'\n')
				output.write('     <h5><span style="display:inline-block; width: 100px;"></span><a href="https://exofop.ipac.caltech.edu/kepler/edit_target.php?id='+str(number)+'" target="_blank"><i>Kepler</i> Exoplanet Follow-up Observing Program (access required)</a><br></h5>'+'\n')

				output.write('   </tr>'+'\n')
				output.write(' </table>'+'\n')
				output.write(' <center><h5><span style="display:inline-block; height: 50px;"></span><span style="display:inline-block; width: 40px;"></span>&copy; Carl Ziegler and the Robo-AO collaboration</h5></center>'+'\n')
				output.write(' </html>'+'\n')

	if koiexists==False:
		#print number, 'does not exist'
		output=open('KOI-'+str(number)+'.html','w')
		output.write('<html>'+'\n')
		output.write('<head>'+'\n')
		output.write('<title>Robo-AO KOI Survey</title>'+'\n')
		output.write('<link rel="stylesheet" href="../css/bootstrap.min.css">'+'\n')
		output.write('<link rel="stylesheet" href="../css/font-awesome.min.css">'+'\n')
		output.write('<link rel="stylesheet" href="../css/style.css">'+'\n')
		output.write('<link href="https://fonts.googleapis.com/css?family=Lora|Merriweather:300,400" rel="stylesheet">'+'\n')
 		output.write('<link rel="shortcut icon" type="image/x-icon" href="../robo_ao_logo.png" />')
		output.write('</head>'+'\n')
		output.write('<body>'+'\n')
		output.write('<div class="navbar navbar-default navbar-static-top" role="navigation">'+'\n')
		output.write(' <span style="display:inline-block; height: 20px;"></span>'+'\n')
		output.write('     <div class="container">'+'\n')
		output.write('          <div class="navbar-header">'+'\n')
		output.write('               <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">'+'\n')
		output.write('                    <span class="icon icon-bar"></span>'+'\n')
		output.write('                    <span class="icon icon-bar"></span>'+'\n')
		output.write('                    <span class="icon icon-bar"></span>'+'\n')
		output.write('               </button>'+'\n')

		output.write('               <a href="http://www.ifa.hawaii.edu/Robo-AO/" class="navbar-brand" target="_blank">Robo-AO</a>'+'\n')
		output.write('          </div>'+'\n')
		output.write('          <div class="collapse navbar-collapse">'+'\n')
		output.write('               <ul class="nav navbar-nav navbar-center">'+'\n')
		output.write('			<h4><form onsubmit="location.href='+str("'")+'KOI-'+str("'")+' + document.getElementById('+str("'")+'myInput'+str("'")+').value + '+str("'")+'.html'+str("'")+'; return false;">'+'\n')
		output.write(' 		<span style="display:inline-block; width: 200px;"></span>'+'\n')
		output.write('   KOI-<input type="text" id="myInput" />'+'\n')
		output.write('   <input type="submit" value="Go"/>'+'\n')
		output.write(' </form></h4>'+'\n')
		output.write('                </ul>'+'\n')
		output.write('                <ul class="nav navbar-nav navbar-right">'+'\n')
		output.write('                     <li><a href="../index.html">Home</a></li>'+'\n')
		output.write('                     <li><a href="../index.html#about">About</a></li>'+'\n')
		output.write('                     <li><a href="../contact.html">Contact</a></li>'+'\n')
		output.write('                </ul>'+'\n')
		output.write('           </div>'+'\n')
		output.write('   </div>'+'\n')
		output.write('   </div>'+'\n')
		output.write(' </body>'+'\n')
		output.write(' <span style="display:inline-block; height: 100px;"></span>'+'\n')
		output.write(' <h3><span style="display:inline-block; width: 20px;"></span>KOI-'+str(number)+' does not exist :(</h3>'+'\n')



#number
# COLUMN kepoi_name:     KOI Name
# COLUMN kepler_name:    Kepler Name
# COLUMN koi_disposition: Exoplanet Archive Disposition
# COLUMN koi_pdisposition: Disposition Using Kepler Data
# COLUMN koi_period:     Orbital Period [days]
# COLUMN koi_period_err1: Orbital Period Upper Unc. [days]
# COLUMN koi_period_err2: Orbital Period Lower Unc. [days]
# COLUMN koi_time0:      Transit Epoch [BJD]
# COLUMN koi_time0_err1: Transit Epoch Upper Unc. [BJD]
# COLUMN koi_time0_err2: Transit Epoch Lower Unc. [BJD]
# COLUMN koi_duration:   Transit Duration [hrs]
# COLUMN koi_duration_err1: Transit Duration Upper Unc. [hrs]
# COLUMN koi_duration_err2: Transit Duration Lower Unc. [hrs]
# COLUMN koi_depth:      Transit Depth [ppm]
# COLUMN koi_depth_err1: Transit Depth Upper Unc. [ppm]
# COLUMN koi_depth_err2: Transit Depth Lower Unc. [ppm]
# COLUMN koi_prad:       Planetary Radius [Earth radii]
# COLUMN koi_prad_err1:  Planetary Radius Upper Unc. [Earth radii]
# COLUMN koi_prad_err2:  Planetary Radius Lower Unc. [Earth radii]
# COLUMN koi_teq:        Equilibrium Temperature [K]
# COLUMN koi_teq_err1:   Equilibrium Temperature Upper Unc. [K]
# COLUMN koi_teq_err2:   Equilibrium Temperature Lower Unc. [K]
# COLUMN koi_steff:      Stellar Effective Temperature [K]
# COLUMN koi_steff_err1: Stellar Effective Temperature Upper Unc. [K]
# COLUMN koi_steff_err2: Stellar Effective Temperature Lower Unc. [K]
# COLUMN koi_slogg:      Stellar Surface Gravity [log10(cm/s**2)]
# COLUMN koi_slogg_err1: Stellar Surface Gravity Upper Unc. [log10(cm/s**2)]
# COLUMN koi_slogg_err2: Stellar Surface Gravity Lower Unc. [log10(cm/s**2)]
# COLUMN koi_smet:       Stellar Metallicity [dex]
# COLUMN koi_smet_err1:  Stellar Metallicity Upper Unc. [dex]
# COLUMN koi_smet_err2:  Stellar Metallicity Lower Unc. [dex]
# COLUMN ra:             RA [decimal degrees]
# COLUMN dec:            Dec [decimal degrees]
# COLUMN koi_kepmag:     Kepler-band [mag]
#

