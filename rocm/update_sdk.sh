# details can be found in https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/native-install/ubuntu.html#installing

ROCM_VERSION=6.2

# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
SIGNED_KEY_SAVE_DEST=/etc/apt/trusted.gpg.d # /etc/apt/keyrings
sudo mkdir --parents --mode=0755 $SIGNED_KEY_SAVE_DEST

# Add rocm repository

# Download the key, convert the signing-key to a full
# keyring required by apt and store in the keyring directory
if [ -d $SIGNED_KEY_SAVE_DEST ]; then
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | \
    gpg --dearmor | sudo tee $SIGNED_KEY_SAVE_DEST/rocm.gpg > /dev/null
else
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | apt-key add -
fi

# register kernel-mode driver
echo "deb [arch=amd64 signed-by=$SIGNED_KEY_SAVE_DEST/rocm.gpg] https://repo.radeon.com/amdgpu/${ROCM_VERSION}/ubuntu jammy main" \
    | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update

# add the ROCm repository.
echo "deb [arch=amd64 signed-by=$SIGNED_KEY_SAVE_DEST/rocm.gpg] https://repo.radeon.com/rocm/apt/${ROCM_VERSION} jammy main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update

sudo apt install -y rocm