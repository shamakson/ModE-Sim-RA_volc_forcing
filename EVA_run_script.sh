

ln -s /usr/include/netcdf.mod

gfortran -c mo_EVA.f90

######BUILD
#---- Create the initial sulfate time series.
/usr/bin/gfortran -ffree-line-length-none -o eva_build_sulfate_file eva_build_sulfate_file.f90 mo_EVA.o -lnetcdf -lnetcdff

#---- Create AOD(time,lat) from the sulfate time series
/usr/bin/gfortran -ffree-line-length-none -o eva_build_aod_file eva_build_aod_file.f90 mo_EVA.o -lnetcdf -lnetcdff

#---- Create the forcing file over all heights from the sulfate time series.  
/usr/bin/gfortran -ffree-line-length-none -o eva_build_forcing_files eva_build_forcing_files.f90 mo_EVA.o -lnetcdf -lnetcdff

/usr/bin/gfortran -ffree-line-length-none -o eva_build_forcing_files_on_levels eva_build_forcing_files_on_levels.f90 mo_EVA.o -lnetcdf -lnetcdff

/usr/bin/gfortran -ffree-line-length-none -o eva_build_forcing_files_on_zoptions eva_build_forcing_files_on_levels.f90 mo_EVA.o -lnetcdf -lnetcdff


#RUN
./eva_build_sulfate_file

./eva_build_forcing_files



