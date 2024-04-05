# ansible-role-systemd-timesyncd

![GitHub](https://img.shields.io/github/license/jomrr/ansible-role-systemd-timesyncd) [![Build Status](https://travis-ci.org/jomrr/ansible-role-systemd-timesyncd.svg?branch=main)](https://travis-ci.org/jomrr/ansible-role-systemd-timesyncd)

**Ansible role for configuring network time synchronisation
using `systemd-timesyncd`.**

> **Attention**:
> The packages `ntp` and `chrony` will be uninstalled by this role.

The role is only applied if `ansible_service_manager == 'systemd'`
and if `/usr/lib/systemd/systemd-timesyncd` exists.

## Supported Platforms

- Archlinux
- Debian 9, 10
- Ubuntu 16.04, 18.04, 20.04

## Requirements

Ansible 2.9 or higher.

## Variables

Variables and defaults for this role:

### defaults/main.yml

```yaml
---
# The role is disabled by default, so you do not get in trouble.
# Checked in tasks/main.yml which includes tasks.yml if enabled.
systemd_timesyncd_role_enabled: false

systemd_timesyncd_timezone: "Europe/Berlin"

systemd_timesyncd_ntp_servers:
  - 0.de.pool.ntp.org
  - 1.de.pool.ntp.org

systemd_timesyncd_fallback_servers:
  - 2.de.pool.ntp.org
  - 3.de.pool.ntp.org

# Maximum acceptable root distance as time value (in seconds), default = 5
systemd_timesyncd_root_distance_max_seconds: 5

# Minimum poll interval in seconds for ntp messages,
# must be greater than 16 and smaller than systemd_timesyncd_poll_interval_max_sec
systemd_timesyncd_poll_interval_min_sec: 32

# Maximum poll interval in seconds for ntp messages,
# must be greater than systemd_timesyncd_poll_interval_min_sec
systemd_timesyncd_poll_interval_max_sec: 2048
```

## Dependencies

None.

## Example Playbook

```yaml
---
# role: ansible-role-systemd-timesyncd
# file: site.yml

- hosts: all
  become: true
  vars:
    systemd_timesyncd_role_enabled: true
  roles:
    - role: 'ansible-role-systemd-timesyncd'
```

## License and Author

- Author:: [jomrr](https://github.com/jomrr/)
- Copyright:: 2020, [jomrr](https://github.com/jomrr/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jomrr/ansible-role-ntp/blob/master/LICENSE) file in repository.

## References

- [ArchWiki - systemd-timesyncd](https://wiki.archlinux.org/index.php/systemd-timesyncd)
- [Freedesktop.org](https://www.freedesktop.org/software/systemd/man/systemd-timesyncd.conf.html)
