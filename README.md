# Ansible Role: timesyncd

![GitHub](https://img.shields.io/github/license/jomrr/ansible-role-timesyncd)
![GitHub last commit](https://img.shields.io/github/last-commit/jomrr/ansible-role-timesyncd)
![GitHub issues](https://img.shields.io/github/issues-raw/jomrr/ansible-role-timesyncd)
[![dev](https://img.shields.io/github/actions/workflow/status/jomrr/ansible-role-timesyncd/dev.yml?branch=dev&label=dev)](https://github.com/jomrr/ansible-role-timesyncd/actions/workflows/dev.yml?query=branch%3Adev)
[![main](https://img.shields.io/github/actions/workflow/status/jomrr/ansible-role-timesyncd/main.yml?branch=main&label=main)](https://github.com/jomrr/ansible-role-timesyncd/actions/workflows/main.yml?query=branch%3Amain)

Ansible role to configure systemd-timesyncd.

## Purpose

Set the system timezone and configure systemd-timesyncd as an enabled, running
NTP client. Repeated runs with unchanged inputs are idempotent; a stopped or
disabled service is restored even when its configuration is unchanged.

## Scope

### Managed

- Installation of the time service and timezone data.
- Removal of the packages listed in timesyncd_remove_packages.
- The system timezone and complete /etc/systemd/timesyncd.conf file.
- Enabling, unmasking and starting systemd-timesyncd.service.
- Installation of epel-release on AlmaLinux to obtain systemd-timesyncd.

### Not Managed

- Per-link NTP servers and timesyncd.conf.d drop-ins.
- Serving NTP requests to other hosts.

## Requirements

- A systemd host on which systemd-timesyncd is permitted to adjust the system
  clock.

## Dependencies

```yaml
collections:
  - name: community.general
    version: '>=12.0.0'
```

## Role Variables

### `timesyncd_timezone`

Type: `str`. Required: `false`.

System timezone from the installed timezone database.

Default:

```yaml
timesyncd_timezone: Europe/Berlin
```

### `timesyncd_ntp_servers`

Type: `list`. Required: `false`.

NTP server hostnames or IP addresses, independent of the fallback server list.
An empty list clears the system server list; per-link servers remain available.

Default:

```yaml
timesyncd_ntp_servers:
  - 0.de.pool.ntp.org
  - 1.de.pool.ntp.org
```

### `timesyncd_fallback_servers`

Type: `list`. Required: `false`.

Fallback servers used when neither system nor per-link NTP servers are
configured.
An empty list omits FallbackNTP and retains the distribution's built-in fallback
servers.

Default:

```yaml
timesyncd_fallback_servers:
  - 2.de.pool.ntp.org
  - 3.de.pool.ntp.org
```

### `timesyncd_root_distance_max_seconds`

Type: `int`. Required: `false`.

Maximum acceptable root distance in seconds; must be positive.

Default:

```yaml
timesyncd_root_distance_max_seconds: 5
```

### `timesyncd_poll_interval_min_sec`

Type: `int`. Required: `false`.

Minimum polling interval in seconds; must be at least 16.

Default:

```yaml
timesyncd_poll_interval_min_sec: 32
```

### `timesyncd_poll_interval_max_sec`

Type: `int`. Required: `false`.

Maximum polling interval in seconds; must exceed
timesyncd_poll_interval_min_sec.

Default:

```yaml
timesyncd_poll_interval_max_sec: 2048
```

### `timesyncd_remove_packages`

Type: `list`. Required: `false`.

Conflicting time-service packages to remove before installing systemd-timesyncd.

Default:

```yaml
timesyncd_remove_packages:
  - ntp
  - chrony
```

## Managed Files

- `/etc/systemd/timesyncd.conf` Owned by root with mode 0644; previous contents
  are backed up.

## Check Mode

Package, timezone, configuration and service tasks use their modules' check-mode
support.

- A check before the first installation can fail because the repository,
  timezone data or service does not exist yet.

## Service Behavior

Configuration changes restart systemd-timesyncd; every run ensures the service
is enabled and running.

## Operational Notes

- Public variables use the `timesyncd_` prefix. Existing playbooks using
  `systemd_timesyncd_` must rename their variables while retaining the suffix.
- The NTP and fallback lists are independent. An empty NTP list clears the
  system server list; an empty fallback list omits FallbackNTP and retains the
  distribution's built-in fallback servers, matching the previous role behavior.
- Per-link servers can supplement the system server list, and drop-ins override
  the main configuration.
- systemd-timesyncd has no native validation command for a candidate
  timesyncd.conf. Argument specs validate input types and a domain assertion
  checks the numeric time limits before changes.
- Running the service does not guarantee immediate synchronization; an NTP
  server must be reachable and supply a usable time sample.

## Supported Platforms

| OS Family | Distribution | Version | Container Image |
| --------- | ------------ | ------- | --------------- |
| RedHat | AlmaLinux | latest | [jomrr/molecule-almalinux:latest](https://hub.docker.com/r/jomrr/molecule-almalinux) |
| Debian | Debian | latest | [jomrr/molecule-debian:latest](https://hub.docker.com/r/jomrr/molecule-debian) |
| RedHat | Fedora | latest | [jomrr/molecule-fedora:latest](https://hub.docker.com/r/jomrr/molecule-fedora) |
| Suse | OpenSuse Leap | latest | [jomrr/molecule-opensuse-leap:latest](https://hub.docker.com/r/jomrr/molecule-opensuse-leap) |
| Suse | OpenSuse Tumbleweed | latest | [jomrr/molecule-opensuse-tumbleweed:latest](https://hub.docker.com/r/jomrr/molecule-opensuse-tumbleweed) |
| Debian | Ubuntu | latest | [jomrr/molecule-ubuntu:latest](https://hub.docker.com/r/jomrr/molecule-ubuntu) |

## Example Playbook

### Configure UTC with explicit NTP servers

```yaml
---
- name: Configure time synchronization
  hosts: all
  gather_facts: true
  roles:
    - role: jomrr.timesyncd
      timesyncd_timezone: UTC
      timesyncd_ntp_servers:
        - time.example.net
      timesyncd_fallback_servers: []
      timesyncd_poll_interval_min_sec: 16
```

## References

- [timesyncd.conf](https://www.freedesktop.org/software/systemd/man/latest/timesyncd.conf.html)

## Author

[Jonas Mauer](https://github.com/jomrr)

## License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for the full license text.

Copyright (c) 2019-2026 Jonas Mauer.
