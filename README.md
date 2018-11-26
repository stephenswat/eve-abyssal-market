# Abyssal Market

This is the source code behind https://mutaplasmid.space/. It's a website that
allows users to browse, appraise and buy abyssal modules that are available on
the contract market.

There are no tests, there is no CI, there is no quality control, there is no
documentation, there is only pain and suffering here. Run this software at your
own risk.

## Installation

1. Install the requirements: `pipenv install`.
2. Configure the settings by copying
   `abyssal_markets/settings/local.template.py` to
   `abyssal_markets/settings/local.py` and configure it as any other Django
   project.
3. Run all migrations: `pipenv run python manage.py migrate`.
4. Run a web server (`pipenv run python manage.py runserver`) and a Huey
   consumer (`pipenv run python manage.py run_huey -w 4`) at the same time.

## Contributing

You can either make a pull request or submit an issue. Any contribution is
appreciated, even if it's just a feature request.
