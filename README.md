# Abyssal Market

This is the source code behind [https://mutaplasmid.space/]. It's a website that
allows users to browse, appraise and buy abyssal modules that are available on
the contract market.

There are no tests, there is no CI, there is no quality control, there is no
documentation, there is only pain and suffering here. Run this software at your
own risk.

## Running a development instance

1. Make sure that Docker is installed, as well as Docker Compose.
1. Copy `secrets/configuration.template.yaml` to
   `secrets/configuration.dev.yaml` and enter the required information.
1. Run `docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up
   --build`.
1. Visit your instance at `localhost:33760`.

## Contributing

You can either make a pull request or submit an issue. Any contribution is
appreciated, even if it's just a feature request.
