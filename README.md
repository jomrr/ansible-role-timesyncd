# ansible-role-timesyncd

Ansible role for setting up systemd-timesyncd.

The role is only applied if

* ansible_os_family == "Archlinux"
* ansible_distribution == "Debian" and ansible_distribution_major_version is version ("9", ">=")
* ansible_distribution == "Ubuntu" and ansible_distribution_major_version is version ("16", ">=")

## Supported Platforms

* Archlinux
* Debian 9, 10
* Raspbian 9, 10
* Ubuntu 16.04, 18.04

## Requirements

Ansible 2.7 or higher is recommended.

## Variables

Variables and defaults for this role:

| variable | default value in defaults/main.yml | description |
| -------- | ---------------------------------- | ----------- |
| timesyncd_enabled | False | Determine whether role is enabled (True) or not (False) |
| timesyncd_timezone | 'Europe/Berlin' | Timezone for `timedatectl set-timezone`, see `timedatectl list-timezones` |
| timesyncd_ntp_servers | [ 0.de.pool.ntp.org, 1.de.pool.ntp.org ] | List of ntp servers |
| timesyncd_fallback_servers | [ 2.de.pool.ntp.org, 3.de.pool.ntp.org ] | List of ntp servers used as fallback |
| timesyncd_root_distance_max_seconds | 5 | Maximum acceptable root distance as time value (in seconds), default = 5 |
| timesyncd_poll_interval_min_sec | 32 | Minimum poll interval in seconds for ntp messages, must be greater than 16 and smaller than timesyncd_poll_interval_max_sec |
| timesyncd_poll_interval_max_sec | 2048 | Maximum poll interval in seconds for ntp messages, must be greater than timesyncd_poll_interval_min_sec |

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

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.

## References

* [ArchWiki - systemd-timesyncd](https://wiki.archlinux.org/index.php/systemd-timesyncd)
* [Freedesktop.org](https://www.freedesktop.org/software/systemd/man/timesyncd.conf.html)
