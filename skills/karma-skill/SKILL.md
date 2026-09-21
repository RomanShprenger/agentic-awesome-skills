---
name: karma-skill
description: Generates Karma test runner configurations for browser-based JavaScript
  testing. Works with Jasmine, Mocha, or QUnit. Use when user mentions "Karma", "karma.conf.js",
  "browser test runner". Triggers…
languages:
- JavaScript
- TypeScript
category: unit-testing
license: MIT
metadata:
  author: TestMu AI
  version: '1.0'
source_repo: lambdatest/agent-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Karma Testing Skill

## Core Patterns

### karma.conf.js

```javascript
module.exports = function(config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine'],
    files: [
      'src/**/*.js',
      'test/**/*.spec.js'
    ],
    preprocessors: {
      'src/**/*.js': ['coverage']
    },
    reporters: ['progress', 'coverage'],
    coverageReporter: {
      type: 'html',
      dir: 'coverage/'
    },
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['Chrome', 'Firefox'],
    singleRun: false,
    concurrency: Infinity,

    // LambdaTest cloud browsers
    customLaunchers: {
      ChromeLT: {
        base: 'WebDriver',
        config: {
          hostname: 'hub.lambdatest.com',
          port: 80
        },
        browserName: 'Chrome',
        version: 'latest',
        name: 'Karma Test',
        tunnel: true,
        user: process.env.LT_USERNAME,
        accessKey: process.env.LT_ACCESS_KEY
      }
    }
  });
};
```

### Test with Jasmine Framework

```javascript
describe('StringUtils', () => {
  it('should capitalize first letter', () => {
    expect(StringUtils.capitalize('hello')).toBe('Hello');
  });

  it('should handle empty string', () => {
    expect(StringUtils.capitalize('')).toBe('');
  });
});
```

### Angular Integration

```javascript
// karma.conf.js for Angular
frameworks: ['jasmine', '@angular-devkit/build-angular'],
plugins: [
  require('karma-jasmine'),
  require('karma-chrome-launcher'),
  require('karma-coverage'),
  require('@angular-devkit/build-angular/plugins/karma')
],
```

## Setup: `npm install karma karma-jasmine karma-chrome-launcher karma-coverage --save-dev`
## Run: `npx karma start` or `npx karma start --single-run`
## Init: `npx karma init karma.conf.js`

## Deep Patterns

See `reference/playbook.md` for production-grade patterns:

| Section | What You Get |
|---------|-------------|
| §1 Production Configuration | Full karma.conf.js with coverage thresholds, reporters, CI launchers |
| §2 Component Testing | Service mocking, DOM interaction, form validation patterns |
| §3 HTTP Service Testing | HttpTestingController, error handling, retry testing |
| §4 Directive & Pipe Testing | Host component pattern, custom pipes with edge cases |
| §5 RxJS & Async Patterns | debounceTime, switchMap cancellation, subscription cleanup |
| §6 Router & NgRx Testing | RouterTestingModule, MockStore, selector overrides |
| §7 LambdaTest Integration | Cloud browser configuration for cross-browser testing |
| §8 CI/CD Integration | GitHub Actions with coverage, test reporting |
| §9 Debugging Table | 12 common problems with causes and fixes |
| §10 Best Practices | 14-item checklist for production Angular testing |

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
