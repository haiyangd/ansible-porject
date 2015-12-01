---

# ----------------- rbenv related vars ----------------------------

rbenv_install_cmd: "git clone https://github.com/sstephenson/rbenv.git /root/.rbenv"
rbenv_post_cmd_01: echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> /root/.bash_profile
rbenv_post_cmd_02: echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
rbbuild_install_cmd: "git clone https://github.com/sstephenson/ruby-build.git /root/.rbenv/plugins/ruby-build"

rbenv_dir: /root/.rbenv
rbbuild_dir: /root/.rbenv/plugins/ruby-build

ruby_install_cmd_01: /root/.rbenv/bin/rbenv install 2.2.1
ruby_install_cmd_02: /root/.rbenv/bin/rbenv global 2.2.1

gem_executable: /root/.rbenv/shims/gem

ssh_user_name: root
extra_pk_name: pubkeys.pub


# ----------------- vars for RHN register ----------------------------

rhn_user: qa@redhat.com
rhn_pwd: uBLybd5JSmkRHebA


# ----------------- vars for QEOS ----------------------------

qeos_usr: rhevhqe
qeos_pwd: rhevhqe
qeos_tenant_name: rhevh
qeos_auth_url: http://qeos.lab.eng.rdu2.redhat.com:5000/v2.0
qeos_key_name: cmdcenter
qeos_security_groups: default


qeos_image_id: 
qeos_image_name: 
qeos_image_list: [["f4627c9e-0393-4bcd-b59e-297b7b4130e9", "RHEL-7.1-Server-x86_64-released"],
                  ["aa103fe9-1423-4b82-b1fe-23d8b5c5898d", "rhel-guest-image-6.7-20150430.0"],
                  ["ac98e93d-34a3-437d-a7ba-9ad24c02f5b2", "rhel-guest-image-6.6-20150127.0"]]


qeos_flavor_id: 3
# 1 -> m1.tiny
# 2 -> m1.small
# 3 -> m1.medium
# 4 -> m1.large

qeos_vm_name:


nova_cmd: nova --os-auth-url=http://qeos.lab.eng.rdu2.redhat.com:5000/v2.0 --os-tenant-id=abf342c0b2654bf7a65e1c4dd653cbe5 --os-tenant-name=rhevh --os-username=rhevhqe --os-password=rhevhqe

# ----------------- vars for debug ----------------------------

debug_output: this is debug message



# ----------------- vars for RHEVM Yum Repo ----------------------

jboss_base_url: http://download.eng.tlv.redhat.com/pub/rhel/devel/candidates/JBEAP/JBEAP-6.4.1.CR2/composes/JBEAP-6.4.1-RHEL-6/Server/x86_64/os/
rhevm_base_url: "http://bob.eng.lab.tlv.redhat.com/builds/%s/%s"
rhevm_ver: "%s_%s"

rhevm_pass_word: 123qweP

notification_mail: rhevh-qe <rhevh-qe@redhat.com>
notification_mail_debug: yaniwang <yaniwang@redhat.com>


# ------------------ vars for cobbler and Igor --------------------

v_netowrk_name: netboot
v_ip: 192.168.15.1
v_netmask: 255.255.255.0
v_dhcp_start: 192.168.15.100
v_dhcp_end: 192.168.15.254
v_tftp_root: /var/lib/tftpboot

# ----------------- proxy for machine in lab which need to access internet ----------

redhat_proxy:
  http_proxy: http://squid.apac.redhat.com:3128
  https_proxy: http://squid.apac.redhat.com:3128
nic_name: ens5