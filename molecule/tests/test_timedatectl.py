import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_timesyncd_conf(host):

    os = host.system_info.distribution
    conf = "/etc/systemd/timesyncd.conf"
    ntp_servers = "NTP=0.de.pool.ntp.org 1.de.pool.ntp.org"
    ntp_fallbacks = "FallbackNTP=2.de.pool.ntp.org 3.de.pool.ntp.org"

    if os == 'arch' or os == 'debian' or os == 'ubuntu':
        assert host.file(conf).user == 'root'
        assert host.file(conf).group == 'root'
        assert host.file(conf).mode == 0o644
        assert host.file(conf).contains(ntp_servers)
        assert host.file(conf).contains(ntp_fallbacks)


def test_timesyncd_service(host):

    if os == 'arch' or os == 'debian' or os == 'ubuntu':
        service = host.service("systemd-timesyncd")
        assert service.is_running
        assert service.is_enabled


def test_timedatectl(host):

    os = host.system_info.distribution

    if os == 'arch' or os == 'debian':
        cmd = "/usr/bin/timedatectl show-timesync"
        cmd_out = "SystemNTPServers=0.de.pool.ntp.org 1.de.pool.ntp.org"
    elif os == 'ubuntu':
        cmd = "/usr/bin/timedatectl"
        cmd_out = "System clock synchronized: yes"

    if os == 'arch' or os == 'debian' or os == 'ubuntu':
        assert host.run(cmd).rc == 0
        output = host.check_output(cmd)
        assert cmd_out in output
