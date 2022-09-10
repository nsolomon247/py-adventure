Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2010"
  config.vm.provision :shell, path: "env/python_provisioning.sh"
  config.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = 3072
      vb.name = "python-prov"
  end
  config.vm.synced_folder "app/", "/home/vagrant/app/"
  config.vm.synced_folder "env/", "/home/vagrant/env"
end
