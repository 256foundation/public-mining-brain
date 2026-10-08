# Contributing - HashScope Documentation

> Source: https://256foundation.github.io/HashScope/contributing
> Collected: 2026-10-07
> Published: Unknown

# Contributing to HashScope[¶](https://256foundation.github.io#contributing-to-hashscope)

Thank you for your interest in contributing to HashScope!

## Development Setup[¶](https://256foundation.github.io#development-setup)

### Backend[¶](https://256foundation.github.io#backend)

### Frontend[¶](https://256foundation.github.io#frontend)

## Code Style[¶](https://256foundation.github.io#code-style)

### Python[¶](https://256foundation.github.io#python)

- Type hints required for all public functions
- Follow PEP 8
- Use `ruff` or `black` for formatting if available
- No blocking calls in async code
- Structured logging preferred

### TypeScript[¶](https://256foundation.github.io#typescript)

- Strict mode enabled
- Use functional components with hooks
- Prefer composition over complex components
- Follow existing component patterns

## Testing[¶](https://256foundation.github.io#testing)

All new features should include tests:

## Pull Request Process[¶](https://256foundation.github.io#pull-request-process)

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Architecture Guidelines[¶](https://256foundation.github.io#architecture-guidelines)

### Key Principles[¶](https://256foundation.github.io#key-principles)

1. **Never modify message contents** - byte-for-byte relay
2. **Best-effort parsing** - parse errors should not crash the proxy
3. **Security first** - treat all input as untrusted
4. **Type safety** - use type hints and TypeScript strictly
5. **Nostr publishing never blocks relay** - background tasks only

### Development Approach[¶](https://256foundation.github.io#development-approach)

HashScope is built in phases:

- **Core Proxy**: Transparent proxy with real-time visualization
- **Distributed Testing**: Agent fleet with Nostr coordination for load testing
- **Future Enhancements**: Additional protocol support, persistent storage, authentication

## Code Review[¶](https://256foundation.github.io#code-review)

All submissions require review. We look for:

- Code quality and style consistency
- Test coverage
- Documentation updates
- Performance considerations
- Security implications

## Reporting Issues[¶](https://256foundation.github.io#reporting-issues)

When reporting issues, include:

- HashScope version
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs
- System information (OS, Docker version, etc.)

## Feature Requests[¶](https://256foundation.github.io#feature-requests)

We welcome feature requests! Please:

- Check existing issues first
- Describe the use case
- Explain expected behavior
- Consider implementation complexity

## Questions?[¶](https://256foundation.github.io#questions)

Open an issue for any questions about contributing!

## License[¶](https://256foundation.github.io#license)

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

This project is licensed under the MIT License - see the [LICENSE](https://github.com/256foundation/HashScope/blob/main/LICENSE) file for details.

Copyright © 2024 256 Foundation
