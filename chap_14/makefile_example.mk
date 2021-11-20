# Building the Shell Model Paper
all : figure.*svg *.dat *.tex *.pdf

photon_photon.dat : photon_analysis.sh ./raw_data/*.h5
		./photon_analysis.sh -n=2 > photon_photon.dat

fig4.svg : photon_photon.dat plot_dat.py
		python plot_dat.py --input=photon_photon.dat --output=fig4.svg
