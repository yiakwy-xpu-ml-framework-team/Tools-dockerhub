# make sure you have update_sdk_6.3.3.sh so the sources have been registered into apt sources list
apt install omniperf

# make sure you have right locales 
apt install locales
locale-gen "en_US.UTF-8"


# install dependencies
pip install -r requirements/run_rocm63+py312_rocprofiler_compute_auxiliar.txt

/opt/rocm-6.3.3/bin/rocprof-compute --version
