# AI GitHub Coding Agent

> **An AI orchestration system that explores how large language models can be integrated into modern software development workflows, evolving from a constrained repository editor into an autonomous GitHub coding agent.**

---

# Project Status

**Status:** 🚧 Active Development

**Current Milestone:** **1.5 – CLI Input Generalization**

This project is being developed incrementally through a series of implementation milestones. Each milestone introduces a single architectural capability while maintaining a fully working system at every stage.

## Current Progress

| Component                        | Status         |
| -------------------------------- | -------------- |
| React Target Repository          | ✅ Complete     |
| Python Orchestration Application | ✅ Complete     |
| OpenAI Responses API Integration | ✅ Complete     |
| AI File Modification Pipeline    | ✅ Complete     |
| Build Verification               | ✅ Complete     |
| CLI User Input                   | ✅ Complete     |
| Repository Generalization        | 🚧 In Progress  |
| Repository Generalization        | ⏳ Planned      |
| Git Automation                   | ⏳ Planned      |
| Pull Request Automation          | ⏳ Planned      |

## Current MVP

The current implementation demonstrates a complete end-to-end AI editing workflow:

1. Read an existing React source file
2. Build an LLM prompt using the user's request and the current file contents
3. Generate a complete replacement file using the OpenAI Responses API
4. Validate the generated output
5. Replace the target source file
6. Verify that the application still builds successfully

The current scope is intentionally limited to a single target file while establishing a reliable architectural foundation for future milestones.

---

# Project Overview

Modern AI coding assistants demonstrate impressive code generation capabilities, but the surrounding engineering workflow—repository interaction, validation, Git automation, and software lifecycle management which is equally important.

This project explores that orchestration layer by incrementally building an end-to-end AI-assisted development workflow while intentionally maintaining a working system at every milestone.

The long-term objective is to build an autonomous system capable of understanding natural language development requests, analyzing an existing repository, generating code modifications, validating those changes, and automating portions of the GitHub development lifecycle.

Development follows an incremental, milestone-based approach. Each milestone introduces one new architectural capability while preserving a stable, working implementation.

---

## Related Repository

The current implementation is intentionally constrained to a single source file within a controlled target repository while the core orchestration workflow is being established.

**React Target Repository**

https://github.com/ark-96/ai-agent-portfolio

This repository serves as a controlled environment for developing and validating the orchestration pipeline while limiting the scope of repository analysis and code generation.

The target was intentionally chosen because it provides:

- A realistic software project structure
- Immediate visual feedback after AI-generated modifications
- Deterministic build verification using `npm run build`
- A manageable codebase for incremental architectural development

Although the current implementation is limited to this repository, the long-term architecture is being designed to support additional repository types through repository-specific validation workflows.

---

# Current Architecture

```text
User Request
      │
      ▼
Python CLI
      │
      ▼
Read Target Repository File
      │
      ▼
Construct Prompt
      │
      ▼
OpenAI Responses API
      │
      ▼
Generate Complete File Replacement
      │
      ▼
Validate Response
      │
      ▼
Overwrite Target File
      │
      ▼
React Build Verification
```

Current architecture consists of:

* React + TypeScript target repository (Vite)
* Python orchestration application
* OpenAI Responses API integration
* File reading and prompt construction
* AI-generated full file replacement
* Basic response validation
* Automated overwrite of the target file
* React build verification

---

# Completed Milestones

## Milestone 1.1 — Target Repository

* Created a React + TypeScript application using Vite
* Initialized Git version control
* Verified local development environment
* Verified successful production builds

---

## Milestone 1.2 — AI Orchestration

* Created a standalone Python orchestration project
* Configured a Python virtual environment
* Integrated the OpenAI Python SDK
* Added environment variable management
* Implemented a CLI entry point
* Successfully connected to the OpenAI Responses API

---

## Milestone 1.3 — AI-Driven Repository Modification

Implemented the first complete AI-assisted repository editing workflow.

The current system can:

* Read `src/App.tsx`
* Combine the user's request with the current file contents
* Generate an updated implementation using an LLM
* Perform basic output validation
* Replace the original source file
* Successfully rebuild the React application

This milestone establishes the first working end-to-end AI coding pipeline.

---

## Milestone 1.4 — CLI Input Generalization

Generalized the AI editing workflow by replacing the hardcoded modification request with command-line input.

The current system can:

* Accept arbitrary natural language modification requests via the CLI
* Validate user input before executing the editing pipeline
* Reuse the existing prompt construction and AI orchestration workflow without modification
* Produce different AI-generated outputs based on the supplied request

This milestone separates user interaction from the orchestration pipeline, transforming the project from a fixed proof of concept into a reusable command-line tool while intentionally retaining the existing single-file editing architecture.

---

# Current Capabilities

The current MVP can:

* Accept arbitrary natural language modification requests through the CLI
* Read an existing source file
* Build a structured prompt
* Generate updated code using the OpenAI Responses API
* Validate generated output
* Replace the original source file
* Produce a successful React build after modification

---

# Known Limitations

The current implementation intentionally prioritizes architectural simplicity over feature completeness.

Current limitations include:

* Modification request is currently hardcoded
* Only a single predefined source file can be modified
* Entire files are regenerated rather than patched
* No repository-wide code analysis
* No automated testing beyond successful builds
* No Git branch creation
* No commit generation
* No pull request automation
* Limited validation beyond basic output checks
* No rollback or recovery mechanism

These constraints are intentional while the core architecture is being established.

---

# Roadmap

## ✅ Phase 1 — Core Orchestration

* [x] Environment setup
* [x] Repository interaction
* [x] LLM integration
* [x] File modification
* [x] Build verification

---

## 🚧 Phase 2 — Workflow Generalization

* [x] CLI input
* [ ] Automated build validation
* [ ] Configurable targets
* [ ] Repository context selection/Target discovery
* [ ] Prompt refinement
---

## ⏳ Phase 3 — Development Automation

* [ ] Git branches
* [ ] Commits
* [ ] Pull requests
* [ ] Change summaries

---

## ⏳ Phase 4 — Reliability & Scale

* [ ] Multi-file edits
* [ ] Validation improvements
* [ ] Rollback
* [ ] Test execution
* [ ] Target adapters

---

# Design Principles

This project is guided by a small set of engineering principles:

* Build incrementally through clearly defined milestones
* Maintain a working system throughout development
* Introduce one architectural capability at a time
* Keep orchestration and target repositories separated
* Favor simplicity before optimization
* Design for maintainability and extensibility
* Validate changes continuously
* Accurately represent project capabilities without overstating maturity

The objective is not only to build an AI coding agent, but also to document the engineering decisions and iterative development process behind it, resulting in a portfolio quality demonstration of practical AI software engineering.
