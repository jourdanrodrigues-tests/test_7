# JobBot Test

_Generated from [this Django template][template-link]._

This project runs entirely on Docker containers. Make sure to [have it][docker-download] in your environment.

## Style Guides

- [Git Commit Message][git-commit-message-style-guide]
- [Django REST in Style][django-rest-in-style]
- Flake8 with customizations ([check the setup file](setup.cfg))

## Setting up development environment

Before doing anything, run the following:

```bash
./scripts/setup_dev_env.sh
```

## Running the app

To make your life slightly easier, the script [`compose.sh`](compose.sh) is there for you to run commands in your
container. It's just a wrapper for `docker-compose`, so you might want to take a look at
[its documentation][docker-compose-docs].

### Production mode

```bash
./compose.sh up
```

### Development mode

```bash
./compose.sh dev up
```

[template-link]: https://github.com/jourdanrodrigues/django-template
[docker-download]: https://www.docker.com/community-edition#/download
[docker-compose-docs]: https://docs.docker.com/compose/reference/
[django-rest-in-style]: https://github.com/jourdanrodrigues/django-rest-in-style
[git-commit-message-style-guide]: https://github.com/slashsBin/styleguide-git-commit-message
