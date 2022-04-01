function schoolSlides() {
  return [
    '00-school/00-TITLE.md',
    '00-school/01-speaker-aal.md',
    '00-school/02-speaker-jbo.md',
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
    '02-installation/02-pip.md',
    '02-installation/03-virtualenv.md',
  ];
}

function letsGoSlides() {
  return [
    '03-lets-go/00-TITLE.md',
    '03-lets-go/01-hello-world.md',
    '03-lets-go/02-features.md',
    '03-lets-go/03-types.md',
    '03-lets-go/04-collections.md',
    '03-lets-go/05-functions.md',
    '03-lets-go/06-variables.md',
    '03-lets-go/07-conditional-statements.md',
    '03-lets-go/08-loops.md',
    '03-lets-go/09-exceptions.md',
    '03-lets-go/10-step-01.md',
    '03-lets-go/11-packages.md',
    '03-lets-go/12-imports.md',
    '03-lets-go/13-standard-library.md',
    '03-lets-go/14-step-02.md'
  ];
}

function letsGoFurtherSlides() {
  return [
    '04-lets-go-further/00-TITLE.md',
    '04-lets-go-further/01-hints.md',
    '04-lets-go-further/02-generators.md',
    '04-lets-go-further/03-decorators.md',
    '04-lets-go-further/04-lambdas.md',
    '04-lets-go-further/05-list-comprehension.md',
    '04-lets-go-further/06-step-06.md',
    '04-lets-go-further/07-classes.md',
    '04-lets-go-further/08-step-07.md',
    '04-lets-go-further/09-context-manager.md',
    '04-lets-go-further/10-callables.md',
    '04-lets-go-further/11-step-08.md',
    '04-lets-go-further/12-code-conventions.md',
    '04-lets-go-further/13-pylint.md',
    '04-lets-go-further/14-unit-tests.md',
    '04-lets-go-further/15-step-09.md',
  ];
}

function conclusionSlides() {
  return [
    '05-conclusion/00-TITLE.md',
  ];
}

function formation() {
  return [
    ...schoolSlides(),
    ...whyPythonSlides(),
    ...installationSlides(),
    ...letsGoSlides(),
    ...letsGoFurtherSlides(),
    ...conclusionSlides(),
  ].map(slidePath => {
    return { path: slidePath };
  });
}

export function usedSlides() {
  return formation();
}
