import { SfeirThemeInitializer } from '../web_modules/sfeir-school-theme/dist/sfeir-school-theme.mjs';

function schoolSlides() {
  return [
    '00-school/00-TITLE.md',
    '00-school/02-speaker-ake.md',
    '00-school/03-repository.md',
    '00-school/04-app-screenshot.md',
    '00-school/05-what-we-will-do.md',
  ];
}

function whyPythonSlides() {
  return [
    '01-why-python/00-TITLE.md',
    '01-why-python/01-background.md',
    '01-why-python/02-strengthes.md',
    '01-why-python/03-use-cases.md',
    '01-why-python/04-future.md',
  ];
}

function installationSlides() {
  return [
    '02-installation/00-TITLE.md',
    '02-installation/01-python.md',
    '02-installation/02-virtualenv.md',
    '02-installation/03-mise.md',
    '02-installation/04-uv.md',
  ];
}

function letsGoSlides() {
  return [
    '03-lets-go/00-TITLE.md',
    '03-lets-go/01-hello-world.md',
    '03-lets-go/03-types.md',
    '03-lets-go/04-collections.md',
    '03-lets-go/05-idioms.md',
    '03-lets-go/06-functions.md',
    '03-lets-go/07-variables.md',
    '03-lets-go/08-conditional-statements.md',
    '03-lets-go/09-loops.md',
    '03-lets-go/10-step-01.md',
    '03-lets-go/11-exceptions.md',
    '03-lets-go/12-packages.md',
    '03-lets-go/13-imports.md',
    '03-lets-go/14-standard-library.md',
    '03-lets-go/15-step-02.md',
  ];
}

function letsGoFurtherSlides() {
  return [
    '04-lets-go-further/00-TITLE.md',
    '04-lets-go-further/01-hints.md',
    '04-lets-go-further/02-generators.md',
    '04-lets-go-further/03-decorators.md',
    '04-lets-go-further/04-comprehensions-lambdas.md',
    '04-lets-go-further/05-classes.md',
    '04-lets-go-further/06-dataclasses.md',
    '04-lets-go-further/07-context-managers.md',
    '04-lets-go-further/08-async.md',
    '04-lets-go-further/09-code-conventions.md',
    '04-lets-go-further/10-quality.md',
    '04-lets-go-further/11-tests.md',
    '04-lets-go-further/12-step-03.md',
  ];
}

function fastApiSlides() {
  return [
    '05-fastapi/00-TITLE.md',
    '05-fastapi/01-fastapi.md',
    '05-fastapi/02-pydantic.md',
    '05-fastapi/03-lab-step-01.md',
    '05-fastapi/04-sqlmodel.md',
    '05-fastapi/05-lab-step-02.md',
  ];
}

function mcpSlides() {
  return [
    '06-mcp/00-TITLE.md',
    '06-mcp/01-what-is-mcp.md',
    '06-mcp/02-security.md',
    '06-mcp/03-fastmcp.md',
    '06-mcp/04-connect-agents.md',
    '06-mcp/05-from-fastapi.md',
    '06-mcp/06-labs.md',
  ];
}

function conclusionSlides() {
  return [
    '07-conclusion/00-TITLE.md',
    '07-conclusion/01-recap.md',
    '07-conclusion/02-resources.md',
    '07-conclusion/03-feedback.md',
  ];
}

function formation() {
  return [
    ...schoolSlides(),
    ...whyPythonSlides(),
    ...installationSlides(),
    ...letsGoSlides(),
    ...letsGoFurtherSlides(),
    ...fastApiSlides(),
    ...mcpSlides(),
    ...conclusionSlides(),
  ].map((slidePath) => {
    return { path: slidePath };
  });
}

SfeirThemeInitializer.init(formation);
