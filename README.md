# ansible-role-timesyncd

![GitHub](https://img.shields.io/github/license/jam82/ansible-role-timesyncd) [![Build Status](https://travis-ci.org/jam82/ansible-role-timesyncd.svg?branch=master)](https://travis-ci.org/jam82/ansible-role-timesyncd)

**Ansible role for configuring network time synchronisation
using `systemd-timesyncd`.**

> **Attention**:
> The package `ntp` will be uninstalled by this role.

The role is only applied if `ansible_service_manager == 'systemd'`.

## Supported Platforms

- Archlinux
- Debian 9, 10
- Ubuntu 16.04, 18.04, 20.04

## Requirements

Ansible 2.8 or higher is recommended.

## Variables

Variables and defaults for this role:

```yaml
---
# role: ansible-role-timesyncd
# file: defaults/main.yml

# The role is disabled by default, so you do not get in trouble.
# Checked in tasks/main.yml which includes tasks.yml if enabled.
timesyncd_role_enabled: False

timesyncd_timezone: "Europe/Berlin"

timesyncd_ntp_servers:
  - 0.de.pool.ntp.org
  - 1.de.pool.ntp.org

timesyncd_fallback_servers:
  - 2.de.pool.ntp.org
  - 3.de.pool.ntp.org

# Maximum acceptable root distance as time value (in seconds), default = 5
timesyncd_root_distance_max_seconds: 5

# Minimum poll interval in seconds for ntp messages,
# must be greater than 16 and smaller than timesyncd_poll_interval_max_sec
timesyncd_poll_interval_min_sec: 32

# Maximum poll interval in seconds for ntp messages,
# must be greater than timesyncd_poll_interval_min_sec
timesyncd_poll_interval_max_sec: 2048
```

## Dependencies

None.

## Example Playbook

```yaml
---
# role: ansible-role-timesyncd
# file: site.yml

- hosts: timesyncd_systems
  become: True
  vars:
    timesyncd_enabled: True
  roles:
    - role: ansible-role-timesyncd
```

## License and Author

- Author:: [jam82](https://github.com/jam82/)
- Copyright:: 2020, [jam82](https://github.com/jam82/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jam82/ansible-role-ntp/blob/master/LICENSE) file in repository.

## References

- [ArchWiki - systemd-timesyncd](https://wiki.archlinux.org/index.php/systemd-timesyncd)
- [Freedesktop.org](https://www.freedesktop.org/software/systemd/man/timesyncd.conf.html)
