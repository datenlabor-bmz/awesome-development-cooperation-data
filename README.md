[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

# Awesome Development Cooperation Data 🌍

> A curated list of APIs and data sources about global development projects, for use by humans and machines.

## Contents 📚

- [Contents 📚](#contents-)
- [Terminology 📖](#terminology-)
- [Project Evaluation Repositories 🔍](#project-evaluation-repositories-)
- [Rigorous Evidence Repositories 📊](#rigorous-evidence-repositories-)
- [AI Apps 🤖](#ai-apps-)
- [Contributing 🤝](#contributing-)
- [License 📄](#license-)

## Terminology 📖

- **Database Interface**: Web-based interface for humans to browse and search data
- **API**: Application Programming Interface - allows machines to programmatically access data
- **API Spec**: Technical documentation describing how to use an API – one common standard is [OpenAPI](https://swagger.io/resources/open-api/)
- **MCP Server**: [Model Context Protocol](https://github.com/modelcontextprotocol) server – allows AI chatbots and tools to access data

## Project Evaluation Repositories 🔍

| Organization | Name | Database Interface | API | API Spec | MCP Server |
|-------------|------|-------------------|-----|----------|------------|
| **Global** |
| IATI | Registry / d-portal | [✓](https://d-portal.org/) | [✓](https://iatiregistry.org/api/) | [✓](https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/) | [(✓)](./interfaces/iati/mcp_server_iati/) |
| UNDP IEO | Evaluation Resource Center | [✓](https://erc.undp.org/evaluation/search) | [✓](https://erc.undp.org/api/) | – | – |
| World Bank | Project List | [✓](https://projects.worldbank.org/en/projects-operations/projects-list) | [✓](https://search.worldbank.org/api/v3/projects) | – | – |
| JPAL | Evaluations | [✓](https://www.povertyactionlab.org/evaluations) | [✓](https://www.povertyactionlab.org/views/ajax) | – | – |
| AfDB | Data Portal | [✓](https://projectsportal.afdb.org/dataportal/VProject/list) | – | – | – |
| ADB | Completed Evaluations | [✓](https://www.adb.org/who-we-are/evaluation/completed-evaluations) | – | – | – |
| IDB | Projects | [✓](https://www.iadb.org/en/project-search) | – | – | – |
| **United Kingdom** |
| FCDO | DevTracker | [✓](https://devtracker.fcdo.gov.uk/) | [✓](https://devtracker.fcdo.gov.uk/solr-response) | – | – |
| **Netherlands** |
| MBZ | Development Portal | [✓](https://www.nlontwikkelingshulp.nl/en/) | [✓](https://www.nlontwikkelingshulp.nl/api/jsonws) | – | – |
| **Germany** |
| BMZ | Transparenzportal | [✓](https://www.transparenzportal.bund.de/de/detailsuche) | [✓](https://www.transparenzportal.bund.de/api/v1/activities) | – | – |
| KfW | Interactive Database for Evaluation and Learning | [✓](https://www.kfw-entwicklungsbank.de/ideal/) | [✓](https://www.kfw-entwicklungsbank.de/kfw-ideal-service/api/projects) | – | – |
| GIZ | Medien- und Informationszentrum | [✓](https://publikationen.giz.de/esearcha/browse.tt.html) | – | – | – |
| PTB | Evaluierungsdatenbank | [✓](https://www.evaluierung.ptb.de/evaluierungsdatenbank) | – | – | – |

## Rigorous Evidence Repositories 📊

| Organization | Name | Database Interface | API | API Spec | MCP Server |
|-------------|------|-------------------|-----|----------|------------|
| 3ie | Development Evidence Portal | [✓](https://developmentevidence.3ieimpact.org/) | – | – | – |
| OpenAlex | Open catalog to the global research system | [✓](https://openalex.org/) | [✓](https://docs.openalex.org/) | [✓](https://github.com/Mearman/openalex-api-spec) | – |

## AI Apps 🤖

| Organization | App | Description | Availability | Open Source |
|-------------|------|-------------------|-----|----------|
| World Bank DIME | [ImpactAI](https://www.worldbank.org/en/about/unit/unit-dec/impactevaluation/ai/impact-ai) | Quantitative evidence synthesis tool | waitlist | planned |
| FCDO FTH | [Dev Explorer](https://app.devexplorer.ai) | IATI project search and anlysis | testing | planned |
| UNDP IEO | [AIDA](https://aida.undp.org/) | UNDP project search and analysis | public, v2 in development | |
| BMZ Data Lab | KIEZ | General AI assistant with focus on development | internal | planned |


## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the CC0 1.0 Universal License.
