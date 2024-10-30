## Dataset
Data used have a 'Public Domain' license and comes from Washington State's [Public Disclosure Commission].

### API docs
- [Contributions to Candidates and Political Committees]


## Local Development
To start developing, there are a few things you need to do to set up:
 - Install [Docker] Desktop
 - Generate an app token to access the API. Follow the instructions from [Generating App Tokens and API Keys]. 
   - Save this app token in your environment as `app_token`
   - DO NOT SAVE YOUR TOKEN IN THE CODE

### Running the application:
1. Run Docker desktop 
  - Mac: `open -a Docker` 
  - Windows: `start Docker`
  - Linux: `xdg-open Docker`
2. Navigate to the [dev] directory
3. Run `docker compose watch`


### Making updates
Changes in [src] directory will automatically be updated in the apps container


[Contributions to Candidates and Political Committees]: https://dev.socrata.com/foundry/data.wa.gov/kv7h-kjye
[Public Disclosure Commission]: https://pdc.wa.gov/
[dev]: ./dev
[src]: ./src
[Docker]: https://docs.docker.com/engine/install/
[Generating App Tokens and API Keys]: https://support.socrata.com/hc/en-us/articles/210138558-Generating-App-Tokens-and-API-Keys
