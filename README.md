## Dataset
Data used have a 'Public Domain' license and comes from Washington State's [Public Disclosure Commission].

### API docs
- [Contributions to Candidates and Political Committees]


## Local Development
To start developing, you will need to install [Docker].

- Run Docker desktop 
  - Mac: `open -a Docker` 
  - Windows: `start Docker`
  - Linux: `xdg-open Docker`
- Navigate to the [dev] directory
- Run `docker compose watch`

Changes in [src] directory will be updated in the apps container

[Contributions to Candidates and Political Committees]: https://dev.socrata.com/foundry/data.wa.gov/kv7h-kjye
[Public Disclosure Commission]: https://pdc.wa.gov/
[dev]: ./dev
[src]: ./src
[Docker]: https://docs.docker.com/engine/install/
