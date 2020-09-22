Vagrant.configure("2") do |config|
 config.vm.box = "hashicorp/bionic64"
 config.vm.provision "shell", inline: <<-SHELL
 sudo apt-get update
 
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
 
echo 'export PYENV_ROOT="C:/Users/King/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"

 SHELL
end